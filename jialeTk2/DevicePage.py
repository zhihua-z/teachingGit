# 导入tkinter并且重命名为tk
import tkinter as tk
from Page import Page

# Page 它会控制当前页面应该画什么
class DevicePage(Page):
    def __init__(self, x, y, w, h, bg, a):
        super().__init__(x, y, w, h, bg, a)
    
    def draw(self):
        # 画出这个页面的分区
        self.frame = tk.Frame(width=self.width, height=self.height, background=self.backgroundColor)
        self.frame.place(x = self.posX, y = self.posY)
        
        t = tk.Label(master=self.frame, text='这是设备页面', background=self.backgroundColor)
        t.place(x = 50, y = 20)