from PIL import Image, ImageTk
import tkinter as tk


class ImageButton:
    
    # input: file location, (size: tuple), (position: tuple)
    def __init__(self, master, filename, size, position, command):
        self.filename = filename
        self.size = size
        self.width = size[0]
        self.height = size[1]
        self.position = position
        self.command = command
        
        self.image = None
        self.photoImage = None
        self.component = None
        
        # open this image using Pillow Image
        self.image = Image.open(filename).resize(size)
        
        # convert this image into PhotoImage for it to be used in TK
        self.photoImage = ImageTk.PhotoImage(self.image)
        
        self.component = tk.Button(master=master, 
                                   image=self.photoImage, 
                                   width=size[0], 
                                   height=size[1], 
                                   command=command)
        
        self.component.image = self.photoImage
        self.component.place(x=position[0], y=position[1])
        
        # self.label = tk.Label(..lxlkxl)
        # self.label.place(x=position[0], y = position[1] + 20)
        
    def destroy(self):
        self.component.destroy()
        del self.image
        del self.photoImage
        
        self.image = None
        self.photoImage = None
        self.component = None