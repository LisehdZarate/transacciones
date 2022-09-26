from calendar import c
from http.client import HTTPResponse
import imp
import json
from email import message
from django.shortcuts import render
from django.views import View
from .models import empresa, movimientofinanciero, cargo, usuario, empresaUsuario
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User



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




class  cargoVista(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request,*args, **kwargs)
   
    def get(self, request): 
        cargo1=list(cargo.objects.values())
        datos={'listadocargo': cargo1}
        return JsonResponse (datos)

    def post (self, request):
        datos=json.loads(request.body)
        cargo.objects.create(cargoId=datos["cargoId"], descripcionCargo=datos["descripcionCargo"])
        return JsonResponse(datos)

    def put(self,request,doc):
      datos=json.loads(request.body)
      cargo1=list(cargo.objects.filter(cargoId=doc).values())
      if len(cargo1)>0:
         cargos=cargo.objects.get(cargoId=doc)
         cargos.estado=datos["estado"]
         cargos.cargo=datos["cargo"]
         cargos.save()
         mensaje={"Respuesta":"Datos actualizados"}
      else:
         mensaje={"Respuesta":"Datos no encontrados"}
      return JsonResponse(mensaje)
 

    def delete(self,request,doc):
        cargo1=list(cargo.objects.filter(cargoId=doc).values())
        if len(cargo1)>0:
               cargo.objects.filter(cargoId=doc).delete()
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
        cargos=cargo.objects.get(cargoId = datos["cargoId"])
        usuario.objects.create(usuarioId=datos["usuarioId"]
           , nombre_Usu=datos["nombre_Usu"]
           , apellido_Usu=datos["apellido_Usu"]
           , correoUsu=datos["correoUsu"]
           , login=datos["login"]
           , password_Usu=datos["password_Usu"]
           , cargoId=cargos)
        return JsonResponse(datos)
      

    def put(self,request,doc):
      datos=json.loads(request.body)
      usu=list(usuario.objects.filter(usuarioId=doc).values())
      if len(usu)>0: 
         usuario1=usuario.objects.get(usuarioId=doc)
         usuario1.nombre_Usu=datos["nombre_Usu"]
         usuario1.apellido_Usu=datos["apellido_Usu"]
         usuario1.correoUsu=datos["correoUsu"]
         usuario1.login=datos["login"]
         usuario1.password_Usu=datos["password_Usu"]
         usuario1.fk_cargo=cargo.objects.get(cargoId = datos["cargoId"])
         usuario1.save()
         mensaje={"Respuesta":"Datos actualizados"}
      else:
         mensaje={"Respuesta":"Datos no encontrados"}
      return JsonResponse(mensaje)
 
    def delete(self,request,doc):
        usu=list(usuario.objects.filter(usuarioId=doc).values())
        if len(usu)>0:
               usuario.objects.filter(usuarioId=doc).delete()
               mensaje={"Respuesta":"Registro eliminado"}
        else:   
               mensaje={"Respuesta":"Registro no encontrado"}
        return JsonResponse (mensaje) 


class empresaUsuarioVista(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request,*args, **kwargs)
   
    def get(self, request): 
        empUsu=list(empresaUsuario.objects.values())
        datos={'listadoEmpUsuario': empUsu}
        return JsonResponse (datos)

    def post (self, request):
        datos=json.loads(request.body)
        empUsu1=usuario.objects.get(usuarioId = datos["usuarioId"])
        empUsu2=empresa.objects.get(nit_empresa = datos["nit_empresa"])
        empresaUsuario.objects.create(empresaUsuarioId=datos["empresaUsuarioId"]
            , usuarioId=empUsu1, nit_empresa=empUsu2)
        return JsonResponse(datos)

    def put(self,request, doc):
      datos=json.loads(request.body)
      empUsu=list(empresaUsuario.objects.filter(usuarioId=doc).values())
      if len(empUsu)>0: 
         empUsu1=empresaUsuario.objects.get(empresaUsuarioId=doc)
         empUsu1.usuarioId=usuario.objects.get(usuarioId = datos["usuarioId"])
         empUsu1.nit_empresa=empresa.objects.get(nit_empresa = datos["nit_empresa"])
         empUsu1.save()
         mensaje={"Respuesta":"Datos actualizados"}
      else:
         mensaje={"Respuesta":"Datos no encontrados"}
      return JsonResponse(mensaje)
 
    
    def delete(self,request,doc):
        empUsu=list(empresaUsuario.objects.filter(empresaUsuarioId=doc).values())
        if len(empUsu)>0:
               empresaUsuario.objects.filter(empresaUsuarioId=doc).delete()
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
        usu=usuario.objects.get(usuarioId = datos["cargoId"])
        emp=empresa.objects.get(nit_empresa = datos["nit_empresa"])
        movimientofinanciero.objects.create(
            movimientoId=datos["movimientoId"]
            ,fecha=datos["fecha"]
            ,cargoId=usu
            ,nit_empresa=emp
            ,descripcion_movimiento=datos["descripcion_movimiento"]
            ,tipo_movimiento=datos["tipo_movimiento"]
            ,saldo=datos["saldo"])
        return JsonResponse(datos)

    def put(self,request,doc):
        datos=json.loads(request.body)
        mov=list(movimientofinanciero.objects.filter(movimientoId=doc).values())
        searchUser = list(usuario.objects.filter(usuarioId = datos["fk_usuario"]).values())
        if len(searchUser)==0:
            mensaje={"Respuesta":"Usuario no encontrado"}
            return JsonResponse(mensaje)

        searchUser = list(empresa.objects.filter(nit_empresa = datos["fk_empresa"]).values())
        if len(searchUser)==0:
            mensaje={"Respuesta":"Empresa no encontrada"}
            return JsonResponse(mensaje)


        if len(mov)>0:
            movfinanciero=movimientofinanciero.objects.get(movimientoId=doc)
            movfinanciero.fecha=datos["fecha"]
            movfinanciero.fk_usuario = usuario.objects.get(usuarioId = datos["fk_usuario"])
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
            mov=list(movimientofinanciero.objects.filter(movimientoId=doc).values())
            if len(mov)>0:
                movimientofinanciero.objects.filter(movimientoId=doc).delete()
                mensaje={"Respuesta":"Registro eliminado"}
            else:   
                mensaje={"Respuesta":"Registro no encontrado"}
            return JsonResponse (mensaje) 

