# 导入tkinter并且重命名为tk
import tkinter as tk
from PIL import Image, ImageTk
from Page import Page
import styles

from tkinter.filedialog import askopenfilename, asksaveasfilename

from UI import class图片按钮, class调整按钮, class功能按钮
from Tuceng import Tuceng
from process import liangdu, baohedu

from MyImage import MyImage


# Page 它会控制当前页面应该画什么
class 调整页面(Page):
    def __init__(self, x, y, w, h, a):
        super().__init__(x, y, w, h, a)

    def draw(self):
        # 画出这个页面的分区
        self.frame = tk.Frame(
            width=self.width, height=self.height, background=styles.菜单背景颜色
        )
        self.frame.place(x=self.posX, y=self.posY)
        self.register(self.frame)

        self.label = tk.Label(master=self.frame, text="调整")
        self.label.place(x=0, y=0)
        self.register(self.label)


# Page 它会控制当前页面应该画什么
class 图层页面(Page):
    def __init__(self, x, y, w, h, a):
        super().__init__(x, y, w, h, a)

    def draw(self):
        # 画出这个页面的分区
        self.frame = tk.Frame(
            width=self.width, height=self.height, background=styles.菜单背景颜色
        )
        self.frame.place(x=self.posX, y=self.posY)
        self.register(self.frame)

        self.label = tk.Label(master=self.frame, text="图层")
        self.label.place(x=0, y=0)
        self.register(self.label)

        # 亮度
        self.btn亮度 = class调整按钮(
            master=self.frame,
            text='调整亮度',
            labelText='亮度',
            position=((0, 40)),
            command=self.fn调整亮度
        )        
        
        # 饱和度
        self.btn饱和度 = class调整按钮(
            master=self.frame,
            text='调整饱和度',
            labelText='饱和度',
            position=((0, 120)),
            command=self.fn调整饱和度
        )    
        
        # 透明度
        self.btn透明度 = class调整按钮(
            master=self.frame,
            text='调整透明度',
            labelText='透明度',
            position=((0, 200)),
            command=self.fn调整透明度
        )  
        
    # 调整亮度
    # 1.获取当前图层的照片
    # 2.呼叫process里面的liangdu函数
    # 3.返回一张调整过的照片
    # 4.替换当前图层的照片
    # 5。刷新画板

    def fn调整亮度(self):
        
        if self.app.currenttuceng is None:
            print("没有选中图层")
            return
        
        self.app.currenttuceng.亮度 = int(self.btn亮度.entry.get())

        self.app.canvas.fn重画()
    
    def fn调整饱和度(self):
        
        if self.app.currenttuceng is None:
            print("没有选中图层")
            return

        self.app.currenttuceng.饱和度 = float(self.btn饱和度.entry.get())
        
        self.app.canvas.fn重画()
        
    
    def fn调整透明度(self):
        
        if self.app.currenttuceng is None:
            print("没有选中图层")
            return
        
        self.app.currenttuceng.透明度 = float(self.btn透明度.entry.get())

        self.app.canvas.fn重画()


