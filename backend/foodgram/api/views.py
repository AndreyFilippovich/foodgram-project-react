import io

from django.http import HttpResponse
from reportlab.pdfgen import canvas

from django.db.models import Sum
from django.http import FileResponse
from django.utils.translation import gettext as _
from django_filters.rest_framework import DjangoFilterBackend
from djoser.views import UserViewSet
from recipes.models import (Favorite, Ingredient, IngredientRecipe, Recipe,
                            ShoppingCart, Tag)
from reportlab.pdfbase import pdfmetrics, ttfonts
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas
from rest_framework import permissions, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from users.models import Follow, User

from .filters import IngredientSearchFilter, RecipeFilter
from .mixins import CustomRecipeModelViewSet, ListRetrieveCustomViewSet
from .pagination import LimitPagePagination
from .permissions import AuthorOrReadOnly
from .serializers import (FavoriteSerializers, FollowUserSerializers,
                          IngredientSerializers, RecipeSerializers,
                          ShoppingCardSerializers, TagSerializers)


class CustomUserViewSet(UserViewSet):
    """
    Переопределение UserViewSet добавление новых эндпоинтов для подписок.
    1- Подписаться;
    2- Удалить подпису;
    3- Список подписок.
    Пагинация:
    Page- страница (6 обънктов на страницу по умолчанию);
    Limit- ограничение на вывод объектов на одну страницу;
    Recipes_limit- количество рецептов у автора.
    """
    pagination_class = LimitPagePagination

    @action(detail=False, permission_classes=[permissions.IsAuthenticated])
    def subscriptions(self, request):
        queryset = Follow.objects.filter(user=request.user)
        page = self.paginate_queryset(queryset)
        serializer = FollowUserSerializers(page, many=True,
                                           context={'request': request})
        return self.get_paginated_response(serializer.data)

    @action(detail=True,
            methods=['post'],
            permission_classes=[permissions.IsAuthenticated])
    def subscribe(self, request, id=None):
        user = request.user
        author = get_object_or_404(User, id=id)
        if user == author:
            return Response({'errors':
                            _('Вы не можете подписаться на себя.')},
                            status=status.HTTP_400_BAD_REQUEST)
        if Follow.objects.filter(user=user, author=author).exists():
            return Response({'errors':
                            _('Вы уже подписались на автора.')},
                            status=status.HTTP_400_BAD_REQUEST)
        Follow.objects.create(user=user, author=author)
        queryset = Follow.objects.get(user=request.user, author=author)
        serializer = FollowUserSerializers(queryset,
                                           context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @subscribe.mapping.delete
    def subscribe_del(self, request, id=None):
        user = request.user
        author = get_object_or_404(User, id=id)
        if not Follow.objects.filter(user=user, author=author).exists():
            return Response({'errors': 'Подписки не существует.'},
                            status=status.HTTP_400_BAD_REQUEST)
        Follow.objects.get(user=user, author=author).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TagViewSet(ListRetrieveCustomViewSet):
    """
    ViewSet для TagSerializers только GET запросы.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializers
    permission_classes = (permissions.AllowAny,)


class IngredientViewSet(ListRetrieveCustomViewSet):
    """
    ViewSet для IngredientSerializers только GET запросы.
    Фильтр по названиям ингридиентов.
    """
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializers
    permission_classes = (permissions.AllowAny,)
    filter_backends = (IngredientSearchFilter,)
    search_fields = ('name',)


class RecipeViewSet(CustomRecipeModelViewSet):
    """
    Receptviews с дополнительными методами:
    1- Добавить/удалить из избранного;
    2- Добавить/удалить из списка покупок;
    3- Получите список покупок в формате PDF.
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializers
    pagination_class = LimitPagePagination
    filter_backends = (DjangoFilterBackend, )
    filter_class = RecipeFilter
    permission_classes = (AuthorOrReadOnly,)

    @action(detail=True, methods=['post', 'delete'],
            permission_classes=[permissions.IsAuthenticated])
    def favorite(self, request, pk=None):
        if request.method == 'POST':
            return self.add_obj(model=Favorite,
                                pk=pk,
                                serializers=FavoriteSerializers,
                                user=request.user)
        elif request.method == 'DELETE':
            return self.del_obj(model=Favorite, pk=pk, user=request.user)
        return None

    @action(methods=['POST', 'DELETE'], detail=True)
    def shopping_cart(self, request, pk):
        return self.action_post_delete(pk, ShoppingCardSerializers)

    @action(detail=False)
    def download_shopping_cart(self, request):
        response = HttpResponse(content_type='application/pdf', )
        response['Content-Disposition'] = (
            "attachment; filename='shopping_cart.pdf'"
        )
        p = canvas.Canvas(response)
        arial = ttfonts.TTFont('Arial', 'data/arial.ttf')
        pdfmetrics.registerFont(arial)
        p.setFont('Arial', 14)

        ingredients = IngredientRecipe.objects.filter(
            recipe__shopping_cart__user=request.user).values_list(
            'ingredient__name', 'amount', 'ingredient__measurement_unit')

        ingr_list = {}
        for name, amount, unit in ingredients:
            if name not in ingr_list:
                ingr_list[name] = {'amount': amount, 'unit': unit}
            else:
                ingr_list[name]['amount'] += amount
        height = 700

        p.drawString(100, 750, 'Список покупок')
        for i, (name, data) in enumerate(ingr_list.items(), start=1):
            p.drawString(
                80, height,
                f"{i}. {name} – {data['amount']} {data['unit']}")
            height -= 25
        p.showPage()
        p.save()
        return response
