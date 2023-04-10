from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.women.models import Women
from apps.women.permissions import OwnerCanChange
from apps.women.serializers import WomenSerializer


class WomenAPIListPagination(PageNumberPagination):
    page_size = 5
    page_query_param = "page"


class WomenViewSet(viewsets.ModelViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, OwnerCanChange]
    pagination_class = WomenAPIListPagination
