import cv2
import numpy as np
import dlib
from math import hypot
# Loading Camera and Nose image and Creating mask
cap = cv2.VideoCapture(0)
nose_image = cv2.imread("pig_nose.png")
_, frame = cap.read()
rows, cols, _ = frame.shape
nose_mask = np.zeros((rows, cols), np.uint8)
# Loading Face detector
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

while True:
    _, frame = cap.read()
    nose_mask.fill(0)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(frame)
    for face in faces:
        landmarks = predictor(gray_frame, face)
        # Nose coordinates
        top_nose = (landmarks.part(29).x, landmarks.part(29).y)
        center_nose = (landmarks.part(30).x, landmarks.part(30).y)
        left_nose = (landmarks.part(31).x, landmarks.part(31).y)
        right_nose = (landmarks.part(35).x, landmarks.part(35).y)
        nose_width = int(hypot(left_nose[0] - right_nose[0], left_nose[1] - right_nose[1]) * 1.7)
        nose_height = int(nose_width * 0.77)