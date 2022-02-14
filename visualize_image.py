import matplotlib.pyplot as plt
import cv2
from image_read_write import Image_read_write
class Visualize_image:
    def __init__(self, img_path):
        self.img_path = img_path
        self.ob = Image_read_write(self.img_path)

    def visualize_from_matplot(self):
        self.imgArray = self.ob.read_img_by_matplot()
        plt.imshow(self.imgArray)
        plt.show()
    
    def visualize_from_cv2(self):
        self.imgArray = self.ob.read_img_by_cv2()
        cv2.imshow('image', self.imgArray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
