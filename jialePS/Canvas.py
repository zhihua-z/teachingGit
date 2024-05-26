# 导入tkinter并且重命名为tk

# python3 -m pip install Pillow
import tkinter as tk
from Page import Page

from PIL import Image, ImageTk
import styles

import process

# Page 它会控制当前页面应该画什么
class Canvas(Page):
    def __init__(self, x, y, w, h, a):
        super().__init__(x, y, w, h, a)
        self.picture = None
    
    def draw(self):
        # 画出这个页面的分区
        self.frame = tk.Frame(width=self.width, height=self.height, background=styles.backgroundColor)
        self.frame.place(x = self.posX, y = self.posY)
        self.register(self.frame)
        
        if len(self.app.tuceng) == 0:
            return
        
        # 对于所有的图层，先把全部图层渲染一遍，然后把所有图层融合在一起
        imgs = []
        for t in self.app.tuceng:
            t.draw()
            imgs = [t.image] +imgs
        
        
        img = process.compose(imgs, self.width, self.height)
        
        # img = self.app.tuceng[0].image
        
        # 把融合了的结果花在self.picture里面，然后花在屏幕上
        if self.picture is not None:
            self.picture.destroy()
            self.picture = None
        photoImg = ImageTk.PhotoImage(img)
        self.picture = tk.Label(master=self.frame, image=photoImg)
        self.picture.image = photoImg
        self.picture.place(x = 0, y = 0)
        self.register(self.picture)
    
    def fnfn重画(self):
        self.clear()
        self.draw()
    