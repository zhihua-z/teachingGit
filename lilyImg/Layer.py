"""
Layer : 
- can open file
- can redraw

"""


import process


class Layer:
    def __init__(self):
        self.path = ""
        self.name = self.path
        self.image = None
        self.final_result = None
        
        self.crop_A_point = None
        self.crop_B_point = None

        self.brightness = 0
        self.saturation = 50
        self.vibrance = 50

    def render(self):

        # apply brightness
        t_image = process.adjust_brightness(self.image, self.brightness)

        # apply vibrance
        t_image = process.adjust_vibrance(t_image, self.vibrance)

        # apply contrast
        t_image = process.adjust_saturation(t_image, self.saturation)

        # apply saturation
        
        # apply crop mask (if there is any)
        if self.crop_A_point:
            t_image = process.crop_a_mask(t_image, self.crop_A_point, self.crop_B_point)
        
        if self.crop_B_point:
            t_image = process.crop_b_mask(t_image, self.crop_A_point, self.crop_B_point)
        # ...
        
        print('---------==========----------')
        print(self.crop_A_point, self.crop_B_point)

        self.final_result = t_image

    def clear(self):
      pass
