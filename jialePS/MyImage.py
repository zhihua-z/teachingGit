import PIL

# 储存图像的一些信息
# png格式的文件有透明通道(channel)，RGB + Alpha （透明度）
# jpg / webp 只有三个通道，RGB
class MyImage:
    def __init__(self, image, filename):
        self.image = image
        self.filename = filename
        self.hasAlpha = False
        
        if filename[-3:] == 'png':
            self.hasAlpha = True
        pass