
import cv2
import torch
from torchvision import transforms
from PIL import Image

transform = transforms.Compose([
	 transforms.ToTensor()])
"""
transformacion_2 =transforms.Compose([
	transforms.ToPILImage("RGB")
	])
"""

 # Cargamos la imagen del disco duro
imagen = cv2.imread("dog.jpg")
 #cv2.imshow("prueba", imagen)
 #cv2.waitKey(0)

 #img = Image.open("dog.jpg") # Por lo que entiendo esta sentencia viene de la libreria de python (PIL) y sirve para 
imagen_t = transform(imagen)
#imagen_t.cuda
#imagen_nueva = imagen_t[0].numpy().transpose(1,2,0)
imagen_nueva = imagen_t[0].permute(1,0).numpy()
#cv2.imwrite('nuevo_perro.png', imagen_nueva)
cv2.imshow("prueba_2",imagen_nueva)
cv2.waitKey(0)