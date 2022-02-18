import numpy as np
import matplotlib.pyplot as plt

from image_read_write import Image_read_write
from sobal_filter import Sobal_filter

class Apply_filter:
    def __init__(self, image):
        self.ob_sobal = Sobal_filter()
        self.h_filter = self.ob_sobal.get_horizontel_filetr()
        self.v_filter = self.ob_sobal.get_vertical_filter()
        self.ob_image = Image_read_write(image)
        self.imgArray = self.ob_image.read_img_by_matplot()
    
    def apply_vertical_filter(self, stride=1, padding=0):
        k = self.v_filter.shape[0]
        p = self.imgArray.shape[0]
        print(f"p is {p}")
        print(f"k is {k}")
        final_row = ((p-k+2*padding)//stride) + 1
        final_col = ((p-k+2*padding)//stride) + 1
        print("row is ",final_row)
        result = list() # to store the final result 
        # take vertically down stride across row by row
        for v_stride in range(final_row):
            # # take horizontally right stride across col by col
            for h_stride in range(final_col):
                target_area_of_pic = self.imgArray[v_stride: v_stride+k, h_stride: h_stride+k]
                # now multiply this area with filter and sum it all
                temp = target_area_of_pic * self.v_filter
                result.append(sum(sum(temp)))
        return np.array(result).reshape(final_row, final_col)

    def plot_after_filter(self, v_filter =True, h_filter=False):
        if v_filter:
            img = self.apply_vertical_filter()
            plt.imshow(img)
            plt.show()



