from django.urls import path
from .views import empresaVista
from .views import rolVista
from .views import usuarioVista
from .views import movimientofinancieroVista



urlpatterns=[
    path('empresa/', empresaVista.as_view(), name="Listar"),
    path('rol/', rolVista.as_view(), name="Listar"),
    path('usuario/', usuarioVista.as_view(), name="Listar"),
    path('movimientofinanciero/', movimientofinancieroVista.as_view(), name="Listar"),
    path ('empresa/<int:doc>',empresaVista.as_view(), name="Actualizar"),
    path ('rol/<int:doc>',rolVista.as_view(), name="Actualizar"),
    path ('usuario/<int:doc>',usuarioVista.as_view(), name="Actualizar"),
    path ('movimientofinanciero/<int:doc>',movimientofinancieroVista.as_view(), name="Actualizar")
        ]

