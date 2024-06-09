from PIL import Image, ImageTk
import tkinter as tk
import copy

import process


class Tuceng:
    def __init__(self, name, img, x, y, myImage, current):
        self.name = name
        self.image = img
        self.x = x
        self.y = y
        self.current = current
        self.imageSetting = myImage
        
        # 设置
        self.可见 = True
        self.亮度 = 0
        self.饱和度 = 0
        self.透明度 = 1 # 0 没有 1 满格
        
        # 上一轮设置 previous
        self.p可见 = self.可见
        self.p亮度 = self.亮度
        self.p饱和度 = self.饱和度
        self.p透明度 = 1
        
        
        # 原图
        self.originalImage = copy.deepcopy(img)
        
    def draw(self):
        if self.亮度 != self.p亮度 or self.饱和度 != self.p饱和度 or self.透明度 != self.p透明度:
            self.image = copy.deepcopy(self.originalImage)
        
        if self.亮度 != self.p亮度:
            self.image = process.liangdu(self.image, self.亮度)
        
        if self.饱和度 != self.p饱和度:
            self.image = process.baohedu(self.image, self.饱和度)
            
        if self.透明度 != self.p透明度:
            self.image = process.fn调整透明度(self.image, self.透明度)

        
        self.p可见 = self.可见
        self.p亮度 = self.亮度
        self.p饱和度 = self.饱和度
        self.p透明度 = self.透明度
