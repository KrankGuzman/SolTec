from django.conf.urls import include
from apps.organizacion.views import index, almacen_view, almacen_list, almacen_edit, almacen_delete, \
    AlmacenList, AlmacenCreate, AlmacenUpdate, AlmacenDelete
from django.urls import path
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', index, name='index'),
    path('registrar', login_required(AlmacenCreate.as_view()), name='almacen_crear'),
    path('listar', login_required(AlmacenList.as_view()), name='almacen_listar'),
    path('actualizar/<int:pk>/', login_required(AlmacenUpdate.as_view()), name='almacen_editar'),
    path('eliminar/<int:pk>/', login_required(AlmacenDelete.as_view()), name='almacen_eliminar'),
]