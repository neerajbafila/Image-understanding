
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2

class Image_read_write:
    def __init__(self, img_path):
        self.img_path = img_path

    def read_img_by_matplot(self):
        """read image and return imageArray

        Args:
            img_path (_type_): image

        Returns:
            _type_: _return array of image
        """
        img_path = self.img_path
        imgArray = mpimg.imread(img_path)
        print(f"shape of image is {imgArray.shape}")
        return imgArray

    def read_img_by_cv2(self):
        """read image and return imageArray

        Args:
            img_path (_type_): image

        Returns:
            _type_: _return array of image
        """
        img_path = self.img_path
        img = cv2.imread(img_path)
        print(f"shape of image is {img.shape}")
        return img


# ob = read_img_by_matplot('car1.jpeg')
# print(ob)
# ob = Image_read_write('car1.jpeg')
# ob.read_img_by_cv2()
