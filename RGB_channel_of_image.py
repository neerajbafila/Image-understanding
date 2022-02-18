from image_read_write import Image_read_write
import numpy as np
import cv2

import matplotlib.pyplot as plt

class RGB_channel_visualize:
    def __init__(self,img_path):
        self.img_path = img_path
        self.ob = Image_read_write(self.img_path)
        # self.imgArray = self.ob.read_img_by_cv2()
        self.imgArray = self.ob.read_img_by_matplot()
        
    
    def get_zero_matrix(self):
        if self.imgArray.shape[-1]!=3:
            print("Error: image is not RGB")
        else:
            imgShape = self.imgArray.shape
            r, g, b = cv2.split(self.imgArray)
            return np.zeros(shape=r.shape, dtype=r.dtype)

    def get_red_channel(self):
        if self.imgArray.shape[-1] !=3:
            print("Error: image is not RGB")
        else:   
            r,g,b = cv2.split(self.imgArray)
            z = self.get_zero_matrix()
            red_channel = cv2.merge([r,z,z])
            # plt.imshow(red_channel)
            # plt.show()
            return red_channel
    
    def get_blue_channel(self):
        if self.imgArray.shape[-1]!=3:
            print("Error: image is not RGB")
        else:
            r,g,b = cv2.split(self.imgArray)
            z = self.get_zero_matrix()
            blue_channel = cv2.merge([z,z,b])
            # plt.imshow(blue_channel)
            # plt.show()
            return blue_channel
    
    def get_green_channel(self):
        if self.imgArray.shape[-1]!=3:
            print("Error: image is not RGB")
        else:

            r,g,b = cv2.split(self.imgArray)
            z = self.get_zero_matrix()
            green_channel = cv2.merge([z,g,z])
            # plt.imshow(green_channel)
            # plt.show()
            return green_channel
    
    def get_all_rgb_channel(self):
        print(len(self.imgArray))
        if self.imgArray.shape[-1]!=3:
            print("Error: image is not RGB")
        else:
            red = self.get_red_channel()
            blue = self.get_blue_channel()
            green = self.get_green_channel()
            return red, blue, green
    



