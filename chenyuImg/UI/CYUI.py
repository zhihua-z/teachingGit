import tkinter as tk
from PIL import Image
from PIL import ImageTk

class CYButton:
    def __init__(self, master, text, styles, command, position):
        self.btn = tk.Button(master = master, 
                                text=text, 
                                command=command,
                                highlightbackground=styles.app_background)
        self.btn.place(x = position[0], y = position[1])
        
    
    def destroy(self):
        self.btn.destroy()
        del self.btn

class CYImageButton:
    def __init__(self, master, image_path, label, size, styles, command, position):
            
        self.img = Image.open(image_path)
        self.img = self.img.resize(size)
        
        self.photoImage = ImageTk.PhotoImage(self.img)
        
        self.btn = tk.Button(master = master, 
                                image=self.photoImage, 
                                command=command,
                                highlightbackground=styles.app_background)
        self.btn.image = self.photoImage
        self.btn.place(x = position[0], y = position[1])
        
        text_position = (position[0], position[1] + 45)
        self.label = tk.Label(master, 
                                        text=label, 
                                        background=styles.app_background, 
                                        foreground=styles.light_text_color)
        self.label.place(x = text_position[0], y = text_position[1])
    
    def destroy(self):
        del self.img
        del self.photoImage
        
        self.btn.destroy()
        self.label.destroy()
        
        del self.btn
        del self.label
        

class CYLabel:
    def __init__(self, master, text, styles, position):
        self.label = tk.Label(master, 
                                text=text, 
                                background=styles.app_background, 
                                foreground=styles.light_text_color)
        self.label.place(x = position[0], y = position[1])
    
    def destroy(self):
        self.label.destroy()
        del self.label