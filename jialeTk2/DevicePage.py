# 导入tkinter并且重命名为tk
import tkinter as tk
from Device import InternetDevice
from Page import Page

from Phone import Phone

# Page 它会控制当前页面应该画什么
class DevicePage(Page):
    def __init__(self, x, y, w, h, bg, a):
        super().__init__(x, y, w, h, bg, a)
        
        # 设备列表
        self.device_list = []
        
        dns = ''
        
        d1 = Phone('我的手机', 'iphone 11')
        d2 = InternetDevice('我的电脑')
        d3 = InternetDevice('我的电脑2')
        d4 = Phone('我的d30', 'sony d30')
        d5 = Phone('小花的手机', 'huawei mate 30 pro')
        
        self.device_list.append(d1)
        self.device_list.append(d2)

        

    
    def draw(self):
        # 画出这个页面的分区
        self.frame = tk.Frame(width=self.width, height=self.height, background=self.backgroundColor)
        self.frame.place(x = self.posX, y = self.posY)
        
        start_pos_x = 10
        start_pos_y = 10
        
        for x in self.device_list:
            # 画设备的名字和ip
            
            x1 = tk.Label(master=self.frame, text=x.name, background=self.backgroundColor)
            x1.place(x = start_pos_x, y = start_pos_y)
            
            if x.ip is not None:
                x1 = tk.Label(master=self.frame, text='ip: ' + x.ip, background=self.backgroundColor)
                x1.place(x = start_pos_x + 100, y = start_pos_y)
            else:
                x1 = tk.Label(master=self.frame, text='无网络连接', background=self.backgroundColor)
                x1.place(x = start_pos_x + 100, y = start_pos_y)
            
            if not x.connected:
                x1 = tk.Button(master=self.frame, 
                            text='连接', 
                            highlightbackground=self.backgroundColor, 
                            command=lambda y = x: self.connect(y))
                x1.place(x = start_pos_x, y = start_pos_y + 30)
            
            
            start_pos_y += 100
    
    def connect(self, device):
        luyouqi_name = input('你要连哪个路由器？') 
    
        luyouqi = self.app.findRouter(luyouqi_name)
        
        device.connect(luyouqi)
        self.draw()
     