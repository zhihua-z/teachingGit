# 导入tkinter并且重命名为tk
import tkinter as tk
from PIL import Image, ImageTk
import styles

class ImageButton:
    
    def __init__(self, master, imagePath, size, text, position, labelPos = (5, 43)):
        self.img = Image.open(imagePath)    
        self.img = self.img.resize(size)
        
        buttonPosition = position
        labelPosition = (position[0] + labelPos[0], position[1] + labelPos[1])
        
        # 通过ImageTk把这张照片转换为tkinter可以使用的格式
        self.photoImage = ImageTk.PhotoImage(self.img)
        
        self.button = tk.Button(master=master, 
                      image=self.photoImage, 
                      highlightbackground=styles.menuBackgroundColor,
                      foreground=styles.foregroundColor)
        self.button.place(x = buttonPosition[0], y = buttonPosition[1])
        
        self.label = tk.Label(master=master, 
                     text=text, 
                     background=styles.menuBackgroundColor,
                     foreground=styles.foregroundColor)
        self.label.place(x = labelPosition[0], y = labelPosition[1])
