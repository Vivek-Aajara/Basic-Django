from django.urls import path
from .views import img

urlpatterns = [
    path("", img, name="img"),
]