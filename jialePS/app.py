# 导入tkinter并且重命名为tk
import tkinter as tk

from MenuPage import MenuPage
from Canvas import Canvas
from TucengPage import TucengPage

# App 它是一个状态机，它会保存当前程序所有的状态，并且连接所有的页面
# 切换页面
class App:
    def __init__(self):
        self.window = None
        self.menuPage = None
        self.canvas = None
        self.tucengPage = None
    
    def draw(self):
        self.window = tk.Tk()
        
        # geometry : 几何 / 形状
        self.window.geometry("1300x700")
        
        self.menuPage = MenuPage(0, 0, 80, 700, self)
        self.canvas = Canvas(80, 0, 1070, 700, self)
        self.tucengPage = TucengPage(1150, 0, 150, 700, self)
        
        self.menuPage.draw()
        self.canvas.draw()
        self.tucengPage.draw()
        
        
        self.window.mainloop()
    
    def switch(self, pageName):
        pass