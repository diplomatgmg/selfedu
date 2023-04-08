from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.women.models import Women
from apps.women.permissions import OwnerCanChange
from apps.women.serializers import WomenSerializer


class WomenViewSet(viewsets.ModelViewSet):
    serializer_class = WomenSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, OwnerCanChange]

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        return Women.objects.filter(pk=pk) if pk else Women.objects.all()[:3]
