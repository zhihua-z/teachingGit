# 导入tkinter并且重命名为tk
import tkinter as tk
from PIL import Image, ImageTk
import styles
import copy
import process

class class图片按钮:
    
    def __init__(self, master, imagePath, size, text, position, command = None, labelPos = (5, 43)):
        self.img = Image.open(imagePath)    
        self.img = self.img.resize(size)
        
        buttonPosition = position
        labelPosition = (position[0] + labelPos[0], position[1] + labelPos[1])
        
        # 通过ImageTk把这张照片转换为tkinter可以使用的格式
        self.photoImage = ImageTk.PhotoImage(self.img)
        
        self.button = tk.Button(master=master, 
                      image=self.photoImage, 
                      highlightbackground=styles.菜单背景颜色,
                      foreground=styles.前景颜色,
                      command=command)
        self.button.place(x = buttonPosition[0], y = buttonPosition[1])
        
        self.label = tk.Label(master=master, 
                     text=text, 
                     background=styles.菜单背景颜色,
                     foreground=styles.前景颜色)
        self.label.place(x = labelPosition[0], y = labelPosition[1])

    def destroy(self):
        # delete / 删除
        del self.img
        del self.photoImage
        
        self.button.destroy()
        self.label.destroy()


class class图片按钮2:
    def __init__(self, master, img, size, text, position, command = None, labelPos = (5, 43),current = False, 可见 = True):
        self.img = copy.deepcopy(img)
        self.img = self.img.resize(size)
        self.current = current
        
        buttonPosition = position
        labelPosition = (position[0] + labelPos[0], position[1] + labelPos[1])
        
        if 可见 == False:
            self.img = process.liangdu(self.img, -100)
        
        # 通过ImageTk把这张照片转换为tkinter可以使用的格式
        self.photoImage = ImageTk.PhotoImage(self.img)

        color = styles.菜单背景颜色
        
        if (self.current == True):
            color = 'red'

        

        #self.frame = tk.Frame(master, bd=2, relief="solid",background = color)  # bd 是边框宽度，relief 是边框样式  
           
        self.button = tk.Button(master=master, 
                      image=self.photoImage, 
                      highlightbackground=color,
                      foreground=styles.前景颜色,
                      command=command)
        self.button.place(x = buttonPosition[0], y = buttonPosition[1])

        #self.frame.pack(pady=2, padx=2) # 添加一些内边距 

        self.label = tk.Label(master=master, 
                     text=text, 
                     background=color,
                     foreground=styles.前景颜色)
        self.label.place(x = labelPosition[0], y = labelPosition[1])

    def destroy(self):
        # delete / 删除
        del self.img
        del self.photoImage
        
        
        self.button.destroy()
        self.label.destroy()
        #self.frame.destroy()

class class调整按钮:
    def __init__(self, master, text, labelText, position, command = None,):
        self.button = None
        self.label = None
        self.entry = None
        
        self.label = tk.Label(
            master=master, 
            text=labelText,
            background=styles.菜单背景颜色,
            foreground=styles.前景颜色
        )
        self.label.place(x = position[0], y = position[1])
        
        self.entry = tk.Entry(master=master, width=5)
        self.entry.place(x = position[0] + 60, y = position[1])
        
        self.button = tk.Button(
            master=master, 
            text=text, 
            highlightbackground=styles.菜单背景颜色,
            command=command
        )
        self.button.place(x = position[0], y = position[1] + 30)
        
    def destroy(self):
        self.button.destroy()
        self.label.destroy()
        self.entry.destroy()
        
        

class class功能按钮:
    def __init__(self, master, text, position, command = None,):
        self.button = None
        
        self.button = tk.Button(
            master=master, 
            text=text, 
            highlightbackground=styles.菜单背景颜色,
            command=command
        )
        self.button.place(x = position[0], y = position[1])
        
    def destroy(self):
        self.button.destroy()
        
        
