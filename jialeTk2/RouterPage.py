# 导入tkinter并且重命名为tk
import tkinter as tk
from Page import Page

from Router import Router

# Page 它会控制当前页面应该画什么
class RouterPage(Page):
    def __init__(self, x, y, w, h, bg, a):
        super().__init__(x, y, w, h, bg, a)
        
        # 路由器列表
        self.router_list = []
        
        dns = ''
        
        r1 = Router('客厅', dns, '49.18.27.11',
            ['192.168.0.1', '192.168.0.2', '192.168.0.3'])
        r2 = Router('中国移动-银泰', dns, '199.172.1.10', [])
        r3 = Router('中国移动-上城区', dns, '193.0.1.12', ['192.168.0.4'])
        r4 = Router('小花家沙发前面茶几上', dns, '105.1.0.40', ['10.0.0.1'])
        
        self.router_list.append(r1)
        self.router_list.append(r2)
        self.router_list.append(r3)
        self.router_list.append(r4)
        

    
    def draw(self):
        # 画出这个页面的分区
        self.frame = tk.Frame(width=self.width, height=self.height, background=self.backgroundColor)
        self.frame.place(x = self.posX, y = self.posY)
        
        start_pos_x = 10
        start_pos_y = 10
        
        for x in self.router_list:
            # 画路由器的名字和ip
            x1 = tk.Label(master=self.frame, text=x.name + ' ' + x.ip, background=self.backgroundColor)
            x1.place(x = start_pos_x, y = start_pos_y)
            
            x1 = tk.Label(master=self.frame, text='可用ip: ', background=self.backgroundColor)
            x1.place(x = start_pos_x, y = start_pos_y + 30)
            
            if len(x.ip_list) > 0:
                count = 0
                for y in x.ip_list:
                    x1 = tk.Label(master=self.frame, text=y, background=self.backgroundColor)
                    x1.place(x = 50 + start_pos_x + count * 100, y = start_pos_y + 30)
                    count += 1
            else:
                x1 = tk.Label(master=self.frame, text='无', background=self.backgroundColor)
                x1.place(x = 50 + start_pos_x, y = start_pos_y + 30)
            
            # 画出路由器全部可用ip
            
            
            start_pos_y += 100
        
    def findRouter(self, luyouqi_name):
        for x in self.router_list:
            if x.name == luyouqi_name:
                return x
            
        return None