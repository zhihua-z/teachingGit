# 导入tkinter并且重命名为tk
import tkinter as tk

from MenuPage import MenuPage
from Canvas import Canvas
from TucengPage import TucengPage

from SubMenu import TiaozhengPage, LiangduPage, GongnengPage

class Caidan:
    def __init__(self, name, page):
        self.name = name
        self.page = page
        self.opened = False

# App 它是一个状态机，它会保存当前程序所有的状态，并且连接所有的页面
# 切换页面
class App:
    def __init__(self):
        self.window = None
        self.menuPage = None
        self.canvas = None
        self.tucengPage = None
        
        self.tiaozhengPage = None
        self.openTiaozhengPage = False
        
        self.tuceng = [] # 保存所有的图层，每一个图层都是一张照片
        
        self.tiaozhengPage = TiaozhengPage(80, 0, 200, 700, self)
        self.liangdupage = LiangduPage(80, 0, 200, 700, self)
        self.gongnengPage = GongnengPage(80, 0, 200, 700, self)
        
        self.caidanDict = {
            '调整': Caidan('调整', self.tiaozhengPage),
            '亮度': Caidan('亮度', self.liangdupage),
            '功能': Caidan('功能', self.gongnengPage)
        }
    
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
    
    # switch (调整)
    def switch(self, pageName):
        for key in self.caidanDict:
            caidan = self.caidanDict[key]
            
            caidan.page.clear()
        
        caidan = self.caidanDict[pageName]
        if caidan.opened:
            self.canvas.setSize((1080, 700))
            self.canvas.setPosition((80, 0))
            self.canvas.draw()
            
            caidan.opened = False
        else:
            self.canvas.setSize((870, 700))
            self.canvas.setPosition((280, 0))
            self.canvas.draw()
            caidan.page.draw()
            
            caidan.opened = True
            
            # 如果我本来打开了调整菜单，调整菜单True，其他菜单False
            # 如果这时候我直接切换到亮度菜单，亮度菜单设置为True，其他菜单应该被重置回False
            for key in self.caidanDict:
                caidan2 = self.caidanDict[key]
                
                if caidan.name != caidan2.name:
                    caidan2.opened = False
                
        
                