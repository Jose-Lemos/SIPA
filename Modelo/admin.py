from django.contrib import admin

from .models import  Pais, Fuente_Informacion, Configuracion_Fuente_Informacion, Contenido_Original, Categoria, Contenido_Procesado, Adjunto

# Register your models here.
admin.site.register(Pais)
admin.site.register(Fuente_Informacion)
admin.site.register(Configuracion_Fuente_Informacion)
admin.site.register(Contenido_Procesado)
admin.site.register(Categoria)
admin.site.register(Adjunto)

@admin.register(Contenido_Original)
class ContOrigAdmin(admin.ModelAdmin):
    list_display = ("id", "idFuente")

