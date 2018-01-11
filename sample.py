import numpy as np
import cv2
import tensorflow as tf

image = cv2.imread('image.jpg',1)
gray = cv2.imread('image.jpg',0)

while(1):
	cv2.imshow("Color",image)
	cv2.imshow("Gray",gray)
	k = cv2.waitKey(0) & 0xff
	if k == 27:
		cv2.destroyAllWindows()
		break
	elif k == 'q':
		cv2.destroyAllWindows()
		break
print "End of the script"
