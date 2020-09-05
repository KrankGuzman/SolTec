from django.conf.urls import include
from apps.organizacion.views import index, almacen_view, almacen_list, almacen_edit, almacen_delete
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('registrar', almacen_view, name='almacen_crear'),
    path('listar', almacen_list, name='almacen_listar'),
    path('actualizar/<almacen_id>/', almacen_edit, name='almacen_editar'),
    path('eliminar/<almacen_id>/', almacen_delete, name='almacen_eliminar'),
]