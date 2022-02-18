import matplotlib.pyplot as plt
import cv2
from RGB_channel_of_image import RGB_channel_visualize

class Plotting:
    def __init__(self):
        self.ob_rgb = RGB_channel_visualize('car1.jpeg')
        self.r,self.g,self.b = self.ob_rgb.get_all_rgb_channel()
        

    def plot_rgb(self, n_row=1, n_col=3 , fig_size=(10,7)):
        fig, ax = plt.subplots(nrows=n_row,ncols=n_col, figsize=fig_size)
        channel_list = [self.r, self.g, self.b]
        title = ["Red", 'Blue', "Green"]
        c = 0
        # ax[0,0].imshow(self.r)
        # plt.show()
        [a.set_axis_off() for a in ax.ravel()]
        for a in ax:
            a.imshow(channel_list[c])
            a.set_title(f'{title[c]} channel')

            c = c+1
        plt.show()

