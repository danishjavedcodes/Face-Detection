import cv2
#for random color
from random import randrange

#already trained model
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')



# #get img
# img = cv2.imread('img1.jpg')
# #convert to B&W
# grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# #detect rectangle coordinates
#
#
# face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
#
# #draw rectangle along faces
# for (x, y, w, h) in face_coordinates:
#     cv2.rectangle(img, (x, y), (x+w, y+h), (randrange(128,256),randrange(256),randrange(256)),2)
# #show image
# cv2.imshow('face detector', img)
# cv2.waitKey()
# # print (face_coordinates)
# print ("dj")



#for video
webcam = cv2.VideoCapture(0)
key = cv2.waitKey(1)
while True:

    successful_frame_read, frame = webcam.read()
    grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_frame)
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (randrange(256),randrange(256),randrange(256)),2)
    cv2.imshow('face detected',frame)
    cv2.waitKey(1)

    if key == 81 or key == 113:
        break
webcam.release()
 