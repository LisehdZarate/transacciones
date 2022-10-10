from calendar import c
from http.client import HTTPResponse
import imp
import json
from email import message
from re import template
from django.contrib import messages
from django.shortcuts import render
from django.views import View
from .models import empresa, movimientofinanciero, cargo, usuario, empresaUsuario
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.shortcuts import redirect


class empresaVista(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request,*args, **kwargs)

    
    
    def get(self, request, empId=0): 
        if empId>0:
            empresas=list(empresa.objects.filter(nit_empresa=empId).values())
            print(empresas)
            if len(empresas)>0:
                getEmp=empresas[0]
                template_name='actualizaremp.html'
                datos={'empresa': getEmp}
                return render(request,template_name,datos)
            else:    
             datos={"respuesta":"Dato no se encontro"}
             print("ENCONTRADO")
             return render(request,template_name,datos)     
        else:
           template_name='consultarempresa.html'
           emp=empresa.objects.all()
           datos={'listadoEmpresa': emp}
           return render(request,template_name,datos)

    def post (self, request):
        datos=(request.POST)
        empresa.objects.create(
            nit_empresa=datos["nit_empresa"],
            nombre_Empresa=datos["nombre_Empresa"], 
            ciudad_Empresa=datos["ciudad_Empresa"],
            direccion_Empresa=datos["direccion_Empresa"])
        return redirect('/empresa/')

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
   
     
    def get(self, request, usuId=0):
        if usuId>0:
            usuario1=list(usuario.objects.filter(usuarioId=usuId).values())
            print(usuario1)
            if len(usuario1)>0:
                getUsu=usuario1[0]
                template_name='actualizarusu.html'
                datos={'usuario': getUsu}
                return render(request,template_name,datos)
            else:
             datos={"respuesta":"Dato no se encontro"}
             print("ENCONTRADO")
             return render(request,template_name,datos)     
        else:
          template_name='consultarusuario.html'
          usu=usuario.objects.all()
          datos={'listadoUsuario': usu}
          return render(request,template_name,datos)


    def post (self, request):
        datos=(request.POST)
        cargos=cargo.objects.get(cargoId = datos["Cargo"])
        
        usuario.objects.create(
            usuarioId=datos["usuarioId"]
            , nombre_Usu=datos["nombre_Usu"]
            , apellido_Usu=datos["apellido_Usu"]
            , correoUsu=datos["correoUsu"]
            , login=datos["login"]
            , password_Usu=datos["password_Usu"]
            , cargoId=cargos)
        return redirect('/usuario/')
      

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
  


class login(View):
    def loginusuario(request):
        if request.method=='POST':
            try:
                detalleusuario=usuario.objects.get(login=request.POST['login'],password_Usu=request.POST['password_Usu'])                 
                cargos=cargo.objects.get(cargoId=detalleusuario.cargoId_id)
                

                if cargos.isAdministrator=="1":
                    request.session['login']=detalleusuario.login
                    request.session['usuarioId']=detalleusuario.usuarioId
                    return render(request,'gestionc.html')
                elif cargos.isAdministrator=="0":
                    request.session['login']=detalleusuario.login
                    return render(request,'empleado.html')
            except usuario.DoesNotExist as e:
                messages.success(request,('No existe el dato'))
        return render(request,'login.html')
    
    def formularioregistro(request):
        return render(request,'registromovimiento.html')

    def formularioactualizar(request,movimientoId):
        mov=movimientofinanciero.objects.get(movimientoId=movimientoId)
        datos={
            'movimientofinanciero':mov
        }
        return render(request,'actualizarmov.html',datos)
    
    def actualizar(request):
        movid=request.POST["movimientoId"]
        fch=request.POST["fecha"]
        usu=usuario.objects.get(usuarioId = request.POST["usuarioId"])
        emp=empresa.objects.get(nit_empresa = request.POST["nit_empresa"])
        des=request.POST["descripcion_movimiento"]
        tip=request.POST["tipo_movimiento"]
        sal=request.POST["saldo"]
        mov=movimientofinanciero.objects.get(movimientoId=movid)
        mov.fecha=fch
        mov.usuarioId=usu
        mov.nit_empresa=emp
        mov.descripcion_movimiento=des
        mov.tipo_movimiento=tip
        mov.saldo=sal
        mov.save()
        return redirect("movimientofinanciero")


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
   
    def get(self, request, movId=0):
        if movId>0:
            movimiento=list(movimientofinanciero.objects.filter(movimientoId=movId).values())
            print(movimiento)
            if len(movimiento)>0:
                getMovimiento=movimiento[0]
                template_name='actualizarmov.html'
                datos={'movimientofinanciero': getMovimiento}
                return render(request,template_name,datos)
            else:
             datos={"respuesta":"Dato no se encontro"}
             print("ENCONTRADO")
             return render(request,template_name,datos)     
        else:
          template_name='consultarmovimiento.html'
          mov=movimientofinanciero.objects.all()
          datos={'listadoMovimiento': mov}
          return render(request,template_name,datos)

   



    def post (self, request):
        datos=(request.POST)
        
        usu=usuario.objects.get(usuarioId = datos["usuarioId"])
        emp=empresa.objects.get(nit_empresa = datos["nit_empresa"])
        movimientofinanciero.objects.create(
            movimientoId=datos["movimientoId1"]
            ,fecha=datos["fecha1"]
            ,usuarioId=usu
            ,nit_empresa=emp
            ,descripcion_movimiento=datos["descripcion_movimiento1"]
            ,tipo_movimiento=datos["tipo_movimiento1"]
            ,saldo=datos["saldo1"])
        return redirect('/movimientofinanciero/')


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

