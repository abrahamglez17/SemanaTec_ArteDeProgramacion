import cv2
import imutils

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

# Imágen a incrustar, png para que tenga transparencia
# IMREAD_UNCHANGED agrega 4 canales: en el 4to es un canal alfa o tranparencia
image = cv2.imread('helado.png', cv2.IMREAD_UNCHANGED)

# Clasificador
faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:

    ret, frame = cap.read()
    if ret == False: break
    frame = imutils.resize(frame, width=640)
    # Detección de los rostros presentes en el fotograma
    faces = faceClassif.detectMultiScale(frame, 1.3, 5)
    for (x, y, w, h) in faces:
        # Se comenta para que no salga el cuadro
        #cv2.rectangle(frame, (x,y), (x + w, y + h), (0, 255, 0), 2)
        
        # Redimencionarla al ancho del rostro con imutils
        # w es ancho del rostro detectado
        resized_image = imutils.resize(image, width = w)
        filas_image = resized_image.shape[0]
        col_image = w

        
        # Para que sólo sea una porción de tu cabeza y no todo arriba
        porcion_alto = filas_image // 4
        #El inicio de esto es sólo para que no importe que el gorro no quepa, que aun funcione
        dif = 0
        
        # Condición para que se dibuje la imagen sólo cuando el rostro este a una distancia aceptable para que se detecte
        if y + porcion_alto - filas_image >= 0:
            # Se toma una porción del video y ahi se incerta la imágen
            n_frame = frame[y - filas_image + porcion_alto: y + porcion_alto, x: x + col_image]

        else:
            dif =  abs(y - filas_image + porcion_alto)  
            n_frame = frame[0: y + porcion_alto, x: x + col_image]  
            
        mask = resized_image[:, :, 3] #Mask es como la imagen negra para poder mezclarlas
            

