from rest_framework import generics

from apps.women.models import Women
from apps.women.serializers import WomenSerializer


class WomenAPIView(generics.ListAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
