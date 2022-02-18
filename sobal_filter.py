import numpy as np

class Sobal_filter:
    
    def get_filter(self):
        filter = np.array([[1,0,-1], [2,0,-2], [1,0,-1]])
        return filter
    
    def get_vertical_filter(self):
        v_filter = self.get_filter()
        return v_filter
    
    def get_horizontel_filetr(self):
        h_filter = self.get_filter().T
        return h_filter