def editarmovimiento(request):
   if request.method=='POST':
      movid=request.POST['movimientoId1']
      fecha =request.POST['fecha1']
      usu=request.POST['usuarioId1']
      nit=request.POST['nit_empresa1']
      des=request.POST['descripcion_movimiento1']
      tip=request.POST['tipo_movimiento1']
      sal=request.POST['saldo1']
      #print(nom)
      mov=movimientofinanciero.objects.get(movimientoId=movid)
      usuario1=usuario.objects.get(usuarioId=usu)
      emp=empresa.objects.get(nit_empresa=nit)
      

      mov.fecha=fecha
      mov.usuarioId=usuario1
      mov.nit_empresa=emp
      mov.descripcion_movimiento=des
      mov.tipo_movimiento=tip
      mov.saldo=sal
      mov.save()
      return redirect('/movimientofinanciero/')

def editarusuario(request):
        if request.method=='POST':
            usuid=request.POST['usuarioId']
            nom =request.POST['nombre_Usu']
            ape =request.POST['apellido_Usu']
            cor=request.POST['correoUsu']
            log=request.POST['login']
            pas=request.POST['password_Usu']
            car=request.POST['cargoId']
            #print(nom)
            usu=usuario.objects.get(usuarioId=usuid)
            cargoId1=cargo.objects.get(cargoId=car)  

            usu.nombre_Usu=nom
            usu.apellido_Usu=ape
            usu.correoUsu=cor
            usu.login=log
            usu.password_Usu=pas
            usu.cargoId=cargoId1
            usu.save()
            return redirect('/usuario/')

def editarempresa(request):
   if request.method=='POST':
      empid=request.POST['nit_empresa']
      nombre_Empresa=request.POST['nombre_Empresa']
      ciudad_Empresa=request.POST['ciudad_Empresa']
      direccion_Empresa=request.POST['direccion_Empresa']
      emp=empresa.objects.get(nit_empresa=empid)
    
      emp.nombre_Empresa=nombre_Empresa
      emp.ciudad_Empresa=ciudad_Empresa
      emp.direccion_Empresa=direccion_Empresa
      emp.save()
      return redirect('/empresa/')

def gestionusuario(request):
           return render(request,"actualizarusu.html")

def formulariousu(request):
        allCargo=usuario.objects.all()
        datos={'listadocargo': allCargo}
        return render(request,"registrousuario.html",datos)

def formularioemp(request):
        allempresa=empresa.objects.all()
        datos={'listadoEmp': allempresa}
        return render(request,"registroEmpresa.html",datos)

def gestionusuario(request):
   return render(request,"gestionc.html")

def frminsertar(request):
    allCargo=usuario.objects.all()
    print("Hola Thor: ",allCargo)
    datos={'listadocargo': allCargo}
    return render(request,"registrousuario.html",datos)   

          
def eliminarMov(request,movId):
    movimiento=list(movimientofinanciero.objects.filter(movimientoId=movId).values())
    movimientofinanciero.objects.filter(movimientoId=movId).delete()
    return redirect('/movimientofinanciero/')

def eliminarUsu(request,usuId):
    usuarios=list(usuario.objects.filter(usuarioId=usuId).values())
    usuario.objects.filter(usuarioId=usuId).delete()
    return redirect('/usuario/')         

def eliminarEmp(request,empId):
    #empresas=list(empresa.objects.filter(nit_empresa=empId).values())
    empresa.objects.filter(nit_empresa=empId).delete()
    return redirect('/empresa/')     