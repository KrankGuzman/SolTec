from django.conf.urls import include
from apps.organizacion.views import index
from django.urls import path

urlpatterns = [
    path('', index),
]