import process

class Layer:
    def __init__(self, img=None, img_path=None):
        self.name = img_path
        self.image = img
        self.brightness_val = 0
        self.opacity = 1
        self.result_image = None

    def render(self):
        self.result_image = process.adjust_brightness(self.image, self.brightness_val)
        # self.result_iamge = process.adjust_opacity(self.image, self.opacity)
        return self.result_image