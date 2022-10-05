from pyexpat import model
from re import template
from django.db import models
from .choices import tipoRol, tipo_movimiento
from django.contrib.auth.models import User

class empresa(models.Model):
    nit_empresa=models.IntegerField(primary_key=True)
    nombre_Empresa=models.CharField(max_length=30)
    ciudad_Empresa=models.CharField(max_length=30)
    direccion_Empresa=models.CharField(max_length=255)
    def __str__(self):
        template = '{0.nit_empresa} {0.nombre_Empresa} {0.ciudad_Empresa} {0.direccion_Empresa}'
        return template.format(self)


class cargo(models.Model):
    cargoId=models.IntegerField(primary_key=True)
    descripcionCargo=models.CharField(max_length=255)
    isAdministrator=models.CharField(max_length=15,choices=tipoRol, default='0')
    def __str__(self):
        template = '{0.cargoId} {0.descripcionCargo} {0.isAdministrator}' 
        return template.format(self)  

class usuario(models.Model):
    usuarioId=models.IntegerField(primary_key=True)
    nombre_Usu=models.CharField(max_length=50)
    apellido_Usu=models.CharField(max_length=50)
    correoUsu=models.CharField(max_length=60) 
    login=models.CharField(max_length=50)
    password_Usu=models.CharField(max_length=50)
    cargoId=models.ForeignKey(cargo, on_delete=models.DO_NOTHING)
    def __str__(self):
        template = '{0.usuarioId} {0.nombre_Usu} {0.apellido_Usu} {0.correoUsu} {0.login} {0.password_Usu} {0.cargoId} '
        return template.format(self) 

class empresaUsuario(models.Model):
    empresaUsuarioId = models.AutoField(primary_key=True)
    usuarioId=models.ForeignKey(usuario, on_delete=models.DO_NOTHING)
    nit_empresa=models.ForeignKey(empresa, on_delete=models.DO_NOTHING)
    def __str__(self):
        template ='{0.empresaUsuarioId} {0.usuarioId} {0.nit_empresa}'
        return template.format(self)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['usuarioId', 'nit_empresa'], name='uniqueUser_Emp')
        ]

class movimientofinanciero(models.Model):
    movimientoId=models.IntegerField(primary_key=True)
    fecha=models.DateField()
    usuarioId=models.ForeignKey(usuario, on_delete=models.DO_NOTHING)
    nit_empresa=models.ForeignKey(empresa, on_delete=models.DO_NOTHING)
    tipo_movimiento=models.CharField(max_length=60,choices=tipo_movimiento, default='Ingreso')
    descripcion_movimiento=models.CharField(max_length=150)
    saldo=models.IntegerField()
    def __str__(self):
        template= '{0.movimientoId} {0.fecha} {0.usuarioId} {0.nit_empresa} {0.tipo_movimiento} {0.descripcion_movimiento} {0.saldo}'
        return template.format(self)

