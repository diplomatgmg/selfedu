from django.urls import path

from apps.women.views import WomenAPIView

app_name = "women"

urlpatterns = [path("", WomenAPIView.as_view(), name="list")]
