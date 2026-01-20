from PIL import Image
from rembg import remove

#Definimos variables
path_in = 'camarero.jpg'
path_out = "camarero_sin_fondo.png"

foto = Image.open(path_in)

#Aplicamos la funcion para eliminar y guardamos el resultado en la ruta 
salida = remove(foto)
salida.save(path_out)