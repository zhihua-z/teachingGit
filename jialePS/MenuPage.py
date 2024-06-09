# 导入tkinter并且重命名为tk
import tkinter as tk
from PIL import Image, ImageTk
from Page import Page
import styles

from UI import class图片按钮

# Page 它会控制当前页面应该画什么
class MenuPage(Page):
    def __init__(self, x, y, w, h, a):
        super().__init__(x, y, w, h, a)
    
    def draw(self):
        # 画出这个页面的分区
        self.frame = tk.Frame(width=self.width, height=self.height, background=styles.菜单背景颜色)
        self.frame.place(x = self.posX, y = self.posY)
        self.register(self.frame)
        
        self.tiaozheng = class图片按钮(self.frame, 
                                     'img/tiaozheng.png', 
                                     (35, 35),
                                     '调整',
                                     (18, 22),
                                     command=self.switchtiaozheng)
        self.register(self.tiaozheng)
        
        
        self.liangdu = class图片按钮(self.frame, 
                                     'img/liangdu.png', 
                                     (35, 35),
                                     '亮度',
                                     (18, 92),
                                     command=self.switchLiangdu)
        self.register(self.liangdu)
        
        
        self.gongneng = class图片按钮(self.frame, 
                                     'img/button1.png', 
                                     (35, 35),
                                     '功能',
                                     (18, 162),
                                     command=self.switchGongneng)
        self.register(self.gongneng)
        
        
    def switchtiaozheng(self):
        self.app.switch('调整')
    
    def switchLiangdu(self):
        self.app.switch('亮度')
        
    def switchGongneng(self):
        self.app.switch('功能')
        
        