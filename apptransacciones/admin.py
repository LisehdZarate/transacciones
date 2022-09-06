from django.contrib import admin
from apptransacciones.models import empresa, rol, usuario, movimientofinanciero
admin.site.register(empresa)
admin.site.register(rol)
admin.site.register(usuario)
admin.site.register(movimientofinanciero)
