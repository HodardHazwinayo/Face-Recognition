from random import randint
import cv2
import sys
import os

CASCADE="../../face_cascade.xml"
FACE_CASCADE=cv2.CascadeClassifier(CASCADE)

def detect_faces(image_path):
	image = cv2.imread(image_path, 0)
	#image_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	faces = FACE_CASCADE.detectMultiScale(image, scaleFactor=1.16, minNeighbors=5, minSize=(25, 25), flags=0)
	for x, y, w, h in faces:
		sub_image = image[y-10:y+h+10, x-10: x+w+10]
		os.chdir("Extracted")
		cv2.write(str(randint(0, 10000))+".jpg", sub_image)
		os.chdir("../")
		cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 0), 2)

	cv2.imshow("Faces Found",image)
	if (cv2.waitKey(0) & 0xFF == ord('q')) or (cv2.waitKey(0) & 0xFF == ord('Q')):
		cv2.destroyAllWindows()

if __name__ == "__main__":
	if not "Extracted" in os.listdir("."):
		os.mkdir("Extracted")

	PATH = '../AvailableSessions/1/Images/Image1.jpg'
	detect_faces(PATH)

