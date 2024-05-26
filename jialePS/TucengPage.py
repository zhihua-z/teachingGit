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
            daxiao = t.image.size
            self.add1 = ImageButton2( self.frame, 
                                    t.image, 
                                    (100,int(daxiao[1]/daxiao[0]*100)),
                                    t.name,
                                    (18, self.currPosition),
                                    command =lambda tuceng=t: self.fn点击按钮(tuceng),
                                    labelPos=(5,int(daxiao[1]/daxiao[0]*100)+5 )
                                    ,current = t.current)
            self.register(self.add1)
            self.currPosition += int(daxiao[1]/daxiao[0]*100) +30


    #点击按钮切换图层
    def fn点击按钮(self,t):
        for tuceng in self.app.tuceng:
            tuceng.current = False
        t.current = True  
        self.app.currenttuceng = t
        self.app.tucengPage.fn重画()
        
    def fn重画(self):
        self.clear()
        self.currPosition = 22
        self.draw()

        
        
