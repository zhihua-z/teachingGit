# 导入tkinter并且重命名为tk

# python3 -m pip install Pillow
import tkinter as tk
from Page import Page

from PIL import Image, ImageTk
import styles

# Page 它会控制当前页面应该画什么
class Canvas(Page):
    def __init__(self, x, y, w, h, a):
        super().__init__(x, y, w, h, a)
    
    def draw(self):
        # 画出这个页面的分区
        self.frame = tk.Frame(width=self.width, height=self.height, background=styles.backgroundColor)
        self.frame.place(x = self.posX, y = self.posY)
        
        # 打开一张照片
        self.img = Image.open('img/mountain.jpg')
        
        img_size = self.img.size
        canvas_size = (self.width, self.height)
        
        border_size = (60, 60)
        canvas_size = (canvas_size[0] - border_size[0], canvas_size[1] - border_size[1])
        
        factor_x = img_size[0] / canvas_size[0]
        factor_y = img_size[1] / canvas_size[1]
        
        new_size = img_size
        
        if factor_x > factor_y:
            # 调整宽度
            new_size = (int(img_size[0] / factor_x), int(img_size[1] / factor_x))
        else:
            # 高度超标
            new_size = (int(img_size[0] / factor_y), int(img_size[1] / factor_y))
        
        self.img = self.img.resize(new_size)
        
        
        # 计算居中位置s
        img_size = self.img.size
        canvas_size = (self.width, self.height)
        
        mov_x = (canvas_size[0] - img_size[0]) // 2
        mov_y = (canvas_size[1] - img_size[1]) // 2
        
        
        # 通过ImageTk把这张照片转换为tkinter可以使用的格式
        self.photoImage = ImageTk.PhotoImage(self.img)
        
        # 通过Tkinter画照片
        t = tk.Label(master=self.frame, image=self.photoImage)
        t.place(x=mov_x, y=mov_y)
        