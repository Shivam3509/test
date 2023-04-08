from rest_framework import pagination

class CustomPageNumberPagination(pagination.PageNumberPagination):
    """Custom page number pagination."""

    page_size = 2
    max_page_size = 4
    page_size_query_param = 'page_size'