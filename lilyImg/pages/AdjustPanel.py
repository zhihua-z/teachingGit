"""
Adjust Panel : 
- draw some buttons

"""

import tkinter as tk
from UIBase import Position, ButtonGroupValInt, Panel
from tkinter.filedialog import askopenfilename, asksaveasfile, asksaveasfilename

from Layer import Layer
from PIL import Image


class AdjustPanel(Panel):
    def __init__(self, app, width, height):
        super().__init__(app, width, height)

    def setup(self, x, y):
        super().setup(x, y)
        self.frame = tk.Frame(width=self.width, height=self.height)
        self.frame.place(x=x, y=y)
        self.register(self.frame)

        t = tk.Button(master=self.frame, text="open file", command=self.open_a_file)
        t.place(x=10, y=30)
        self.register(t)

        t = tk.Button(master=self.frame, text="save file", command=self.save_a_file)
        t.place(x=100, y=30)
        self.register(t)

        self.brightness = ButtonGroupValInt(
            self.frame,
            "Brightness",
            "Adjust Brightness",
            Position(10, 70),
            self.adjust_brightness,
        )
        self.brightness.show()
        self.register(self.brightness)

        self.saturation = ButtonGroupValInt(
            self.frame,
            "Saturation",
            "Adjust Saturation",
            Position(10, 130),
            self.adjust_saturation,
        )
        self.saturation.show()
        self.register(self.saturation)

        self.vibrance = ButtonGroupValInt(
            self.frame,
            "Vibrance",
            "Adjust Vibrance",
            Position(10, 190),
            self.adjust_vibrance,
        )
        self.vibrance.show()
        self.register(self.vibrance)

    def open_a_file(self):
        self.app.current_file = askopenfilename()

        if self.app.current_file == "":
            return
        
        image = Image.open(self.app.current_file)

        # adjust image size if it is too large
        canvas_width = self.app.canvas.width
        canvas_height = self.app.canvas.height
        
        image_width = image.width
        image_height = image.height
        
        factor = 1
        
        # if image width > canvas width: 
        factor1 = image_width / canvas_width
        
        # if image height > canvas height
        factor2 = image_height / canvas_height
        
        
        if factor1 > 1 or factor2 > 1:
            # factor = factor1 if factor1 > factor2 else factor2
            factor = max(factor1, factor2)
            image = image.resize((image_width / factor, image_height / factor))

        l = Layer()
        l.image = image
        l.path = self.app.current_file
        
        l.name = "image" + str(len(self.app.layer))

        self.app.layer.append(l)
        self.app.current_layer_index = 0  # len(self.app.layer) - 1

        self.app.update_render()
        self.app.update_layer()

    def save_a_file(self):
        self.app.current_file = asksaveasfilename()
        self.app.current_image.save(self.app.current_file)

    def adjust_brightness(self):
        val = int(self.brightness.entry.get())

        l = self.app.layer[self.app.current_layer_index]

        l.brightness = val
        self.app.update_render()

    def adjust_saturation(self):
        val = int(self.saturation.entry.get())

        l = self.app.layer[self.app.current_layer_index]

        l.saturation = val
        self.app.update_render()

    def adjust_vibrance(self):
        val = int(self.vibrance.entry.get())

        l = self.app.layer[self.app.current_layer_index]

        l.vibrance = val
        self.app.update_render()