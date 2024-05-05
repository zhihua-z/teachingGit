# 导入tkinter并且重命名为tk
import tkinter as tk
from PIL import Image, ImageTk
import styles

class ImageButton:
    
    def __init__(self, master, imagePath, size, text, position, command = None, labelPos = (5, 43)):
        self.img = Image.open(imagePath)    
        self.img = self.img.resize(size)
        
        buttonPosition = position
        labelPosition = (position[0] + labelPos[0], position[1] + labelPos[1])
        
        # 通过ImageTk把这张照片转换为tkinter可以使用的格式
        self.photoImage = ImageTk.PhotoImage(self.img)
        
        self.button = tk.Button(master=master, 
                      image=self.photoImage, 
                      highlightbackground=styles.menuBackgroundColor,
                      foreground=styles.foregroundColor,
                      command=command)
        self.button.place(x = buttonPosition[0], y = buttonPosition[1])
        
        self.label = tk.Label(master=master, 
                     text=text, 
                     background=styles.menuBackgroundColor,
                     foreground=styles.foregroundColor)
        self.label.place(x = labelPosition[0], y = labelPosition[1])

    def destroy(self):
        # delete / 删除
        del self.img
        del self.photoImage
        
        self.button.destroy()
        self.label.destroy()



class ImageButton2:
    def __init__(self, master, img, size, text, position, command = None, labelPos = (5, 43),current = False):
        self.img = img
        self.img = self.img.resize(size)
        self.current = current
        
        buttonPosition = position
        labelPosition = (position[0] + labelPos[0], position[1] + labelPos[1])
        
        
        # 通过ImageTk把这张照片转换为tkinter可以使用的格式
        self.photoImage = ImageTk.PhotoImage(self.img)
        color = styles.menuBackgroundColor
        if (current == True):
            color = 'red'
class ImageButton2:
    def __init__(self, master, img, size, text, position, command = None, labelPos = (5, 43),current = False):
        self.img = img
        self.img = self.img.resize(size)
        self.current = current
        
        buttonPosition = position
        labelPosition = (position[0] + labelPos[0], position[1] + labelPos[1])
        
        
        # 通过ImageTk把这张照片转换为tkinter可以使用的格式
        self.photoImage = ImageTk.PhotoImage(self.img)
        color = styles.menuBackgroundColor
        
        if (self.current == True):
            color = 'red'
class ImageButton2:
    def __init__(self, master, img, size, text, position, command = None, labelPos = (5, 43),current = False):
        self.img = img
        self.img = self.img.resize(size)
        self.current = current
        
        buttonPosition = position
        labelPosition = (position[0] + labelPos[0], position[1] + labelPos[1])
        
        
        # 通过ImageTk把这张照片转换为tkinter可以使用的格式
        self.photoImage = ImageTk.PhotoImage(self.img)

        color = styles.menuBackgroundColor
        
        if (self.current == True):
            color = 'red'

            

        #self.frame = tk.Frame(master, bd=2, relief="solid",background = color)  # bd 是边框宽度，relief 是边框样式  
           
        self.button = tk.Button(master=master, 
                      image=self.photoImage, 
                      highlightbackground=color,
                      foreground=styles.foregroundColor,
                      command=command)
        self.button.place(x = buttonPosition[0], y = buttonPosition[1])

        #self.frame.pack(pady=2, padx=2) # 添加一些内边距 

        self.label = tk.Label(master=master, 
                     text=text, 
                     background=color,
                     foreground=styles.foregroundColor)
        self.label.place(x = labelPosition[0], y = labelPosition[1])

    def destroy(self):
        # delete / 删除
        del self.img
        del self.photoImage
        
        
        self.button.destroy()
        self.label.destroy()
        #self.frame.destroy()