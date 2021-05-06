cap = cv2.VideoCapture(0) #0 es la camara principal
con = 0
while cap.isOpened():

    #BGR image feed from camera
    ret, img = cap.read()
    #BGR to grayscale
    face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    filename='C:\Users\fatim\OneDrive\Documentos\semana_tec_programación'
    img=cv2.imread(filename)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    fl=face.detectMultiScale(gray,1.09,7)
    ey=face.detectMultiScale(gray,1.09,7)
    hat=cv2.imread('C:\Users\fatim\OneDrive\Documentos\semana_tec_programación\sombrero.png')
    glass=cv2.imread('C:\Users\fatim\OneDrive\Documentos\semana_tec_programación\lentes.png')
    def put_hat(hat, fc, x, y, w, h):
        face_width = w
        face_height = h
        hat_width = face_width + 1
        hat_height = int(0.50 * face_height) + 1
        hat = cv2.resize(hat, (hat_width, hat_height))

        for i in range(hat_height):
        for j in range(hat_width):
            for k in range(3):
                if hat[i][j][k] < 235:
                    fc[y + i - int(0.40 * face_height)][x + j][k] = hat[i][j][k]
        return fc

    for (x, y, w, h) in fl:
    frame = put_hat(hat, img, x, y, w, h)



    cv2.imshow('image',frame)

    k = cv2.waitKey(10)
    if k==27:
        break


cap.release()
cv2.destroyAllWindows()