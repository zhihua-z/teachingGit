# 导入tkinter并且重命名为tk
import tkinter as tk

from RouterPage import RouterPage
from MenuPage import MenuPage
from ConnectionPage import ConnectionPage
from DNSServerPage import DNSServerPage
from DevicePage import DevicePage

# App 它是一个状态机，它会保存当前程序所有的状态，并且连接所有的页面
# 切换页面
class App:
    def __init__(self):
        self.window = None
        self.menuPage = None
        self.routerPage = None
        self.devicePage = None
        self.DNSServerPage = None
        self.connectionPage = None
    
    def draw(self):
        self.window = tk.Tk()
        
        # geometry : 几何 / 形状
        self.window.geometry("1000x600")
        
        self.menuPage = MenuPage(700, 0, 300, 600, '#dddddd', self)
        self.routerPage = RouterPage(0, 0, 700, 600, 'white', self)
        self.devicePage = DevicePage(0, 0, 700, 600, 'white', self)
        self.DNSServerPage = DNSServerPage(0, 0, 700, 600, 'white', self)
        self.connectionPage = ConnectionPage(0, 0, 700, 600, 'white', self)
        
        self.menuPage.draw()
        self.routerPage.draw()
        
        
        self.window.mainloop()
    
    def switch(self, pageName):
        if pageName == '路由器':
            self.routerPage.draw()
            
        if pageName == '设备':
            self.devicePage.draw()
            
        if pageName == 'DNS服务器':
            self.DNSServerPage.draw()
            
        if pageName == '网络连接':
            self.connectionPage.draw()