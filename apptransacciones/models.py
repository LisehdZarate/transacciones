from pyexpat import model
from django.db import models

class empresa(models.Model):
    nit_empresa=models.IntegerField(primary_key=True)
    nombre_Empresa=models.CharField(max_length=30)
    ciudad_Empresa=models.CharField(max_length=30)
    direccion_Empresa=models.CharField(max_length=50)
    def __str__(self):
        return self.nitempresa,self.nombreEmpresa,self.ciudadEmpresa,self.direccionEmpresa

class rol(models.Model):
    rol_id=models.IntegerField(primary_key=True)
    estado=models.CharField(max_length=10)
    rol=models.CharField(max_length=10)
    def __str__(self):
        return self.rol_id,self.estado,self.rol

class usuario(models.Model):
    usuario_id=models.IntegerField(primary_key=True)
    nombre_Usu=models.CharField(max_length=50)
    apellido_Usu=models.CharField(max_length=50)
    correoUsu=models.CharField(max_length=60) 
    login=models.CharField(max_length=50)
    password_Usu=models.CharField(max_length=50)
    fk_rol=models.ForeignKey(rol, on_delete=models.CASCADE)
    def __str__(self):
        return self.usuario_id,self.nombre_Usu,self.apellido_Usu,self.correoUsu,self.login,self.password_Usu,self.fk_rol

class movimientofinanciero(models.Model):
    movimiento_id=models.IntegerField(primary_key=True)
    fecha=models.DateField()
    fk_usuario=models.ForeignKey(usuario, on_delete=models.CASCADE)
    fk_empresa=models.ForeignKey(empresa, on_delete=models.CASCADE)
    descripcion_movimiento=models.CharField(max_length=150)
    tipo_movimiento=models.CharField(max_length=60)
    saldo=models.IntegerField(20)
    def __str__(self):
        return self.movimiento_id,self.fecha,self.fk_usuario,self.fk_empresa,self.descripcion_movimiento,self.tipo_movimiento,self.saldo

