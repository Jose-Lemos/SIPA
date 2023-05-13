# Módulos necesarios para la API

# Modulos necesarios para las vistas comunes
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView, DetailView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

# módulos necesarios para el WebScrapping
import urllib.request
from bs4 import BeautifulSoup
from django.contrib.auth.forms import AuthenticationForm

# Modelos necesarios para las vistas
from .models import Contenido_Procesado, Pais, Categoria, Fuente_Informacion, Contenido_Original, Adjunto
from .forms import RegistroForm, CategoriaForm, PaisForm, Fuente_Info_Form, Configuracion_Fuente_Info_Form, AdjuntoForm


# Create your views here.
import os
# Api de usuarios


def descargarImagen(url, fuente, nombre_fichero):
    #ruta_completa = ruta_fichero + nombre_fichero
    #urllib.request.urlretrieve(url, ruta_completa)
    path_imagenes = os.path.join(os.path.join(os.path.expanduser('~')), 'Pictures')
    path_base = os.path.join(path_imagenes, 'Images-Scrapp') 
    path_img_fuente = os.path.join(path_base, fuente)
    path_img_fuente_file = os.path.join(path_img_fuente, nombre_fichero)

    if(os.path.isdir(path_base)):
        print("el path base existe")
    else:
        os.mkdir(path_base)
        print("se creó el path base: "+path_base)


    if (os.path.isdir(path_img_fuente)):
        print("la carpeta para las imagenes de la fuente ya existe")
    else:
        os.mkdir(path_img_fuente)
        print("se creó la carpeta para las img de la fuente: "+path_img_fuente)


    if (os.path.isfile(path_img_fuente_file)):
        print("la imagen ya existe en la carpeta de la fuente!!")
    else:
        print("se creó la img en la carpeta de la fuente....")
        urllib.request.urlretrieve(url, path_img_fuente_file)
    
    return path_img_fuente_file

#descargarImagen("https://www.bas.ac.uk/wp-content/uploads/2015/03/cbox-00001510-400x250.jpg","BAS", "cbox-00001510-400x250.jpg")
class Articulo:
    def __init__(self, titulo, link_pagina, link_imagen):
        self.titulo = titulo
        self.pagina = link_pagina
        self.imagen = link_imagen

    def __str__(self):
        texto = "Titulo-Articulo: {0} - Link: {1} - Imagen: {2}"
        return texto.format(self.titulo, self.pagina, self.imagen)


# class UsuariosView(View):
#     @method_decorator(csrf_exempt)
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)

#     def get(self, request):

#         usuarios = list(User.objects.values())

#         if len(usuarios) > 0:
#             datos = {'message': 'Éxito', 'usuarios': usuarios}
#         else:
#             datos = {'message': 'No se encontraron Usuarios...'}

#         return JsonResponse(datos)

#     def post(self, request, nombreN, contraseñaN):
#         nuevoUsuario = {"nombre": nombreN, "contraseña": contraseñaN}
#         User.objects.create(
#             nombre=nuevoUsuario['nombreN'], contraseña=nuevoUsuario['contraseñaN'])
#         jd = json.loads(request.body)
#         datos = {'message': 'Éxito'}
#         return JsonResponse(datos)

#     def put(self, request):
#         pass

#     def delete(self, request):
#         pass


# Vistas de Usuarios
# class loginView(LoginView):
#     template_name = 'login.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context
    
#     def post(self, request, **kwargs):
#         name_user = request.POST.get('email-user')
#         pass_user = request.POST.get('pass-user')
#         print(name_user, pass_user)

#         user = authenticate(username=name_user, password=pass_user)
#         if user is not None:
#         # A backend authenticated the credentials
#             redirect('home')
#         else:
#             # No backend authenticated the credentials
#             redirect('login')



class logoutView(TemplateView):
    template_name = 'logout.html'


