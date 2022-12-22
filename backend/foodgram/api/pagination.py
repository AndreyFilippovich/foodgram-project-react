from rest_framework.pagination import PageNumberPagination


class LimitPagePagination(PageNumberPagination):
    """
    Собственный пагинатор:
    page - номер страницы
    limit - количество объектов на странице.
    """
    page_size = 6
    page_size_query_param = 'limit'
