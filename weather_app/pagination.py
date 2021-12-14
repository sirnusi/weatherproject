from rest_framework.pagination import PageNumberPagination

class NotePagination(PageNumberPagination):
    page_size = 3
    # page_query_param = 'notes'
    page_size_query_param = 'notes'