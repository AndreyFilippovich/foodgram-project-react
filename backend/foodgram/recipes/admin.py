from django.contrib import admin

from .models import (Favorite, Ingredient, IngredientRecipe, Recipe,
                     ShoppingCart, Tag)


class TagAdmin(admin.ModelAdmin):
    """
    Админ панель для модели тегов.
    """
    list_display = ("name", "color", "slug")
    search_fields = ('name', 'slug',)


class IngredientAdmin(admin.ModelAdmin):
    """
    Админ панель для модели ингредиентов.
    """
    list_display = ('name', 'measurement_unit')
    list_filter = ('name',)


class IngredientInLine(admin.StackedInline):
    """
    Добавляет набор ингредиентов для рецептов.
    """
    model = IngredientRecipe
    extra = 3


class RecipeAdmin(admin.ModelAdmin):
    """
    Админ панель дял модели рецептов.
    """
    list_display = ('author', 'name', 'text', 'cooking_time', 'favorites')
    list_filter = ('author', 'name', 'tags')
    inlines = [IngredientInLine]

    def favorites(self, obj):
        """
        Подсчитывает сколько раз рецепт добавлялся в избранное.
        """
        return obj.favorites.count()


class ShoppingCartAdmin(admin.ModelAdmin):
    """
    Админ панель для модели корзины покупок.
    """
    list_display = ('user', 'recipe')
    search_fields = ('user', 'recipe',)


class FavoriteAdmin(admin.ModelAdmin):
    """
    Админ панель для модели избранного.
    """
    list_display = ('recipe', 'user')
    list_filter = ('user',)


admin.site.register(Tag, TagAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(ShoppingCart, ShoppingCartAdmin)
admin.site.register(Favorite, FavoriteAdmin)
