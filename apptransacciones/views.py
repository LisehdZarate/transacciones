import json
from django.shortcuts import render
from django.views import View
from .models import empresa, movimientofinanciero, usuario
from django.http.response import JsonResponse

class empresaVista(View):
   
    def get(self, request): 
        emp=list(empresa.objects.values())
        datos={'listadoEmpresa': emp}
        return JsonResponse (datos)

    def post (self, request):
        datos=json.loads(request.body)
        empresa.objects.create(nit_empresa=datos["nit_empresa"], nombre_Empresa=datos["nombre_Empresa"], ciudad_Empresa=datos["ciudad_Empresa"], 
        direccion_Empresa=datos["direccion_Empresa"])
        return JsonResponse(datos)

class rolVista(View):
   
    def get(self, request): 
        rol1=list(rol.objects.values())
        datos={'listadoRol': rol1}
        return JsonResponse (datos)

    def post (self, request):
        datos=json.loads(request.body)
        rol.objects.create(rol_id=datos["rol_id"], estado=datos["estado"], rol=datos["rol"])
        return JsonResponse(datos)

class usuarioVista(View):
   
    def get(self, request): 
        usu=list(usuario.objects.values())
        datos={'listadoUsuario': usu}
        return JsonResponse (datos)

    def post (self, request):
        datos=json.loads(request.body)
        usuario.objects.create(usuario_id=datos["usuario_id"], nombre_Usu=datos["nombre_Usu"], apellido_Usu=datos["apellido_Usu"], correoUsu=datos["correoUsudo"], 
        login=datos["login"], password_Usu=datos["password_Usu"],fk_rol=datos["fk_rol"])
        return JsonResponse(datos)

class movimientofinancieroVista(View):
   
    def get(self, request): 
        mov=list(movimientofinanciero.objects.values())
        datos={'listadoMovimiento': mov}
        return JsonResponse (datos)

    def post (self, request):
        datos=json.loads(request.body)
        movimientofinanciero.objects.create(movimiento_id=datos["movimiento_id"], fecha=datos["fecha"], fk_usuario=datos["fk_usuario"], fk_empresa=datos["fk_empresa"], 
        descripcion_movimiento=datos["descripcion_movimiento"], tipo_movimiento=datos["tipo_movimiento"],saldo=datos["saldo"])
        return JsonResponse(datos)   


