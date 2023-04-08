from rest_framework import viewsets, permissions

from apps.women.models import Women
from apps.women.serializers import WomenSerializer


class WomenViewSet(viewsets.ModelViewSet):
    serializer_class = WomenSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        return Women.objects.filter(pk=pk) if pk else Women.objects.all()[:3]
