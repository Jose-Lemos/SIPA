import urllib.request
from bs4 import BeautifulSoup

page = urllib.request.urlopen('https://www.bas.ac.uk/').read().decode()  #Este parámetro define la URL de donde se van a obtener los elementos
soup = BeautifulSoup(page, 'html.parser')

#Links de la Pagina Principal (Home)
links = soup('link')

for link in links:
    print(link.get('href'))

#Titulo de la Pagina Principal
cabecera = soup('head')

for elemento in cabecera:
    titulo_pagina =(elemento.find_all('title'))
    print(titulo_pagina)

#Articulos


#Titulos de los articulos de las diferentes secciones
titulo_articulos = soup.find_all('h2', class_="text-center bandTitle")

for titulo in titulo_articulos:
    print(titulo.string)


secciones_selects = soup.select('section')

#Clase y Objeto  de Articulos

class Articulo:
    def __init__(self, titulo, link_pagina, link_imagen) -> None:
        self.titulo=titulo
        self.pagina = link_pagina
        self.imagen = link_imagen


    def __str__(self):
        texto="Titulo-Articulo: {0} - Link: {1} - Imagen: {2}"
        return texto.format(self.titulo, self.pagina, self.imagen)    


#Clase y Objeto seccion,  con su lista de articulos 
class Seccion:
    lista_articulos = [Articulo]
    def __init__(self, titulo) -> None:
        self.titulo = titulo
    
    def __str__(self):
        texto = "Titulo-Seccion: {0}"
        return texto.format(self.titulo)

    def listar_articulos(self):
        for articulo in self.lista_articulos:
            print(articulo)


#Clase y Objeto pagina, con su lista de secciones
class Pagina: 
    lista_secciones = [Seccion]

    def __init__(self, titulo, url) -> None:
        self.titulo = titulo
        self.url = url


    def __str__(self) :
        texto = "Titulo: {0} - url: {1}"
        return texto.format(self.titulo, self.url)

    def listar_secciones(self):
        for seccion in self.lista_secciones:
            print(seccion)
  
#Creacion de los objetos Pagina, Seccion y Articulo
#Creo la Pagina Home del BAS
pagina_home_bas = Pagina('BAS','https://www.bas.ac.uk/')

#Creo las secciones de la pagina Home del BAS
for seccion in secciones_selects:
    mi_seccion_nueva = Seccion(seccion.get('class'))
    pagina_home_bas.lista_secciones.append(mi_seccion_nueva)



pagina_home_bas.listar_secciones()

#selectores de los tags donde se encuentran los articulos de la seccion 0
articulos_selects_links_s0 = soup.select('section > div > div > article > div > h4 > a ')
articulos_selects_imagenes_s0 = soup.select('section > div > div > article > div > a > img')

#Extraigo las secciones
seccion0 = pagina_home_bas.lista_secciones[0]
seccion1 = pagina_home_bas.lista_secciones[1]


def guardar_articulos_seccion0():
#Crear Articulo, asignar Titulo y link de pagina; y guardarlo en la lista de articulos de mi seccion
    i=0
    for arty_link in articulos_selects_links_s0: 
        mi_articulo_nuevo = Articulo(arty_link.string, arty_link.get('href'), articulos_selects_imagenes_s0[i].get('src'))

        seccion0.lista_articulos.append(mi_articulo_nuevo)
        i+=1

        



guardar_articulos_seccion0()

for articulo in pagina_home_bas.lista_secciones[0].lista_articulos:
    print(articulo)

