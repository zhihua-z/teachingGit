from PIL import Image, ImageTk
import tkinter as tk

import Styles

class ImageButton:
    
    # input: file location, (size: tuple), (position: tuple)
    def __init__(self, master, filename, size, position, command, text):
        self.filename = filename
        self.size = size
        self.width = size[0]
        self.height = size[1]
        self.position = position
        self.command = command
        self.text = text 
    
        self.image = None
        self.photoImage = None
        self.component = None
        self.label = None
        
        # open this image using Pillow Image
        self.image = Image.open(filename).resize(size)
        
        # convert this image into PhotoImage for it to be used in TK
        self.photoImage = ImageTk.PhotoImage(self.image)
        
        self.component = tk.Button( master = master, 
                                    image =self.photoImage, 
                                    width = size[0], 
                                    height = size[1], 
                                    command =command, 
                                    text = text, 
                                    background=Styles.backgroundColor,
                                    highlightbackground=Styles.backgroundColor,
                                    foreground=Styles.foregroundColor
                                   )
        
        self.component.image = self.photoImage
        self.component.place(x=position[0], y=position[1])

        self.label = tk.Label(
            master = master, 
            text = text, 
            background=Styles.backgroundColor,
            highlightbackground=Styles.backgroundColor,
            foreground=Styles.foregroundColor
        )
        self.label.place(x = position[0], y = position[1] + 35)
        
    def destroy(self):
        self.component.destroy()
        self.label.destroy()
        del self.image
        del self.photoImage
        
        self.image = None
        self.photoImage = None
        self.component = None
        self.label = None

class Label:
    
    # input: file location, (size: tuple), (position: tuple)
    def __init__(self, master, position, text):
        self.position = position
        self.text = text 
    
        self.label = None
        
        self.label = tk.Label(
            master = master, 
            text = text, 
            background=Styles.backgroundColor,
            highlightbackground=Styles.backgroundColor,
            foreground=Styles.foregroundColor
        )
        self.label.place(x = position[0], y = position[1])
        
    def destroy(self):
        self.label.destroy()
        self.label = None