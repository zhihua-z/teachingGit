import process


class Layer:
    red = 8
    green = 4
    blue = 4
    alpha = 1
    
    def __init__(self, img=None, img_path=None):
        self.name = img_path
        self.image = img
        self.brightness_val = 0
        self.opacity = 1
        self.result_image = None
        self.channel = 15 # 1111

    def render(self):
        # 提取颜色
        self.result_image = process.extract_channel(self.image, self.channel)
    
        # 修改亮度
        self.result_image = process.adjust_brightness(self.result_image, self.brightness_val)
        # self.result_iamge = process.adjust_opacity(self.image, self.opacity)
        return self.result_image