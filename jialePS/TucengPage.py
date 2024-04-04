# 导入tkinter并且重命名为tk
import tkinter as tk
from Page import Page
import styles

from UI import ImageButton

# Page 它会控制当前页面应该画什么
class TucengPage(Page):
    def __init__(self, x, y, w, h, a):
        super().__init__(x, y, w, h, a)
    
    def draw(self):
        # 画出这个页面的分区
        self.frame = tk.Frame(width=self.width, height=self.height, background=styles.menuBackgroundColor)
        self.frame.place(x = self.posX, y = self.posY)
        
        self.add = ImageButton( self.frame, 
                                'img/add.png', 
                                (100, 50),
                                '新图层',
                                (18, 22),
                                labelPos=(30, 58))