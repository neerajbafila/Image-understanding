from  image_read_write import Image_read_write
from visualize_image import Visualize_image
from RGB_channel_of_image import RGB_channel_visualize
from plotting import Plotting
from apply_filter import Apply_filter
# ob = Visualize_image('car1.jpeg')
# ob.visualize_from_matplot()
# # ob.visualize_from_cv2()

# ob_r = RGB_channel_visualize('car1.jpeg')
# r = ob_r.get_red_channel()
# print(f"r is {r}")
# b = ob_r.get_blue_channel()
# g = ob_r.get_green_channel()

# ob_rgb = RGB_channel_visualize('car1.jpeg')
# r,g,b = ob_rgb.get_all_rgb_channel()
# print(f"r is {r}")
# print(f"g is {g}")
# print(f"b is {b}")


# """For RGB channel"""
# ob_p = Plotting()
# ob_p.plot_rgb()

"""For Filter"""

ob_filter = Apply_filter('car_gray.jpeg')
# ob_filter.apply_vertical_filter()
ob_filter.plot_after_filter()




