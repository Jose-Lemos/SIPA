from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static
from .views import (Panel_Administracion_View, Pantalla_Principal_View, Visualizar_Contenido_View, Contenidos_Procesados,
UsuarioCreateView, agregar_categoria, agregar_fuente_info, agregar_pais, eliminar_Usuario, eliminar_categoria, eliminar_fuente_info, eliminar_pais,
listar_Categorias, listar_Fuente_informacion, listar_Paises, listar_Usuarios, Extraer_HTML, Panel_Contenidos_Originales,
modificar_Usuario, modificar_categoria, modificar_fuente_info, modificar_pais, logoutView, Panel_Contenidos_Proceasados, Panel_Adjuntos,
agregar_adjunto, modificar_adjunto, eliminar_adjunto, eliminar_contenido_original, eliminar_contenido_procesado, select_fuente_info, Extraer_HTML_Fuente, descargar_pdf, pruebaPDF)


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    #path de CRUD de usuarios
    
    path('usuarios/', listar_Usuarios.as_view(), name='usuarios'),
    path('agregar-usuario/', UsuarioCreateView.as_view(), name = "agregar-usuario"),
    path('modificar-usuario/<int:pk>', modificar_Usuario.as_view(), name = "modificar-usuario"),
    path('eliminar-usuario/<int:pk>', eliminar_Usuario.as_view(), name="eliminar-usuario"),

    #path de CRUD de Adjuntos
    path('adjuntos/', Panel_Adjuntos.as_view(), name="adjuntos"),    
    path('agregar-adjunto/', agregar_adjunto.as_view(), name="agregar-adjunto"),
    path('modificar-adjunto/<int:pk>', modificar_adjunto.as_view(), name = "modificar-adjunto"),
    path('eliminar-adjunto/<int:pk>', eliminar_adjunto.as_view(), name = "eliminar-adjunto"),


    #path de CRUD de categorias
    path('categorias/', listar_Categorias.as_view(), name= "categorias"),
    path('agregar-categoria/', agregar_categoria.as_view(), name = "agregar-categoria"),
    path('modificar-categoria/<int:pk>', modificar_categoria.as_view(), name = "modificar-categoria"),
    path('eliminar-categoria/<int:pk>', eliminar_categoria.as_view(), name="eliminar-categoria"),

    #path de CRUD de fuentes de informacion
    path('fuentes-informacion/', listar_Fuente_informacion.as_view(), name= "fuentes-informacion"),
    path('agregar-fuente-info/', agregar_fuente_info.as_view(), name = "agregar-fuente-info"),
    path('modificar-fuente-info/<int:pk>', modificar_fuente_info.as_view(), name = "modificar-fuente-info"),
    path('eliminar-fuente-info/<int:pk>', eliminar_fuente_info.as_view(), name="eliminar-fuente-info"),

    #path de CRUD de paises
    path('paises/', listar_Paises.as_view(), name = "paises"),
    path('agregar-pais/', agregar_pais.as_view(), name = "agregar-pais"),
    path('modificar-pais/<int:pk>', modificar_pais.as_view(), name = "modificar-pais"),
    path('eliminar-pais/<int:pk>', eliminar_pais.as_view(), name="eliminar-pais"),

    #path de CRUD de contenidos procesados
    path('contenidos-procesados/', Panel_Contenidos_Proceasados.as_view(), name="panel-contenidos-procesados"),
    path('eliminar-contenido-procesado/<int:pk>', eliminar_contenido_procesado.as_view(), name="eliminar-contenido-procesado"),

    #path de CRUD de contenidos originales
    path('contenidos-originales/', Panel_Contenidos_Originales.as_view(), name="panel-contenidos-originales"),
    path('eliminar-contenido-original/<int:pk>', eliminar_contenido_original.as_view(), name="eliminar-contenido-original"),



    #path de Navegacion
    path('admin/', Panel_Administracion_View.as_view(), name = "admin"),
    path('home/', Pantalla_Principal_View.as_view(), name = "home"),
    path('contenidos/', Contenidos_Procesados.as_view(), name="contenidos"),
    path('contenido/<int:pk>', Visualizar_Contenido_View.as_view(), name = 'contenido'),
    path('contenidoPDF/<int:pk>', descargar_pdf, name="descargar-pdf"),

    #path Recoleccion


    #path('configuracion-scrapper/', Configurar_Scrapper.as_view(), name="configurar-scrapper"),
    path('extraer-html/', Extraer_HTML.as_view(), name="extraer-html"),
    path('extraer-html/<int:pk>', Extraer_HTML_Fuente.as_view(), name="extraer-html-fuente"),
    path('seleccionar-fuente/', select_fuente_info.as_view(), name="seleccionar-fuente"),

    path('prueba/', pruebaPDF.as_view(), name="prueba")
]