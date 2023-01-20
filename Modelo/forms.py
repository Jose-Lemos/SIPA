from django import  forms
from .models import Categoria, Usuario, Configuracion_Fuente_Informacion, Contenido_Original, Contenido_Procesado, Fuente_Informacion, Adjunto, Pais

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'email',
            'password',
            'is_superuser',
        ]

        labels={
            'email': "E-mail:",
            'password': "Contraseña: ",
            'is_superuser': "Es SuperUsuario?: ",
        }

        widgets = {
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'contraseña':forms.PasswordInput(attrs={'class':'form-control'}),
            'is_superuser': forms.NullBooleanSelect(attrs={'class':'form-control'}),
        }


#class AdminForm(forms.ModelForm):
#    class Meta:
#       model = Admin
#       fields = [
#           'nombre',
#       ]


class Configuracion_Fuente_Info_Form(forms.ModelForm):
    class Meta:
        model = Configuracion_Fuente_Informacion
        fields = [
            'buscar_Titulo',
            'buscar_Contenido',
            'buscar_Imagenes',
            'buscar_links',
        ]



#class Contenido_Original_Form(forms.ModelForm):
#    class Meta:
#        model = Contenido_Original
#        fields = [
#            'contenido'
#        ]


class Contenido_Procesado_Form(forms.ModelForm):
    class Meta:
        model = Contenido_Procesado
        fields = [
            'titulo',
            'fecha_Creacion',
            'contenido',
            'anotacion',
            'idContenido_Original',
        ]


class Fuente_Info_Form(forms.ModelForm):
    class Meta:
        model = Fuente_Informacion
        fields = [
          'nombre',
          'URL',
          'tipo', 
          #'idContenido_Original', 
          #'idConfiguracion',
          'idPais'
        ]

        labels={
            'nombre': "Nombre:",
            'URL': "url:",
            'tipo': "Tipo:",
            #'idContenido_Original': "ID Contenido Original", 
            #'idConfiguracion': "ID Configuracion",
            'idPais':"ID Pais",
        }

        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'URL':forms.TextInput(attrs={'class':'form-control'}),
            'tipo':forms.TextInput(attrs={'class':'form-control'}),
        }

    def get_url(self) -> str:
       return self.fields['URL']


        


#class AdjuntoForm(forms.ModelForm):
#   class Meta:
#       model = Adjunto
#       fields = [
#
#       ]


class PaisForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = [
            'nombre',
            'idioma',
        ]

        labels={
            'nombre': "Nombre:",
            'idioma': "Idioma:",
        }

        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'idioma':forms.TextInput(attrs={'class':'form-control'}),
        }

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = [
            'concepto',
        ]

        labels={
            'concepto': "Concepto:",
        }

        widgets = {
            'concepto':forms.TextInput(attrs={'class':'form-control'}),
        }

