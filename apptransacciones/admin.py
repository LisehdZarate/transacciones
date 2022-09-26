from django.contrib import admin
from apptransacciones.models import empresa, cargo, usuario, movimientofinanciero, empresaUsuario

admin.site.register(empresa)
admin.site.register(cargo)
admin.site.register(usuario)
admin.site.register(movimientofinanciero)
admin.site.register(empresaUsuario)
