from django.urls import path
from .views import empresaVista
from .views import rolVista
from .views import usuarioVista
from .views import movimientofinancieroVista



urlpatterns=[
    path('empresa/', empresaVista.as_view(), name="Listar"),
    path('rol/', rolVista.as_view(), name="Listar"),
    path('usuario/', usuarioVista.as_view(), name="Listar"),
    path('movimientofinanciero/', movimientofinancieroVista.as_view(), name="Listar")
        ]