# Page 它会控制当前页面应该画什么
class 功能页面(Page): # pg功能页面
    def __init__(self, x, y, w, h, a):
        super().__init__(x, y, w, h, a)

    def draw(self):
        # 画出这个页面的分区
        self.frame = tk.Frame(
            width=self.width, height=self.height, background=styles.菜单背景颜色
        )
        self.frame.place(x=self.posX, y=self.posY)
        self.register(self.frame)

        # 打开图片
        t = class功能按钮(
            master=self.frame,
            text='打开图片',
            position=((5, 5)),
            command=self.openImage
        )
        self.register(t)
        
        # 导入图片
        t = class功能按钮(
            master=self.frame,
            text='导入图片',
            position=((5, 35)),
            command=self.importImage
        )
        self.register(t)
        
        # 提升图层
        t = class功能按钮(
            master=self.frame,
            text='提升图层',
            position=((5, 65)),
            command=self.fn提升图层
        )
        self.register(t)
        
        
        # 降低图层
        t = class功能按钮(
            master=self.frame,
            text='降低图层',
            position=((5, 95)),
            command=self.fn降低图层
        )
        self.register(t)
        

    """
    图层列表: [tuceng1, tuceng2, tuceng3]  
              0        1        2
    提升tuceng2:
    图层列表: [tuceng2, tuceng1, tuceng3] 
              1        0        2 
    """
    def fn提升图层(self):
        
        当前图层 = self.app.currenttuceng
        图层列表 = self.app.tuceng
        
        for i in range(1, len(图层列表)):
            if 图层列表[i] == 当前图层:
                临时变量 = 图层列表[i]
                图层列表[i] = 图层列表[i - 1]
                图层列表[i - 1] = 临时变量
                break
        
        self.app.tucengPage.fn重画()
        self.app.canvas.fn重画()
        
        
    """
    
    图层列表: [tuceng1, tuceng2, tuceng3]  
              0        1        2
    """
    def fn降低图层(self):
                
        当前图层 = self.app.currenttuceng
        图层列表 = self.app.tuceng
        
        for i in range(0, len(图层列表) - 1):
            if 图层列表[i] == 当前图层:
                临时变量 = 图层列表[i]
                图层列表[i] = 图层列表[i + 1]
                图层列表[i + 1] = 临时变量
                break
        
        self.app.tucengPage.fn重画()
        self.app.canvas.fn重画()

    def openImage(self):
        # 打开新图片的时候，先清除所有当前图层
        self.app.tuceng.clear()

        filename = askopenfilename()

        # 打开一张照片
        img = Image.open(filename)

        img_size = img.size
        canvas_size = (self.app.canvas.width, self.app.canvas.height)
        # canvas是画板  width是宽height是高度length是长度
        border_size = (60, 60)
        # border是框
        canvas_size = (canvas_size[0] - border_size[0], canvas_size[1] - border_size[1])

        factor_x = img_size[0] / canvas_size[0]
        factor_y = img_size[1] / canvas_size[1]

        new_size = img_size

        if factor_x > factor_y:
            if factor_x > 1:
                # 调整宽度
                new_size = (int(img_size[0] / factor_x), int(img_size[1] / factor_x))
        else:
            if factor_y > 1:
                # 高度超标
                new_size = (int(img_size[0] / factor_y), int(img_size[1] / factor_y))

        img = img.resize(new_size)
        # 调整

        # 计算居中位置s
        img_size = img.size
        # 重新获取照片的大小
        canvas_size = (self.app.canvas.width, self.app.canvas.height)
        # 是图片居中，挪移
        mov_x = (canvas_size[0] - img_size[0]) // 2
        mov_y = (canvas_size[1] - img_size[1]) // 2

        # position 位置
        pos = 0
        for i in range(len(filename)):
            if filename[i] == "/":
                pos = i
        tucengName = filename[pos + 1 :]

        myImage = MyImage(image=img, filename=filename)

        t = Tuceng(
            name=tucengName, img=img, x=mov_x, y=mov_y, myImage=myImage, current=False
        )

        self.app.tuceng.append(t)

        self.app.canvas.fn重画()
        self.app.tucengPage.fn重画()

    def importImage(self):
        filename = askopenfilename()

        # 打开一张照片
        img = Image.open(filename)
        
        # 转换为RGBA色彩空间
        if img.mode == 'RGB':
            img = img.convert('RGBA')
            
            # 创建一个透明度通道给他
            alphaChannel = Image.new("L", img.size, 255)
            img.putalpha(alphaChannel)

        img_size = img.size
        canvas_size = (self.app.canvas.width, self.app.canvas.height)

        # border_size = (60, 60)
        # canvas_size = (canvas_size[0] - border_size[0], canvas_size[1] - border_size[1])

        factor_x = img_size[0] / canvas_size[0]
        factor_y = img_size[1] / canvas_size[1]

        new_size = img_size

        if factor_x > 1 or factor_y > 1:
            if factor_x > factor_y:
                # 调整宽度
                new_size = (int(img_size[0] / factor_x), int(img_size[1] / factor_x))
            else:
                # 高度超标
                new_size = (int(img_size[0] / factor_y), int(img_size[1] / factor_y))

        img = img.resize(new_size)

        # 计算居中位置s
        img_size = img.size
        canvas_size = (self.app.canvas.width, self.app.canvas.height)

        mov_x = (canvas_size[0] - img_size[0]) // 2
        mov_y = (canvas_size[1] - img_size[1]) // 2

        pos = 0
        for i in range(len(filename)):
            if filename[i] == "/":
                pos = i
        tucengName = filename[pos + 1 :]
        myImage = MyImage(image=img, filename=filename)

        t = Tuceng(
            name=tucengName, img=img, x=mov_x, y=mov_y, myImage=myImage, current=False
        )

        self.app.tuceng = [t] + self.app.tuceng

        self.app.canvas.fn重画()
        self.app.tucengPage.fn重画()
