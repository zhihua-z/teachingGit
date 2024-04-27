import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import process
from Panel import Panel
from CYMath import Vector2

from CYUI import CYLabel, CYButton
import styles

class CropPanel(Panel):
    def __init__(self, app, size: Vector2):
        super().__init__(app, size)

    def setup(self, pos_x, pos_y):
        super().setup()
        self.master = tk.Frame(width=self.size.x, 
                           height=self.size.y, 
                           background=styles.app_background, 
                           highlightbackground=styles.app_background)
        self.master.place(x = pos_x, y = pos_y)
        self.register(self.master)

        t = CYLabel(master=self.master, 
                 text='this is crop panel',
                 position=(5, 350))
        self.register(t)

        t = CYButton(master=self.master, 
                 text='Crop_A', 
                 command=self.on_crop_A_pressed,
                 position=(10, 230))
        self.register(t)

        t = CYButton(master=self.master, 
                 text='Crop_B', 
                 command=self.on_crop_B_pressed,
                 position=(70, 230))
        self.register(t)

        t = CYButton(master=self.master, 
                 text='Export', 
                 command=self.on_export_pressed,
                 position=(10, 270))
        self.register(t)

        t = CYButton(master=self.master, 
                 text='CancelCrop', 
                 command=self.on_cancelcrop_pressed,
                 position=(10, 310))
        self.register(t)

    def on_crop_A_pressed(self):
        self.app.on_selecting_A = True
        self.app.on_selecting_B = False

    def on_crop_B_pressed(self):
        self.app.on_selecting_A = False
        self.app.on_selecting_B = True
   
    def on_cancelcrop_pressed(self):
        self.app.on_selecting_A = False
        self.app.on_selecting_B = False
        self.app.crop_A_layer = None
        self.app.crop_B_layer = None
        self.app.A_pos = None
        self.app.B_pos = None
        self.app.update_render()

    def on_export_pressed(self):
        
        result_image = process.crop_image(self.app.current_image, self.app.A_pos, self.app.B_pos)

        export_path = asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if export_path:
            result_image.save(export_path)
            print(f"Image exported to: {export_path}")
 