import cv2

# cargar el archivo jpg indicado
img = cv2.imread('logo.jpg', cv2.IMREAD_GRAYSCALE)
#cv2.IMREAD_COLOR  		Capturar la imagen a color.
#cv2.IMREAD_GRAYSCALE	Caputrar la imagen a escala de Grisis.
#cv2.IMREAD_UNCHANGED	Capturar la imagen definido por el archivo.


# guardar la imagen con el formato que le indiquemos(PNG,BMP,TIFF,JPG)
cv2.imwrite('save.png', img)
