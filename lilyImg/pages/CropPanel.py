"""
Crop Panel : 
- draw some buttons


find point A
find point B

extract pixels inside and form a new image
- give select A select B some function to select points using mouse
  - press select A
  - press on the screen for position A
  
  - press select B
  - press on the screen for position B
  
- add a function in process.py to make a new image from the selection
  - able to render a mask
  - add a mask to that image layer

- save it

"""

import tkinter as tk
from UIBase import Position, ButtonGroupValInt, Panel
from tkinter.filedialog import askopenfilename, asksaveasfile, asksaveasfilename

from Layer import Layer


class CropPanel(Panel):
    def __init__(self, app, width, height):
        super().__init__(app, width, height)

    def setup(self, x, y):
        super().setup(x, y)
        self.frame = tk.Frame(width=self.width, height=self.height)
        self.frame.place(x=x, y=y)
        self.register(self.frame)

        t = tk.Button(master=self.frame, text="select A", command=self.handleSelectA)
        t.place(x=10, y=30)
        self.register(t)

        t = tk.Button(master=self.frame, text="select B", command=self.handleSelectB)
        t.place(x=10, y=90)
        self.register(t)

    def handleSelectA(self):
        self.app.selectAPressed = True
        self.app.selectBPressed = False

    def handleSelectB(self):
        self.app.selectAPressed = False
        self.app.selectBPressed = True
