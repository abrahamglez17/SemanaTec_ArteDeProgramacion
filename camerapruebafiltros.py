import cv2
import time
import argparse


if __name__ == '__main__':
    
    script_start_time = time.time()

    parser = argparse.ArgumentParser(description='Camera visualization')

    ### Positional arguments
    parser.add_argument('-i', '--cameraSource', default=0, help="Introduce number or camera path, default is 0 (default cam)")

    
    args = vars(parser.parse_args())


    cap = cv2.VideoCapture(args["cameraSource"]) #0 local o primary camera
    while cap.isOpened():
        
        face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        filename='C:\Users\fatim\OneDrive\Documentos\semana_tec_programación'
        img=cv2.imread(filename)
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        fl=face.detectMultiScale(gray,1.09,7)
        ey=face.detectMultiScale(gray,1.09,7)
        hat=cv2.imread('C:\Users\fatim\OneDrive\Documentos\semana_tec_programación\sombrero.png')
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

            # img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        
        #BGR image feed from camera
        success,img = cap.read()    
        
        if not success:
            break
        if img is None:
            break

        
        cv2.imshow("Output", img)

        k = cv2.waitKey(10)
        #if k==27:
        if k>=0:
            break

    cv2.imshow('image',frame)
    cap.release()
    cv2.destroyAllWindows()


    print('Script took %f seconds.' % (time.time() - script_start_time))