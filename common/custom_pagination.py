from collections import OrderedDict

from rest_framework.pagination import PageNumberPagination, CursorPagination
from rest_framework.response import Response


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 100
    page_query_param = 'page'

    def get_results(self, data):
        return Response(
            OrderedDict([
                ("data", data),
            ])
        )

    def get_paginated_response(self, data):
        return Response({
            'prev_page': self.get_previous_link(),
            'next_page': self.get_next_link(),
            'total_pages': self.page.paginator.num_pages,
            'total_records': self.page.paginator.count,
            'data': data,
        })


class CustomCursorSetPagination(CursorPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    ordering = '-pk'
    cursor_query_param = 'page'

    def get_results(self, data):
        return Response(
            OrderedDict([
                ("data", data),
            ])
        )

    def get_paginated_response(self, data):
        next_page_link = self.get_next_link()
        next_page_id = next_page_link.split('?page=')[-1] if next_page_link else None
        prev_page_link = self.get_previous_link()
        prev_page_id = prev_page_link.split('?page=')[-1] if prev_page_link else None
        return Response({
            'prev_page': self.get_previous_link(),
            'next_page': self.get_next_link(),
            'prev_page_id': prev_page_id,
            'next_page_id': next_page_id,
            'data': data,
        })


class SupplierPagination(CustomPageNumberPagination):
    page_query_param = 'page_sup'


class ItemPagination(CustomPageNumberPagination):
    page_query_param = 'page_product'
