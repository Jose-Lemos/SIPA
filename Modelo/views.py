#Módulos necesarios para la API
from email import message
import json
from re import template
from django.forms import ValidationError
from django.http.response import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

#Modulos necesarios para las vistas comunes
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView, DetailView
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy


#Modelos necesarios para las vistas
from .models import Pais, Usuario, Categoria, Fuente_Informacion
from .forms import UsuarioForm,CategoriaForm, PaisForm, Fuente_Info_Form
# Create your views here.

#Api de usuarios
class UsuariosView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs) :
        return super().dispatch(request, *args, **kwargs)   


    def get(self, request):
        
        usuarios = list(Usuario.objects.values())

        if len(usuarios)>0:
            datos = {'message': 'Éxito', 'usuarios': usuarios}
        else:
            datos = {'message': 'No se encontraron Usuarios...'}

        return JsonResponse(datos)

    def post(self, request, nombreN, contraseñaN):
        nuevoUsuario = {"nombre": nombreN, "contraseña": contraseñaN}
        Usuario.objects.create(nombre = nuevoUsuario['nombreN'], contraseña = nuevoUsuario['contraseñaN'])
        jd = json.loads(request.body)
        datos = {'message': 'Éxito'}
        return JsonResponse(datos)


    def put(self, request):
        pass

    def delete(self, request):
        pass


#Vistas de Usuarios
class loginView(TemplateView):
    template_name = 'login.html'

class logoutView(TemplateView):
    template_name = 'logout.html'

class listar_Usuarios(ListView):
    queryset = Usuario.objects.all()
    context_object_name = "Usuarios"
    template_name = 'Listado usuarios.html'

class UsuarioCreateView(CreateView):
    model = Usuario
    form_class = UsuarioForm
    queryset = Usuario.objects.all()
    template_name = "Agregar usuario.html"
    success_url = reverse_lazy('Usuarios')

    #def get_context_data(self, **kwargs):
        #context = super().get_context_data(**kwargs)

    def post(self, request, **kwargs):
        context = super().get_context_data(**kwargs)
        email_user = request.POST["email"]
        pass_user = request.POST["password"]
        is_super = request.POST["is_superuser"]

        new_User = Usuario()
        new_User.email = email_user
        new_User.password = pass_user
        new_User.is_superuser = is_super
        new_User.save()

        #context = self.get_context_data(**kwargs)
        #return self.render_to_response(context)
       

          

class modificar_Usuario(UpdateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = "Agregar usuario.html"
    success_url = reverse_lazy('Usuarios')

class eliminar_Usuario(DeleteView):
    model = Usuario
    template_name = "usuario_confirm_delete.html"
    success_url = reverse_lazy('Usuarios')

#Vistas de las categorías
class listar_Categorias(ListView):
    queryset = Categoria.objects.all()
    context_object_name = "Categorias"
    template_name = 'Listado Categorias2.html'

class agregar_categoria(CreateView):
    model = Categoria
    form_class = CategoriaForm
    queryset = Categoria.objects.all()
    template_name = "Agregar categoria.html"
    success_url = reverse_lazy('categorias')

class modificar_categoria(UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = "modificar categorias.html"
    success_url = reverse_lazy('categorias')


class eliminar_categoria(DeleteView):
    model = Categoria
    template_name = "categoria_confirm_delete.html"
    success_url = reverse_lazy('categorias')


#Vistas de las fuentes de información
class listar_Fuente_informacion(ListView):
    queryset = Fuente_Informacion.objects.all()
    context_object_name = "Fuentes"
    template_name = 'Listado Fuentes de informacion.html'

class agregar_fuente_info(CreateView):
    model = Fuente_Informacion
    form_class = Fuente_Info_Form
    queryset = Fuente_Informacion.objects.all()
    template_name = "Agregar fuente de informacion.html"
    success_url = reverse_lazy('fuentes-informacion')

class modificar_fuente_info(UpdateView):
    model = Fuente_Informacion
    form_class = Fuente_Info_Form
    template_name = "modificar fuente informacion.html"
    success_url = reverse_lazy('fuentes-informacion')


class eliminar_fuente_info(DeleteView):
    model = Fuente_Informacion
    template_name = "fuente_info_confirm_delete.html"
    success_url = reverse_lazy('fuentes-informacion')

#Vistas de los paises
class listar_Paises(ListView):
    queryset = Pais.objects.all()
    context_object_name = "Paises"
    template_name = 'Listado paises.html'

class agregar_pais(CreateView):
    model = Pais
    form_class = PaisForm
    queryset = Pais.objects.all()
    template_name = "Agregar pais.html"
    success_url = reverse_lazy('paises')

class modificar_pais(UpdateView):
    model = Pais
    form_class = PaisForm
    template_name = "Agregar pais.html"
    success_url = reverse_lazy('paises')

class eliminar_pais(DeleteView):
    model = Pais
    template_name = "pais_confirm_delete.html"
    success_url = reverse_lazy('paises')

#Vista del Panel Principal
class Panel_Administracion_View(TemplateView):
    template_name = 'Panel de administracion.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


#Vista de Pantalla Principal
class Pantalla_Principal_View(TemplateView):
    template_name = 'Pantalla Principal.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


#Vistas de los contenidos
class Visualizar_Contenido_View(TemplateView):
    template_name = 'Visualizacion de contenido.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context