class listar_Usuarios(LoginRequiredMixin, TemplateView):
    queryset = User.objects.all()
    context_object_name = "Usuarios"
    template_name = 'ListadoUsuarios.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Usuarios'] = self.queryset
        context['mensaje'] = 'No existen Usuarios en la Base de Datos. Puedes agregar Usuarios con el botón "+ Agregar"'

        return context

    def get(self, request, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Usuarios'] = User.objects.all()
        context['mensaje'] = 'No existen Usuarios en la Base de Datos. Puedes agregar Usuarios con el botón "+ Agregar"'

        return self.render_to_response(context)

    def post(self, request, **kwargs):
        busqueda = request.POST.get("buscador")
        context = super().get_context_data(**kwargs)

        if request.method == "POST":
            print(busqueda)
            if busqueda:
                usuarios = User.objects.filter(
                    Q(username__icontains = busqueda)|Q(email__icontains = busqueda)
                )
                if usuarios.exists()==True:
                    context['Usuarios'] = usuarios
                else:
                    context['mensaje'] = 'No se enconrtraron Usuarios con el nombre o correo ingresado. Por favor ingresar otro nombre o correo para realizar la búsqueda'
            else:
                context['mensaje'] = 'Por favor ingrese un texto para realizar la búsqueda'
            return self.render_to_response(context)
        else:
            return self.render_to_response(context)


class UsuarioCreateView(LoginRequiredMixin, CreateView):
    model = User
    form_class = RegistroForm
    queryset = User.objects.all()
    template_name = "AgregarUsuario.html"
    success_url = reverse_lazy('usuarios')

    # def get_context_data(self, **kwargs):
    # context = super().get_context_data(**kwargs)

    # def post(self, request, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     email_user = request.POST["email"]
    #     pass_user = request.POST["password"]
    #     is_super = request.POST["is_superuser"]

    #     new_User = Usuario()
    #     new_User.email = email_user
    #     new_User.password = pass_user
    #     new_User.is_superuser = is_super
    #     new_User.save()

        # context = self.get_context_data(**kwargs)
        # return self.render_to_response(context)


class modificar_Usuario(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserChangeForm
    template_name = "ModificarUsuario.html"
    success_url = reverse_lazy('usuarios')


class eliminar_Usuario(LoginRequiredMixin, DeleteView):
    model = User
    template_name = "EliminarUsuario.html"
    success_url = reverse_lazy('usuarios')


#Vistas de los Adjuntos
class Panel_Adjuntos(LoginRequiredMixin, TemplateView):
    queryset = Adjunto.objects.all()
    context_object_name = "Adjuntos"
    template_name = "ListadoAdjuntos.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Adjuntos'] = self.queryset
        context['mensaje'] = 'No existen Adjuntos en la Base de Datos. Puedes agregar Adjuntos con el botón "+ Agregar"'

        return context

    def get(self, request, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Adjuntos'] = Adjunto.objects.all()
        context['mensaje'] = 'No existen Adjuntos en la Base de Datos. Puedes agregar Adjuntos con el botón "+ Agregar"'

        return self.render_to_response(context)

    def post(self, request, **kwargs):
        busqueda = request.POST.get("buscador")
        context = super().get_context_data(**kwargs)

        if request.method == "POST":
            print(busqueda)
            if busqueda:
                adjuntos = Adjunto.objects.filter(
                    Q(nombre__icontains = busqueda)
                )
                if adjuntos.exists()==True:
                    context['Adjuntos'] = adjuntos
                else:
                    context['mensaje'] = 'No se enconrtraron Adjuntos con el nombre ingresado. Por favor ingresar otro nombre para realizar la búsqueda'
            else:
                context['mensaje'] = 'Por favor ingrese un texto para realizar la búsqueda'
            return self.render_to_response(context)
        else:
            return self.render_to_response(context)


class agregar_adjunto(LoginRequiredMixin, CreateView):
    model = Adjunto
    form_class = AdjuntoForm
    queryset = Adjunto.objects.all()
    template_name = "AgregarAdjunto.html"
    success_url = reverse_lazy('adjuntos')


class modificar_adjunto(LoginRequiredMixin, UpdateView):
    model = Adjunto
    form_class = AdjuntoForm
    template_name = "ModificarAdjunto.html"
    success_url = reverse_lazy('adjuntos')

class eliminar_adjunto(DeleteView):
    model = Adjunto
    template_name = "EliminarAdjunto.html"
    success_url = reverse_lazy('adjuntos')


# Vistas de las categorías
class listar_Categorias(LoginRequiredMixin, TemplateView):
    queryset = Categoria.objects.all()
    context_object_name = "Categorias"
    template_name = 'ListadoCategorias.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Categorias'] = self.queryset
        context['mensaje'] = 'No existen Categorias en la Base de Datos. Puedes agregar Categorias con el botón "+ Agregar"'

        return context
    
    def get(self, request, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Categorias'] = Categoria.objects.all()
        context['mensaje'] = 'No existen Categorias en la Base de Datos. Puedes agregar Categorias con el botón "+ Agregar"'

        return self.render_to_response(context)


    def post(self, request, **kwargs):
        busqueda = request.POST.get("buscador")
        context = super().get_context_data(**kwargs)
        #categorias = Categoria.objects.all()

        if request.method == "POST":
            print(busqueda)
            if busqueda:
                categorias = Categoria.objects.filter(
                    Q(concepto__icontains = busqueda)
                )
                if categorias.exists()==True:
                    context['Categorias'] = categorias
                else:
                    context['mensaje'] = 'No se encontraron Categorias con el nombre ingresado. Por favor ingresar otro nombre para realizar la búsqueda'
            else:
                context['mensaje'] = 'Por favor ingrese un texto para realizar la búsqueda'
            return self.render_to_response(context)
        else:
            return self.render_to_response(context)


class agregar_categoria(LoginRequiredMixin, CreateView):
    model = Categoria
    form_class = CategoriaForm
    queryset = Categoria.objects.all()
    template_name = "AgregarCategoria.html"
    success_url = reverse_lazy('categorias')


class modificar_categoria(LoginRequiredMixin, UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = "ModificarCategoria.html"
    success_url = reverse_lazy('categorias')


class eliminar_categoria(LoginRequiredMixin, DeleteView):
    model = Categoria
    template_name = "EliminarCategoria.html"
    success_url = reverse_lazy('categorias')


# Vistas de las fuentes de información
class listar_Fuente_informacion(LoginRequiredMixin, TemplateView):
    queryset = Fuente_Informacion.objects.all()
    context_object_name = "Fuentes"
    template_name = 'ListadoFuentes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Fuentes'] = self.queryset
        context['mensaje'] = 'No existen Fuentes de Información en la Base de Datos. Puedes agregar Fuentes de Información con el botón "+ Agregar"'

        return context
    
    def get(self, request, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Fuentes'] = Fuente_Informacion.objects.all()
        context['mensaje'] = 'No existen Fuentes de Información en la Base de Datos. Puedes agregar Fuentes de Información con el botón "+ Agregar"'

        return self.render_to_response(context)

    def post(self, request, **kwargs):
        busqueda = request.POST.get("buscador")
        context = super().get_context_data(**kwargs)

        if request.method == "POST":
            print(busqueda)
            if busqueda:
                fuentes = Fuente_Informacion.objects.filter(
                    Q(nombre__icontains = busqueda)|Q(URL__icontains = busqueda)
                )
                if fuentes.exists()==True:
                    context['Fuentes'] = fuentes
                else:
                    context['mensaje'] = 'No se enconrtraron Fuentes de Información con el nombre ingresado. Por favor ingresar otro nombre'
            else:
                context['mensaje'] = 'Por favor ingrese un texto para realizar la búsqueda'
            return self.render_to_response(context)
        else:
            return self.render_to_response(context)


class agregar_fuente_info(LoginRequiredMixin, CreateView):
    model = Fuente_Informacion
    form_class = Fuente_Info_Form
    queryset = Fuente_Informacion.objects.all()
    template_name = "AgregarFuenteInformacion.html"
    success_url = reverse_lazy('fuentes-informacion')


class modificar_fuente_info(LoginRequiredMixin, UpdateView):
    model = Fuente_Informacion
    form_class = Fuente_Info_Form
    template_name = "ModificarFuenteInfo.html"
    success_url = reverse_lazy('fuentes-informacion')


class eliminar_fuente_info(LoginRequiredMixin, DeleteView):
    model = Fuente_Informacion
    template_name = "EliminarFuenteInfo.html"
    success_url = reverse_lazy('fuentes-informacion')



# Vistas de los paises
class listar_Paises(LoginRequiredMixin, TemplateView):
    queryset = Pais.objects.all()
    context_object_name = "Paises"
    template_name = 'ListadoPaises.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Paises'] = self.queryset
        context['mensaje'] = 'No existen Paises en la Base de Datos. Puedes agregar Paises con el botón "+ Agregar"'

        return context
    
    def get(self, request, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Paises'] = Pais.objects.all()
        context['mensaje'] = 'No existen Paises en la Base de Datos. Puedes agregar Paises con el botón "+ Agregar"'

        return self.render_to_response(context)

    def post(self, request, **kwargs):
        busqueda = request.POST.get("buscador")
        context = super().get_context_data(**kwargs)

        if request.method == "POST":
            print(busqueda)
            if busqueda:
                paises = Pais.objects.filter(
                    Q(nombre__icontains = busqueda)
                )
                if paises.exists()==True:
                    context['Paises'] = paises
                else:
                    context['mensaje'] = 'No se enconrtraron Países con el nombre ingresado. Por favor ingresar otro nombre'
            else:
                context['mensaje'] = 'Por favor ingrese un texto para realizar la búsqueda'
            return self.render_to_response(context)
        else:
            return self.render_to_response(context)



class agregar_pais(LoginRequiredMixin, CreateView):
    model = Pais
    form_class = PaisForm
    queryset = Pais.objects.all()
    template_name = "AgregarPais.html"
    success_url = reverse_lazy('paises')


class modificar_pais(LoginRequiredMixin, UpdateView):
    model = Pais
    form_class = PaisForm
    template_name = "ModificarPais.html"
    success_url = reverse_lazy('paises')


class eliminar_pais(LoginRequiredMixin, DeleteView):
    model = Pais
    template_name = "EliminarPais.html"
    success_url = reverse_lazy('paises')


# Vista del Panel Principal
class Panel_Administracion_View(LoginRequiredMixin,TemplateView):
    template_name = 'PanelAdmin.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# Vista de Pantalla Principal
class Pantalla_Principal_View(LoginRequiredMixin,TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cont_procesado = Contenido_Procesado.objects.all()
        fechas_cont = []

        for cont in cont_procesado:
            if not(cont.fecha_Creacion in fechas_cont):
                fechas_cont.append(cont.fecha_Creacion)

        context["Contenidos"] = cont_procesado
        context["Categorias"] = Categoria.objects.all()
        context["Fuentes"] = Fuente_Informacion.objects.all()
        context["Paises"] = Pais.objects.all()
        context["Fechas"] = fechas_cont
        return context


# Vistas de los contenidos
class Visualizar_Contenido_View(LoginRequiredMixin, TemplateView):
    template_name = 'VisualizarContenido.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class Extraer_HTML(LoginRequiredMixin, TemplateView):
    template_name = "ExtraerHTML.html"
    fuentes = Fuente_Informacion.objects.all()
    form = Contenido_Original

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fuentes'] = self.fuentes
        context['form'] = self.form
        context["html"] = ""
        return context

        

    def post(self, request, **kwargs):
        id_fuente = request.POST.get('fuente-id')
        fuente = Fuente_Informacion.objects.get(id=id_fuente)
        tag_title = request.POST.get("etiqueta-title1")
        tag_contenedor = request.POST.get("etiqueta-seccion1")

        if request.method == "POST":
            context = super().get_context_data(**kwargs)

            #if(context["html"] != ""):
             #   return redirect("contenidos")

            print("id_fuente: ", id_fuente)
            print("fuente: ", fuente)
            print("tag_title: ", tag_title)
            print("tag_contenedor: ", tag_contenedor)

            url = fuente.URL
            # Este parámetro define la URL de donde se van a obtener los elementos
            page = urllib.request.urlopen(url).read().decode()
            soup = BeautifulSoup(page, 'html.parser')

            context['fuentes'] = self.fuentes
            context['form'] = self.form
            context["html"] = ""
            context["id_fuente"] = id_fuente
            context["page"] = soup

            print(fuente)

            articles = []

            for sec in soup.find_all(tag_contenedor):
                title_art = ""
                h2 = sec.find_all(tag_title)
                links = sec.find_all('a')
                imgs = sec.find_all('img')

                titles = []
                for h in h2:
                    padre_title = h.parent
                    if padre_title.get("class") == sec.get("class"):
                        # print(sec.get('class'))
                        title_art = h.string
                        titles.append(title_art)
                    # if h2 is not None:

                        # print(h2.string)

                    # h4 = sec.find('h4')
                    # if h4 is not None:
                    #    print(h4.string)

                links_sections = []
                for link in links:
                    padre_lnk = link.parent
                    if padre_lnk.get('class') == sec.get('class'):
                        if not (link.get("href") in links_sections):
                            links_sections.append(link.get("href"))
                        # print("link: ",link.get('href'))

                imgs_sections = []
                for img in imgs:
                    padre_img = img.parent
                    link_img = padre_img.get("href")
                    if padre_img.get('class') == sec.get('class'):
                        imgs_sections.append(img.get("src"))
                        # print("imagen: ",img.get('src'))
                    else:
                        if link_img is not None:
                            if link_img in links_sections:
                                imgs_sections.append(
                                    img.get("src"))

                if not ((len(links_sections) == 0) or (len(imgs_sections) == 0) or (title_art == None)):
                    new_art = Articulo(
                        title_art, links_sections[0], imgs_sections[0])
                    if not (new_art.titulo == ""):
                        context["html"] += "{"+title_art+"|"  #| utilizado para separar las claves
                        context["html"] += links_sections[0]+"|"  #| utilizado para separar las claves
                        context["html"] += imgs_sections[0]+"};"
                        articles.append(new_art)
                    # print(new_art)
                elif (len(links_sections) == 0):
                    if (len(imgs_sections) > 0):
                        new_art = Articulo(
                            title_art, "vacio", imgs_sections[0])
                        if not (new_art.titulo == ""):
                            articles.append(new_art)
                elif (len(imgs_sections) == 0):
                    if (len(links_sections) > 0):
                        new_art = Articulo(
                            title_art, links_sections[0], "vacio")
                        if not (new_art.titulo == ""):
                            articles.append(new_art)
                else:
                    print("solo titulo: ", title_art)
                    if title_art != "":
                        print("solo titulo: ", title_art)

            for art in articles:
                print(art)

            return self.render_to_response(context)


class Contenidos_Procesados(LoginRequiredMixin, TemplateView):
    template_name = "ContenidosExtraidos.html"
    contenidos_originales = Contenido_Original.objects.all()
    contenidos_procesados = Contenido_Procesado.objects.all()
    links = Fuente_Informacion.objects.all()
    categorias = Categoria.objects.all()
    imagenes = Adjunto.objects.all()
    context_object_name = "contenidos"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['form'] = self.queryset
        return context

    def post(self, request, **kwargs):
        context = super().get_context_data(**kwargs)
        html = request.POST.get("data-html")
        fuente = request.POST.get("font")
        page = request.POST.get("page-html")
        string_html = str(html)
        string_html = string_html.rsplit(";")

        self.contenidos_originales = Contenido_Original.objects.all()
        self.contenidos_procesados = Contenido_Procesado.objects.all()
        self.links = Fuente_Informacion.objects.all()
        self.categorias = Categoria.objects.all()
        self.imagenes = Adjunto.objects.all()

        articulos = []

        #print(string_html)
        print("page: "+page)
        print("list html:")
        for elem in string_html:
            elem = elem.replace("{", "")
            elem = elem.replace("}", "")
            elem = elem.rsplit("|")
            if(elem[0] != ""):
                articulos.append(elem)
                #print("lista con los atributos:")
                #print(elem)

        print("cont_original, fuentes, categorias e imagenes Antes del Scrapping:")
        #print(self.contenidos_originales)
        print(self.contenidos_procesados)
        print(self.links)
        print(self.categorias)
        print(self.imagenes)
        print(fuente)

        contenidos_html = []
        ids_fuentes = []
        for orig in self.contenidos_originales:
            if not(orig.contenido in contenidos_html):
                contenidos_html.append(orig.contenido)
            if not(orig.idFuente in ids_fuentes):
                ids_fuentes.append(orig.idFuente)

        categorias_concepto = []
        for cat in self.categorias:
            categorias_concepto.append(cat.concepto)

        links_url = []
        for lnk in self.links:
            links_url.append(lnk.URL)
        
        imagenes_url = []
        for img in self.imagenes:
            imagenes_url.append(img.imagen)

        contenidos_proc_tit = []
        for proc in self.contenidos_procesados:
            contenidos_proc_tit.append(proc.titulo)

        fuentePerteneciente = Fuente_Informacion.objects.get(id = fuente)
        if (fuentePerteneciente in ids_fuentes):
            #if()
            print("fuente: "+fuente)
            print("fuente perteneciente:"+fuentePerteneciente.URL)
            print(ids_fuentes)
            print("El contenido original ya existe y es exactamente igual que antes")
            newContOriginal = Contenido_Original.objects.get(idFuente = fuentePerteneciente)
        else:
            print("NOPE")
            print("fuente: "+fuente)
            print(ids_fuentes)
            newContOriginal = Contenido_Original(contenido = page, idFuente = fuentePerteneciente)
            newContOriginal.save()

        print("listas: ")
        for arti in articulos:
            print(arti)

            
            if (arti[0] in categorias_concepto):  #Consulto si el titulo ya existe en la tabla de Categorias
                print("La CATEGORIA "+ arti[0] +" Ya eexiste en la BD!!")
                newCategoria = Categoria.objects.get(concepto = arti[0])
            else:
                print("CAT NOT")
                newCategoria = Categoria(concepto = arti[0])
                newCategoria.save()

            
            if (arti[1] in links_url):  #Consulto si la url ya existe en la tabla de FuenteInfo
                print("La fuente de INFO"+ arti[1] +"Ya eexiste")
                newFuente = Fuente_Informacion.objects.get(URL = arti[1])
            else:
                print("NOPE")
                name_link = str(arti[1])
                name_link = name_link.rsplit("/")
                if (len(name_link) > 1):
                    name_ext = name_link[len(name_link)-2]
                else:
                    name_ext = arti[1]
                fuentePadre = Fuente_Informacion.objects.get(id=fuente)
                nameP = fuentePadre.nombre +"-"+ name_ext
                typeP = fuentePadre.tipo
                levelP = fuentePadre.nivel + 1
                paisP = fuentePadre.idPais
                newFuente = Fuente_Informacion(nombre = nameP, URL = arti[1], tipo = typeP, nivel = levelP, idPais = paisP, idPadre = fuente)
                newFuente.save()


            if (arti[2] in imagenes_url):  #Consulto si la imagen ya existe en la tabla de Adjuntos
                print("La IMAGEN"+ arti[2] +"Ya eexiste en la BD!!")
                newImage = Adjunto.objects.get(imagen = arti[2])
            else:
                print("IMG NOT")
                name_img = str(arti[2])
                name_img = name_img.rsplit("/")
                if (len(name_img) > 0):
                    name_ext = name_img[len(name_img)-1]
                else:
                    name_ext = arti[2]
                
                concep = str(newCategoria.concepto)
                concep = concep.replace(" ","-")
                name_ext = concep + "-" + name_ext
                print("name_ext: " + name_ext)
                
                #img_des = descargarImagen(arti[2], fuentePerteneciente.nombre, name_ext)
                newImage = Adjunto(nombre = name_ext, imagen = arti[2], URL = arti[2])
                newImage.save()

            #existeCP = False  #realizar una mejor validacion para los contenidos procesados creados
            #for content in self.contenidos_procesados:
             #   if ((content.idCategoria == newCategoria.id) and (content.idContenido_Original == newContOriginal.id) and (content.idAdjunto == newImage.id) and (content.titulo == newCategoria.concepto)):
              #      existeCP = True
                
            if newCategoria.concepto in contenidos_proc_tit:
                print("el Contenido Procesado ya Existe en la BD!!!")
            else:
                newContenidoProcesado = Contenido_Procesado(titulo = newCategoria.concepto, idContenido_Original = newContOriginal, idCategoria = newCategoria, idAdjunto = newImage)
                newContenidoProcesado.save()
                
            

        #print(string_html)
        #context['form'] = self.queryset
        return self.render_to_response(context)


#CRUD de los contenidos procesados
class Panel_Contenidos_Proceasados(LoginRequiredMixin, ListView):
    queryset = Contenido_Procesado.objects.all()
    context_object_name = "Contenidos"
    template_name = 'ListadoContenidoProcesado.html'

class eliminar_contenido_procesado(LoginRequiredMixin, DeleteView):
    model = Contenido_Procesado
    template_name = "EliminarContenidoProcesado.html"
    success_url = reverse_lazy('panel-contenidos-procesados')

#CRUD de los contenidos originales
class Panel_Contenidos_Originales(LoginRequiredMixin, ListView):
    queryset = Contenido_Original.objects.all()
    context_object_name = "Contenidos"
    template_name = 'ListadoContenidoOriginal.html'

class eliminar_contenido_original(LoginRequiredMixin, DeleteView):
    model = Contenido_Original
    template_name = "EliminarContenidoOriginal.html"
    success_url = reverse_lazy('panel-contenidos-originales')


