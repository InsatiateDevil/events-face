from rest_framework.pagination import CursorPagination


class VenueEventPaginator(CursorPagination):
    ordering = "date"
    page_size = 10
    max_page_size = 10
    page_size_query_param = "page_size"
