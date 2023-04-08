from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from apps.women.views import WomenViewSet

router = routers.DefaultRouter()
router.register(r"women", WomenViewSet, "women")

urlpatterns = [
    path("__debug__/", include("debug_toolbar.urls")),
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
