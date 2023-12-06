from rest_framework.pagination import PageNumberPagination


class TaskPaginator(PageNumberPagination):
    """ Пагинатор для вывода по 5 задач на страницу """
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 5
