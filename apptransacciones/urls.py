from django.urls import path
from .views import empresaVista
from .views import cargoVista
from .views import usuarioVista
from .views import movimientofinancieroVista
from .views import empresaUsuarioVista



urlpatterns=[
    path('empresa/', empresaVista.as_view(), name="Listar"),
    path('cargo/', cargoVista.as_view(), name="Listar"),
    path('usuario/', usuarioVista.as_view(), name="Listar"),
    path('movimientofinanciero/', movimientofinancieroVista.as_view(), name="Listar"),
    path ('empresa/<int:doc>',empresaVista.as_view(), name="Actualizar"),
    path ('cargo/<int:doc>',cargoVista.as_view(), name="Actualizar"),
    path ('usuario/<int:doc>',usuarioVista.as_view(), name="Actualizar"),
    path ('movimientofinanciero/<int:doc>',movimientofinancieroVista.as_view(), name="Actualizar"),
    path('empresaUsuario/', empresaUsuarioVista.as_view(), name="Listar"),
    path ('empresaUsuario/<int:doc>',empresaUsuarioVista.as_view(), name="Actualizar"),
        ]

