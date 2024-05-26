from PIL import Image, ImageTk
import tkinter as tk
import copy


class Tuceng:
    def __init__(self, name, img, x, y, myImage, current):
        self.name = name
        self.image = img
        self.x = x
        self.y = y
        self.current = current
        self.imageSetting = myImage
        
        # 原图
        self.originalImage = copy.deepcopy(img)
        
    def draw(self):
        pass

