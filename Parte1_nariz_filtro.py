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
