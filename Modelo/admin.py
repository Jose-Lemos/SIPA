from django.contrib import admin

from .models import Usuario, Pais, Fuente_Informacion, Configuracion_Fuente_Informacion, Contenido_Original

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Pais)
admin.site.register(Fuente_Informacion)
admin.site.register(Configuracion_Fuente_Informacion)
admin.site.register(Contenido_Original)

