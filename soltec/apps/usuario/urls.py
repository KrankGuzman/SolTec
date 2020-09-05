from django.conf.urls import url
from apps.usuario.views import RegistroUsuario
from django.urls import path

urlpatterns = [
    path('registrarusuario', RegistroUsuario.as_view(), name='registrarusuario'),
]