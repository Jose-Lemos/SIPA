import jinja2
import pdfkit
import os


base_descargas = path_imagenes = os.path.join(os.path.join(os.path.expanduser('~')), 'Downloads') 

def crear_pdf(ruta_template, info, ruta_css, titulo):
    nombre_template = ruta_template.split("/")[-1]
    ruta_template = ruta_template.replace(nombre_template, "")

    env = jinja2.Environment(loader=jinja2.FileSystemLoader(ruta_template))
    template = env.get_template(nombre_template)
    html = template.render(info)

    options = {
        "encoding": "UTF-8",
    }

    config = pdfkit.configuration(wkhtmltopdf="C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")

    ruta_salida = base_descargas + "/" + titulo + ".pdf"

    pdfkit.from_string(html, ruta_salida,css = ruta_css, options=options, configuration=config)

if __name__ == "__main__":
    ruta_template = "C:/Users/progr/Desktop/SIPA/SIPA/Modelo/static/scripts/template/base_pdf.html"
    info = {
        "Adjunto": "https://www.bas.ac.uk/wp-content/uploads/2015/03/10008128-edited-400x250.jpg",
        "titulo": "COntenido 1",
        "contenido": "cuerpo1",
        "fecha_Creacion":"hoy",
        "fuente": "bas"
    }
    crear_pdf(ruta_template, info, "", "Prueba")


