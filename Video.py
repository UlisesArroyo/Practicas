import cv2

cap = cv2.VideoCapture('Video 1.mp4')

# Definir el codec y crear el objeto VideoWriter
fourcc = cv2.VideoWriter_fourcc('M','S','V','C')
out = cv2.VideoWriter('output.mkv', fourcc, 60.0, (720, 528))

while(True):
    # capturar el cuadro
    ret, frame = cap.read()

    if ret:
        # procesar la captura, convertir a grises
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # escribir el cuadro procesado
        out.write(gray)

        # mostar la captura actual
        cv2.imshow('video', gray)

    # esperar, si se presiona la tecla ESC salir 
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
out.release()

cv2.destroyAllWindows()