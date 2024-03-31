# 导入tkinter并且重命名为tk
import tkinter as tk
from Page import Page

# Page 它会控制当前页面应该画什么
class MenuPage(Page):
    def __init__(self, x, y, w, h, bg, a):
        super().__init__(x, y, w, h, bg, a)
    
    def draw(self):
        # 画出这个页面的分区
        self.frame = tk.Frame(width=self.width, height=self.height, background=self.backgroundColor)
        self.frame.place(x = self.posX, y = self.posY)
        
        b1 = tk.Button(
            master=self.frame, 
            text='路由器', 
            highlightbackground=self.backgroundColor,
            command=self.switchRouterPage)
        b1.place(x = 10, y = 10)
        
        
        b2 = tk.Button(
            master=self.frame, 
            text='设备', 
            highlightbackground=self.backgroundColor,
            command=self.switchDevicePage)
        b2.place(x = 10, y = 60)
        
        
        b3 = tk.Button(
            master=self.frame, 
            text='DNS服务器', 
            highlightbackground=self.backgroundColor,
            command=self.switchDNSServerPage)
        b3.place(x = 10, y = 110)
        
        
        b4 = tk.Button(
            master=self.frame, 
            text='网络连接', 
            highlightbackground=self.backgroundColor,
            command=self.switchConnectionPage)
        b4.place(x = 10, y = 160)
        
    def switchRouterPage(self):
        self.app.switch('路由器')
    
    def switchDevicePage(self):
        self.app.switch('设备')
    
    def switchDNSServerPage(self):
        self.app.switch('DNS服务器')
    
    def switchConnectionPage(self):
        self.app.switch('网络连接')
    