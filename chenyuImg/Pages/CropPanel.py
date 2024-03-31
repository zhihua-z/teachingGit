import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import process
from Panel import Panel
from CYMath import Vector2

class CropPanel(Panel):
    def __init__(self, app, size: Vector2, styles):
        super().__init__(app, size, styles)

    def setup(self, pos_x, pos_y):
        super().setup()

        self.master = tk.Frame(width=self.size.x, height=self.size.y)
        self.master.place(x = pos_x, y = pos_y)
        self.register(self.master)

        t = tk.Label(master=self.master, text='this is crop panel')
        t.place(x=0, y=350)
        self.register(t)

        self.btn_crop_A = tk.Button(master=self.master, text='Crop A', command=self.on_crop_A_pressed)
        self.btn_crop_A.place(x=10, y=230)
        self.btn_crop_B = tk.Button(master=self.master, text='Crop B', command=self.on_crop_B_pressed)
        self.btn_crop_B.place(x=70, y=230)
        self.btn_export = tk.Button(master=self.master, text='Export', command=self.on_export_pressed)
        self.btn_export.place(x=130, y=230)
        self.btn_cancelcrop = tk.Button(master=self.master, text='cancelcrop', command=self.on_cancelcrop_pressed)
        self.btn_cancelcrop.place(x=190, y=230)
        self.register(self.btn_crop_A)
        self.register(self.btn_crop_B)
        self.register(self.btn_cancelcrop)
        self.register(self.btn_export)

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
 