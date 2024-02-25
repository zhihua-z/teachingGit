"""
Canvas Panel : 
- draw a frame to render something
- redraw

"""

import tkinter as tk
from UIBase import Position, ButtonGroupValInt, Panel
from PIL import ImageTk


class Canvas(Panel):
    def __init__(self, app, width, height):
        super().__init__(app, width, height)
        self.width = width
        self.height = height

    def setup(self, x, y):
        super().setup(x, y)
        self.frame = tk.Frame(width=self.width, height=self.height, background="black")
        self.frame.place(x=x, y=y)
        self.register(self.frame)

        self.canvas = None

    def update_render(self):
        # 画板清空
        if self.canvas:
            self.canvas.destroy()

        if len(self.app.layer) == 0:
            return

        # 1. update all layers
        for l in self.app.layer:
            l.render()

        # 2. merge layers into one image
        final_image = self.app.layer[0].final_result

        self.app.current_image = final_image

        # 3. draw this final result on the screen
        self.photo_image = ImageTk.PhotoImage(final_image)
        self.canvas = tk.Label(master=self.frame, image=self.photo_image)
        self.canvas.image = self.photo_image
        self.canvas.place(x=0, y=0)
        self.register(self.canvas)
