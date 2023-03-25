import cv2
import os

dataset = "dataset"
name = "Avanish"
path = os.path.join(dataset, name)
if not os.path.isdir(path):
    os.mkdir(path)
(width, height) = (130, 100)

count = 1

alg = "haarcascade_frontalface_default.xml"
cam = cv2.VideoCapture(0)
haar_cascade = cv2.CascadeClassifier(alg)

while count < 31:
    print(count)
    _, img = cam.read()
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face = haar_cascade.detectMultiScale(grayImg, 1.3, 4)  #detectMultiScale method of the face object to detect faces in the image.
    for (x,y,w,h) in face:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
        faceOnly = grayImg[ y:y+h, x:x+w]
        resizeImg = cv2.resize(faceOnly, (width, height))
        cv2.imwrite("%s/%s.jpg" %(path, count), resizeImg)
        count += 1
    cv2.imshow("FaceDetection", img)
    key = cv2.waitKey(10)
    if key == ord("q"):
        break
print("Image captured successfully")
cam.release()
cv2.destroyAllWindows()