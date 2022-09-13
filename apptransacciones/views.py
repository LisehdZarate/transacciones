from calendar import c
import json
from django.shortcuts import render
from django.views import View
from .models import empresa, movimientofinanciero, rol, usuario
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt



class empresaVista(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request,*args, **kwargs)

    
    def get(self, request): 
        emp=list(empresa.objects.values())
        datos={'listadoEmpresa': emp}
        return JsonResponse (datos)

    def post (self, request):
        datos=json.loads(request.body)
        empresa.objects.create(nit_empresa=datos["nit_empresa"]
        , nombre_Empresa=datos["nombre_Empresa"], ciudad_Empresa=datos["ciudad_Empresa"]
        , direccion_Empresa=datos["direccion_Empresa"])
        return JsonResponse(datos)

    def put(self,request,doc):
      datos=json.loads(request.body)
      emp=list(empresa.objects.filter(nit_empresa=doc).values())
      if len(emp)>0:
         emp=empresa.objects.get(nit_empresa=doc)
         emp.nombre_Empresa=datos["nombre_Empresa"]
         emp.ciudad_Empresa=datos["ciudad_Empresa"]
         emp.direccion_Empresa=datos["direccion_Empresa"]
         emp.save()
         mensaje={"Respuesta":"Datos actualizados"}
      else:
         mensaje={"Respuesta":"Datos no encontrados"}
      return JsonResponse(mensaje)
 
    def delete(self,request,doc):
        emp=list(empresa.objects.filter(nit_empresa=doc).values())
        if len(emp)>0:
               empresa.objects.filter(nit_empresa=doc).delete()
               mensaje={"Respuesta":"Registro eliminado"}
        else:   
               mensaje={"Respuesta":"Registro no encontrado"}
        return JsonResponse (mensaje) 

class rolVista(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request,*args, **kwargs)
   
    def get(self, request): 
        rol1=list(rol.objects.values())
        datos={'listadoRol': rol1}
        return JsonResponse (datos)

    def post (self, request):
        datos=json.loads(request.body)
        rol.objects.create(rol_id=datos["rol_id"], estado=datos["estado"], rol=datos["rol"])
        return JsonResponse(datos)

    def put(self,request,doc):
      datos=json.loads(request.body)
      rol1=list(rol.objects.filter(rol_id=doc).values())
      if len(rol1)>0:
         roles=rol.objects.get(rol_id=doc)
         roles.estado=datos["estado"]
         roles.rol=datos["rol"]
         roles.save()
         mensaje={"Respuesta":"Datos actualizados"}
      else:
         mensaje={"Respuesta":"Datos no encontrados"}
      return JsonResponse(mensaje)
 
    def delete(self,request,doc):
        rol1=list(rol.objects.filter(rol_id=doc).values())
        if len(rol1)>0:
               rol.objects.filter(rol_id=doc).delete()
               mensaje={"Respuesta":"Registro eliminado"}
        else:   
               mensaje={"Respuesta":"Registro no encontrado"}
        return JsonResponse (mensaje) 

class usuarioVista(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request,*args, **kwargs)
   
    def get(self, request): 
        usu=list(usuario.objects.values())
        datos={'listadoUsuario': usu}
        return JsonResponse (datos)

    def post (self, request):
        datos=json.loads(request.body)
        usuario.objects.create(usuario_id=datos["usuario_id"]
        , nombre_Usu=datos["nombre_Usu"]
        , apellido_Usu=datos["apellido_Usu"]
        , correoUsu=datos["correoUsu"]
        , login=datos["login"]
        , password_Usu=datos["password_Usu"]
        ,fk_rol=rol.objects.get(rol_id = datos["fk_rol"]))
        return JsonResponse(datos)

    def put(self,request,doc):
      datos=json.loads(request.body)
      usu=list(usuario.objects.filter(usuario_id=doc).values())
      if len(usu)>0: 
         usuario1=usuario.objects.get(usuario_id=doc)
         usuario1.nombre_Usu=datos["nombre_Usu"]
         usuario1.apellido_Usu=datos["apellido_Usu"]
         usuario1.correoUsu=datos["correoUsu"]
         usuario1.login=datos["login"]
         usuario1.password_Usu=datos["password_Usu"]
         usuario1.fk_rol=rol.objects.get(rol_id = datos["fk_rol_id"])
         usuario1.save()
         mensaje={"Respuesta":"Datos actualizados"}
      else:
         mensaje={"Respuesta":"Datos no encontrados"}
      return JsonResponse(mensaje)
 
    def delete(self,request,doc):
        usu=list(usuario.objects.filter(usuario_id=doc).values())
        if len(usu)>0:
               usuario.objects.filter(usuario_id=doc).delete()
               mensaje={"Respuesta":"Registro eliminado"}
        else:   
               mensaje={"Respuesta":"Registro no encontrado"}
        return JsonResponse (mensaje) 

class movimientofinancieroVista(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request,*args, **kwargs)
   
    def get(self, request): 
        mov=list(movimientofinanciero.objects.values())
        datos={'listadoMovimiento': mov}
        return JsonResponse (datos)

    def post (self, request):
        datos=json.loads(request.body)
        movimientofinanciero.objects.create(
            movimiento_id=datos["movimiento_id"]
            ,fecha=datos["fecha"]
            ,fk_usuario=usuario.objects.get(usuario_id = datos["fk_usuario"])
            ,fk_empresa=empresa.objects.get(nit_empresa = datos["fk_empresa"])
            ,descripcion_movimiento=datos["descripcion_movimiento"]
            ,tipo_movimiento=datos["tipo_movimiento"]
            ,saldo=datos["saldo"])
        return JsonResponse(datos)

    def put(self,request,doc):
        datos=json.loads(request.body)
        mov=list(movimientofinanciero.objects.filter(movimiento_id=doc).values())
        searchUser = list(usuario.objects.filter(usuario_id = datos["fk_usuario"]).values())
        if len(searchUser)==0:
            mensaje={"Respuesta":"Usuario no encontrado"}
            return JsonResponse(mensaje)

        searchUser = list(empresa.objects.filter(nit_empresa = datos["fk_empresa"]).values())
        if len(searchUser)==0:
            mensaje={"Respuesta":"Empresa no encontrada"}
            return JsonResponse(mensaje)


        if len(mov)>0:
            movfinanciero=movimientofinanciero.objects.get(movimiento_id=doc)
            movfinanciero.fecha=datos["fecha"]
            movfinanciero.fk_usuario = usuario.objects.get(usuario_id = datos["fk_usuario"])
            movfinanciero.fk_empresa=empresa.objects.get(nit_empresa = datos["fk_empresa"])
            movfinanciero.descripcion_movimiento=datos["descripcion_movimiento"]
            movfinanciero.tipo_movimiento=datos["tipo_movimiento"]
            movfinanciero.saldo=datos["saldo"]
            movfinanciero.save()
            mensaje={"Respuesta":"Datos actualizados"}
        else:
            mensaje={"Respuesta":"Datos no encontrados"}
        return JsonResponse(mensaje)
    
    def delete(self,request,doc):
            mov=list(movimientofinanciero.objects.filter(movimiento_id=doc).values())
            if len(mov)>0:
                movimientofinanciero.objects.filter(movimiento_id=doc).delete()
                mensaje={"Respuesta":"Registro eliminado"}
            else:   
                mensaje={"Respuesta":"Registro no encontrado"}
            return JsonResponse (mensaje) 

