from  image_read_write import Image_read_write
from visualize_image import Visualize_image
from RGB_channel_of_image import RGB_channel_visualize

# ob = Visualize_image('car1.jpeg')
# ob.visualize_from_matplot()
# # ob.visualize_from_cv2()

ob_r = RGB_channel_visualize('car1.jpeg')
# ob_r.get_red_channel()
# ob_r = ob_r.get_blue_channel()
ob_r = ob_r.get_green_channel()