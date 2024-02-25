"""
App : 
- Store all the states data
- Store reference to all the panels
- Help application to switch betweens panels

- Hosting main application window

"""

import tkinter as tk

from pages.AdjustPanel import AdjustPanel
from pages.EffectPanel import EffectPanel
from pages.CropPanel import CropPanel
from pages.LayerPanel import LayerPanel
from pages.MenuPanel import MenuPanel
from pages.Canvas import Canvas

from UIBase import Position


class App:
    def __init__(self):
        # main app window
        self.window = None
        self.current_file = ""
        self.lblImage = None
        self.o_img = None
        self.t_img = None

        # 保留一个叫canvas的物品
        self.current_image = None

        # 保留一个列表的layers，每一个layer都会保留一张图片，最后整个图片就是由全部的layer拼接在一起
        self.layer = []
        self.current_layer_index = -1

        self.current_panel = ""

        # all crop related variables
        self.selectAPressed = False
        self.selectBPressed = False
        self.positionA = Position()
        self.positionB = Position()
        self.canvas_click_position = Position()

        self.setup()

    def setup(self):
        self.window = tk.Tk()
        self.window.geometry("1400x900")
        self.window.bind("<Button-1>", self.handleMouseClick)

        # Frame : div
        self.canvas = Canvas(self, 1000, 800)
        self.canvas.setup(100, 0)

        self.adjust_panel = AdjustPanel(self, 300, 800)
        self.adjust_panel.setup(1100, 0)

        self.effect_panel = EffectPanel(self, 300, 800)
        # self.effect_panel.setup(1100, 0)

        self.crop_panel = CropPanel(self, 300, 800)
        # self.crop_panel.setup(1100, 0)

        self.menu_panel = MenuPanel(self, 100, 800)
        self.menu_panel.setup(0, 0)

        self.layer_panel = LayerPanel(self, 1400, 100)
        self.layer_panel.setup(0, 800)

    def run(self):
        self.window.mainloop()

    # function delegate
    def update_render(self):
        self.canvas.update_render()

    def update_layer(self):
        self.layer_panel.setup(0, 800)

    def switch(self, target):

        # if you are at adjust panel and you clicked adjust panel, do nothing
        if self.current_panel == target:
            return

        if self.current_panel == "adjust":
            self.adjust_panel.clear()
        elif self.current_panel == "effect":
            self.effect_panel.clear()
        elif self.current_panel == "crop":
            self.crop_panel.clear()

        if target == "adjust":
            self.adjust_panel.setup(1100, 0)
            self.current_panel = "adjust"
        elif target == "effect":
            self.effect_panel.setup(1100, 0)
            self.current_panel = "effect"
        elif target == "crop":
            self.crop_panel.setup(1100, 0)
            self.current_panel = "crop"

    def handleMouseClick(self, event):
        x = event.x
        y = event.y
        print(self.current_layer_index)
        if self.current_layer_index < 0:
            return

        self.canvas_click_position = Position(x, y)
        # if selecting A, set A position
        if self.selectAPressed:
            self.positionA = Position(x, y)
            self.selectAPressed = False

            layer = self.layer[self.current_layer_index]
            layer.crop_A_point = self.positionA

            self.update_render()

        # if selecting B, set B position
        if self.selectBPressed:
            self.positionB = Position(x, y)
            self.selectBPressed = False

            layer = self.layer[self.current_layer_index]
            layer.crop_B_point = self.positionB

            self.update_render()
