from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers

from apps.women.views import WomenViewSet

router = routers.DefaultRouter()
router.register(r"women", WomenViewSet, basename="women")

urlpatterns = [
    path("__debug__/", include("debug_toolbar.urls")),
    path("admin/", admin.site.urls),
    path("api/", include(router.urls), name="women"),
    path("auth/", include("rest_framework.urls")),
]
