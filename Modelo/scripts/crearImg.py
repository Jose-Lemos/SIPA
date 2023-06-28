from PIL import Image #Importamos el modulo
import requests
from io import BytesIO
import os


base_descargas = path_imagenes = os.path.join(os.path.join(os.path.expanduser('~')), 'Downloads') 
base_descargas = str(base_descargas).replace("\\", "/")

url = "https://www.bas.ac.uk/wp-content/uploads/2015/03/10010588-edited-400x250.jpg"  # Replace with the actual URL of the image
response = requests.get(url)

img = Image.open(BytesIO(response.content)) #Abrimos la imagen
# responsePDF = FileResponse(img, as_attachment=True)

# return responsePDF
#nuevaimg = img.rotate(25) #Rotamos
img.show() #Mostramos
img.save(base_descargas,"JPEG")