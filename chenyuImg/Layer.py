import process
import copy

class Layer:
    red = 8
    green = 4
    blue = 4
    alpha = 1
    
    def __init__(self, img=None, layername=None, image_path = None):
        self.name = layername
        self.path = image_path
        self.image = img
        self.brightness_val = 0
        self.opacity = 1
        self.result_image = None
        self.channel = 15 # 1111

    def render(self):
        self.result_image = copy.deepcopy(self.image)
        # 提取颜色
        if self.channel != 15:
            self.result_image = process.extract_channel(self.result_image, self.channel)
    
        # 修改亮度
        if self.brightness_val != 0:
            self.result_image = process.adjust_brightness(self.result_image, self.brightness_val)
            # self.result_iamge = process.adjust_opacity(self.image, self.opacity)
        return self.result_image