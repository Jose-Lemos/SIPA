from django.utils import timezone
from datetime import datetime
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
User = get_user_model()
 


class Pais(models.Model):
    nombre = models.CharField(max_length = 150, null = False, blank = None, unique=True)
    idioma = models.CharField(max_length = 250, null = False, blank = None)
    fecha_creacion = models.DateField(default = timezone.now(), null = False, blank = None)

    def __str__(self):
        return self.nombre
    

class Adjunto(models.Model):
    nombre = models.CharField(max_length=250, null = False, blank = None, unique=True)
    imagen = models.ImageField(upload_to='images/', default='adjunto.png', max_length=250)
    URL = models.URLField(max_length= 200, null = False, blank = None, unique=True)
    fecha_creacion = models.DateField(default = timezone.now(), null = False, blank = None)

    def __str__(self):
        return self.URL
    
   

class Categoria(models.Model):
    fecha = models.DateField(null=False, blank=False, default= datetime.date(timezone.now()))
    concepto = models.CharField(max_length=200, null = False, blank = None, unique=True)

    def __str__(self):
        return self.concepto
    




class Fuente_Informacion(models.Model):
    nombre = models.CharField(max_length=200, null = False, blank = None)
    URL = models.URLField(max_length= 200, null = False, blank = None, unique=True)
    tipo = models.CharField(max_length=150)
    nivel = models.PositiveIntegerField(default=1)
    fecha = models.DateField(default=timezone.now())
    idPais = models.ForeignKey(Pais, on_delete=models.CASCADE, null=True)
    idPadre = models.IntegerField(default=0)

    def __str__(self): 
        return self.URL
    
    

class Contenido_Original(models.Model):
    fecha_acceso = models.DateField(default = timezone.now(), null = False, blank = None)
    contenido = models.TextField(max_length=255)
    idFuente = models.ForeignKey(Fuente_Informacion, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('contenido', kwargs={'pk': self.pk})

    def __str__(self):
        return self.contenido


class Contenido_Procesado(models.Model):
    titulo = models.CharField(max_length=200, null = False, blank = None, unique=True)
    fecha_Creacion = models.DateField(default = timezone.now(), null = False, blank = None)
    contenido = models.TextField()
    anotacion = models.TextField()
    idAdjunto = models.ForeignKey( Adjunto, null=False, blank=False, on_delete=models.CASCADE)
    idContenido_Original = models.ForeignKey(Contenido_Original, null=False, blank=False, on_delete=models.CASCADE)
    idCategoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    html = models.TextField(default="")

    def __str__(self):
        return self.titulo
    
    



