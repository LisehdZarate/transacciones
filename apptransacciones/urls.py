from django.urls import path
from .views import empresaVista
from .views import cargoVista
from .views import usuarioVista
from .views import movimientofinancieroVista
from .views import empresaUsuarioVista
from .views import login
from . import views



urlpatterns=[
    path('empresa/', empresaVista.as_view(), name="Listar"),
    path('cargo/', cargoVista.as_view(), name="Listar"),
    path('login/usuario/', usuarioVista.as_view(), name="Listar"),
    path('movimientofinanciero/', movimientofinancieroVista.as_view(), name="Listar"),
    path('empresa/<int:empId>',empresaVista.as_view(), name="Actualizar"),
    path('cargo/<int:doc>',cargoVista.as_view(), name="Actualizar"),
    path('usuario/<int:usuId>',usuarioVista.as_view(), name="Actualizar"),
    path('usuario/',usuarioVista.as_view(), name="Listar"),
    path('movimientofinanciero/<int:movId>',movimientofinancieroVista.as_view(), name="Actualizar"),
    path('actualizadomov/',views.editarmovimiento, name="Actualizar"),
    path('empresaUsuario/', empresaUsuarioVista.as_view(), name="Listar"),
    path('empresaUsuario/<int:doc>',empresaUsuarioVista.as_view(), name="Actualizar"),
    path('login/',login.loginusuario, name="login usuario" ),
    path('gestionusuario',views.gestionusuario, name="gestion" ),
    path('login/frminsertar',views.frminsertar, name="registrar" ),
    path('formulario/',login.formularioregistro,name="Registro"),
    path('formulariousu/', views.formulariousu,name="Registro"),
    path('actualizarusu/',views.editarusuario,name="Actualizar"),
    path('formularioemp/', views.formularioemp,name="Registro"),
    path('actualizaremp/',views.editarempresa,name="Actualizar"),
    path('eliminarmovimiento/<int:movId>',views.eliminarMov, name="eliminar" ),
    path('eliminarusuario/<int:usuId>',views.eliminarUsu, name="eliminar" ),
    path('eliminarempresa/<int:empId>',views.eliminarEmp, name="eliminar" ),
        ]

