# 导入tkinter并且重命名为tk
import tkinter as tk
import copy
from Page import Page
import styles

from UI import class图片按钮, class图片按钮2

from Modal import Modal对话框, modal新图层对话框

from tkinter import simpledialog
from tkinter import messagebox
from tkinter import colorchooser

# Page 它会控制当前页面应该画什么
class TucengPage(Page):
    def __init__(self, x, y, w, h, a):
        super().__init__(x, y, w, h, a)

        self.currPosition = 22

    def draw(self):
        # 画出这个页面的分区
        self.frame = tk.Frame(
            width=self.width, height=self.height, background=styles.菜单背景颜色
        )
        self.frame.place(x=self.posX, y=self.posY)
        self.register(self.frame)

        self.add = class图片按钮(
            self.frame,
            "img/add.png",
            (100, 50),
            "新图层",
            (18, self.currPosition),
            labelPos=(5, 55),
            command=self.fn新图层
        )
        self.register(self.add)
        self.currPosition += 80

        # 画出全部的图层
        for t in self.app.tuceng:
            daxiao = t.image.size
            self.临时图层按钮 = class图片按钮2(
                self.frame,
                t.image,
                (100, int(daxiao[1] / daxiao[0] * 100)),
                t.name,
                (18, self.currPosition),
                command=lambda tuceng=t: self.fn点击按钮(tuceng),
                labelPos=(5, int(daxiao[1] / daxiao[0] * 100) + 5),
                current=t.current,
                可见 = t.可见
            )
            
            self.临时图层按钮.button.bind("<Button-2>", lambda e, x = t:self.fn弹出右键菜单(e, x))
            
            self.register(self.临时图层按钮)
            self.currPosition += int(daxiao[1] / daxiao[0] * 100) + 30
    
    '''
    图层列表:[tuceng1, tuceng2, tuceng3]
                      ^

    图层列表:[tuceng1, tuceng3]
    
    '''
    def fn删除图层(self, 图层):
        
        图层index = None
        for i in range(len(self.app.tuceng)):
            if 图层 == self.app.tuceng[i]:
                图层index = i
        
        if 图层index is None:
            return
        
        self.app.tuceng = self.app.tuceng[0:图层index] + self.app.tuceng[图层index + 1:]
        
        self.fn重画()
        self.app.canvas.fn重画()

    def fn新图层(self):
        # 创建一个有两个图片按钮的对话框
        # 根据用户点击的对话框id，执行不同操作
        # 1. 创建一个新的全黑的照片图层
        # 2. 弹出一个文件选择对话框，让用户选择一个图片加载进来as 新图层
        dialog = modal新图层对话框(self.app.window)
        pass
        
    def fn复制图层(self, 图层):
        #先把当前图层和图层列表转化中文
        图层列表 = self.app.tuceng
        #由于如果用‘复制的图层= 当前图层’那么会双方影响，我问了GPT
        复制的图层 = copy.deepcopy(图层)  # 需要导入 copy 模块
        复制的图层.current = False
        图层列表.append(复制的图层)
        self.app.tucengPage.fn重画()
        self.app.canvas.fn重画()
      
    def fn设置图层可见(self, 图层):
        if 图层.可见:
            图层.可见 = False
        else:
            图层.可见 = True
            
        self.app.tucengPage.fn重画()
        self.app.canvas.fn重画()
            
        # 图层.可见 = False if 图层.可见 else True
        # 图层.可见 = 图层.可见 == False
            
    
    def fn弹出右键菜单(self, 事件, 图层):
        self.app.menu.destroy()
        self.app.menu = tk.Menu(master=self.app.window, tearoff=0)
        
        # 布置每个图层的菜单样式
        self.app.menu.add_command(label='在上面创建新图层')
        self.app.menu.add_command(label='在下面创建新图层')
        self.app.menu.add_command(label="复制", command=lambda x = 图层:self.fn复制图层(x))
        self.app.menu.add_separator()
        self.app.menu.add_command(label="删除", command=lambda x = 图层:self.fn删除图层(x))
        self.app.menu.add_command(label="可见/不可见", command=lambda x = 图层:self.fn设置图层可见(x))
        self.app.menu.add_command(label="重命名", command=lambda x = 图层:self.fn重命名(x))
        # 画出来
        self.app.menu.post(事件.x_root, 事件.y_root)
        
    # 点击按钮切换图层
    def fn点击按钮(self, t):
        for tuceng in self.app.tuceng:
            tuceng.current = False
        t.current = True
        self.app.currenttuceng = t
        self.app.tucengPage.fn重画()

    def fn重画(self):
        self.clear()
        self.currPosition = 22
        self.draw()
    
    def fn重命名(self,tuceng):
        # color_code = colorchooser.askcolor(title="选择颜色")
        # print(f"选择的颜色: {color_code}")
        #num = simpledialog.askinteger("输入数字", "输入数字prompt")
        #fl = simpledialog.askfloat('给一个小书', '输入小树prompt')
        
        dialog = Modal对话框(self.app.window, "重命名")
        
        if (dialog is None or len(dialog.result) != 0):
            tuceng.name = dialog.result
            self.app.currenttuceng = tuceng
            self.app.tucengPage.fn重画()

      

