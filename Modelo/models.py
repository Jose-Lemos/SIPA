from django.utils import timezone, dateformat
from datetime import datetime
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here
class UserManager(BaseUserManager):

    def create_user(self, email=None, password=None, superuser=False):
        if not email:
            raise ValueError('El usuario necesita un email')
        
        if not password:
            raise ValueError('El usuario necesita contraseña')
        
        user_obj = self.model(email=self.normalize_email(email))
        user_obj.set_password(password)
        user_obj.is_superuser = superuser
        user_obj.save(using=self._db)
        return user_obj

    def create_superuser(self, email=None, password=None):
        user_obj = self.create_user(email=email, password=password, superuser=True)
        return user_obj

class Usuario(PermissionsMixin, AbstractBaseUser):
    id = models.BigAutoField(auto_created=True, primary_key=True, verbose_name="ID")
    email = models.EmailField(max_length=255, unique=True, default="@gmail.com")
    password = models.CharField(max_length=255)
    is_superuser = models.BooleanField()

    # New manager
    objects = UserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = [] #USERNAME_FIELD and password are required by default

    def get_username(self):
        return self.email

    def __str__(self):
        return self.email

    # Required by admin app
    def is_staff(self):
        return self.is_superuser
    



class Contenido_Original(models.Model):
    fecha_acceso = models.DateField(default = timezone.now(), null = False, blank = None)
    contenido = models.TextField()

    def get_absolute_url(self):
        return reverse('contenido', kwargs={'pk': self.pk})

    def __str__(self):
        return self.contenido



class Configuracion_Fuente_Informacion(models.Model):
    buscar_Titulo = models.CharField(max_length= 200,null = False, blank = None)
    buscar_Contenido = models.CharField(max_length= 200, null = False, blank = None)
    buscar_Imagenes = models.CharField(max_length= 200, null = False, blank = None)
    buscar_links = models.CharField(max_length= 200, null = False, blank = None)

    def get_absolute_url(self):
        return reverse('fuentes', kwargs={'pk': self.pk})

    def __str__(self):
        return self.buscar_Titulo


class Pais(models.Model):
    nombre = models.CharField(max_length = 50, null = False, blank = None, unique=True)
    idioma = models.CharField(max_length = 250, null = False, blank = None)


    def __str__(self):
        return self.nombre


class Fuente_Informacion(models.Model):
    nombre = models.CharField(max_length=100, null = False, blank = None)
    URL = models.URLField(max_length= 200, null = False, blank = None)
    tipo = models.CharField(max_length=50)
    es_parte_de = models.PositiveBigIntegerField()
    nivel = models.PositiveIntegerField()
    fecha = models.DateField(default=timezone.now())
    idPais = models.ForeignKey(Pais, on_delete=models.CASCADE, null=True)

    def __str__(self): 
        return self.nombre
    
    


class Adjunto(models.Model):
    nombre = models.CharField(max_length=50, null = False, blank = None, unique=True)
    imagen = models.ImageField(upload_to='adjuntos', default='adjunto.png')

    def __str__(self):
        return self.nombre
    
   

class Categoria(models.Model):
    fecha = models.DateField(null=False, blank=False, default= datetime.date(timezone.now()))
    concepto = models.CharField(max_length=100, null = False, blank = None, unique=True)

    def __str__(self):
        return self.concepto



class Contenido_Procesado(models.Model):
    titulo = models.CharField(max_length=100, null = False, blank = None, unique=True)
    fecha_Creacion = models.DateField(default = timezone.now(), null = False, blank = None)
    contenido = models.TextField()
    anotacion = models.TextField()
    idAdjunto = models.ForeignKey( Adjunto, null=False, blank=False, on_delete=models.CASCADE)
    idContenido_Original = models.ForeignKey(Contenido_Original, null=False, blank=False, on_delete=models.CASCADE)
    idFuente = models.ForeignKey(Fuente_Informacion, on_delete=models.CASCADE)
    idCategoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
    
    



