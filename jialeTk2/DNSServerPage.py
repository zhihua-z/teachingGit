# 导入tkinter并且重命名为tk
import tkinter as tk
from Page import Page

# Page 它会控制当前页面应该画什么
class DNSServerPage(Page):
    def __init__(self, x, y, w, h, bg, a):
        super().__init__(x, y, w, h, bg, a)
        
        self.dns_dict = {
            '192.168.0.1': 'http://我的手机.com',
            '192.168.0.2': 'http://我的电脑.com',
            '192.168.0.3': 'http://我的电脑2.com',
            '10.0.0.1': 'http://小花的手机.com',
            '192.168.0.4': 'http://我的d30.com',
            'http://我的手机.com': '192.168.0.1',
            'http://我的电脑.com': '192.168.0.2',
            'http://我的电脑2.com': '192.168.0.3',
            'http://小花的手机.com': '10.0.0.1',
            'http://我的d30.com': '192.168.0.4'
        }
        
        self.ip = None
        self.domain = None
    
    def draw(self):
        # 画出这个页面的分区
        self.frame = tk.Frame(width=self.width, height=self.height, background=self.backgroundColor)
        self.frame.place(x = self.posX, y = self.posY)
        
        
        t3 = tk.Label(master=self.frame, text='ip', background=self.backgroundColor)
        t3.place(x = 450, y = 10)
        self.ip = tk.Entry(master=self.frame, background=self.backgroundColor)
        self.ip.place(x = 500, y = 10)
        
        t4 = tk.Label(master=self.frame, text='域名', background=self.backgroundColor)
        t4.place(x = 450, y = 35)
        self.domain = tk.Entry(master=self.frame, background=self.backgroundColor)
        self.domain.place(x = 500, y = 35)
        
        t5 = tk.Button(
            master=self.frame, 
            text='添加规则', 
            highlightbackground=self.backgroundColor,
            command=self.add_rule)
        t5.place(x = 450, y = 70)
        
        start_pos_x = 10
        start_pos_y = 10
        
        for key in self.dns_dict:
            value = self.dns_dict[key]
            t = tk.Label(master=self.frame, text=key + ' -> ' + value, background=self.backgroundColor)
            t.place(x = start_pos_x, y = start_pos_y)
            
            start_pos_y += 25
            
    def add_rule(self):
        key = self.ip.get()
        value = self.domain.get()
        # 如果这个key已经存在，就覆盖掉
        # 否则新建一个
        self.dns_dict[key] = value
        
        self.draw()