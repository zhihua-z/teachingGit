# 导入tkinter并且重命名为tk
import tkinter as tk
from Page import Page
import styles

from UI import ImageButton, ImageButton2

# Page 它会控制当前页面应该画什么
class TucengPage(Page):
    def __init__(self, x, y, w, h, a):
        super().__init__(x, y, w, h, a)
        
        self.currPosition = 22
    
    def draw(self):
        # 画出这个页面的分区
        self.frame = tk.Frame(width=self.width, height=self.height, background=styles.menuBackgroundColor)
        self.frame.place(x = self.posX, y = self.posY)
        self.register(self.frame)
        
        self.add = ImageButton( self.frame, 
                                'img/add.png', 
                                (100, 50),
                                '新图层',
                                (18, self.currPosition),
                                labelPos=(5, 55))
        self.register(self.add)
        self.currPosition += 80
        
        
        # 画出全部的图层
        for t in self.app.tuceng:
            self.add1 = ImageButton2( self.frame, 
                                    t.image, 
                                    (100, 50),
                                    t.name,
                                    (18, self.currPosition),
                                    labelPos=(5, 55))
            self.register(self.add1)
            self.currPosition += 80
        
        
        
    def redraw(self):
        self.clear()
        self.currPosition = 22
        self.draw()

        
        
