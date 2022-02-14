import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

car_1 = cv2.imread('car_1.jpg')
cv2.imshow('car_1', car_1)
cv2.waitKey(0)
cv2.destroyAllWindows()