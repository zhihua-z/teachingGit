# 导入tkinter并且重命名为tk
import tkinter as tk
from PIL import Image, ImageTk
from Page import Page
import styles

from UI import ImageButton

# Page 它会控制当前页面应该画什么
class MenuPage(Page):
    def __init__(self, x, y, w, h, a):
        super().__init__(x, y, w, h, a)
    
    def draw(self):
        # 画出这个页面的分区
        self.frame = tk.Frame(width=self.width, height=self.height, background=styles.menuBackgroundColor)
        self.frame.place(x = self.posX, y = self.posY)
        
        self.tiaozheng = ImageButton(self.frame, 
                                     'img/tiaozheng.png', 
                                     (35, 35),
                                     '调整',
                                     (18, 22))
        
        
        self.liangdu = ImageButton(self.frame, 
                                     'img/liangdu.png', 
                                     (35, 35),
                                     '亮度',
                                     (18, 92))
        
        
        self.gongneng = ImageButton(self.frame, 
                                     'img/button1.png', 
                                     (35, 35),
                                     '功能',
                                     (18, 162))
        
        
        