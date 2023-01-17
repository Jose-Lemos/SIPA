from django.contrib import admin

from .models import Usuario, Pais, Fuente_Informacion, Configuracion_Fuente_Informacion, Contenido_Original, Categoria, Contenido_Procesado, Adjunto

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Pais)
admin.site.register(Fuente_Informacion)
admin.site.register(Configuracion_Fuente_Informacion)
admin.site.register(Contenido_Original)
admin.site.register(Contenido_Procesado)
admin.site.register(Categoria)
admin.site.register(Adjunto)

