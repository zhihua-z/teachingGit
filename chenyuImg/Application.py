import tkinter as tk
from PIL import Image, ImageTk
import process
from CYMath import Vector2
from Pages.AdjustPanel import AdjustPanel
from Pages.CropPanel import CropPanel
from Pages.EffectPanel import EffectPanel
from Pages.MenuPanel import MenuPanel
from Pages.LayerPanel import LayerPanel
from Pages.ToolsPanel import ToolsPanel
from Pages.LoginPage import LoginPage
from Pages.RegisterPage import RegisterPage
from Pages.Welcomepage import WelcomePage

from Layer import Layer

from DBtool import Database

class Application:
    def __init__(self):
        self.db = Database()
        
        self.filename = ''
        self.original_image = None
        self.current_image = None
        self.layer = []
        self.current_layer_index = None
        self.lblImage = None
        self.current_project_id = 0
        
        self.authenticated = False
        self.welgo = True
        self.go_to_register_page = False
        self.username = None
        
        self.crop_A_layer = None
        self.crop_B_layer = None
        self.on_selecting_A = False
        self.on_selecting_B = False
        self.A_pos = None
        self.B_pos = None
        
        self.click_pos = None
        
        self.control_down = False
        self.viewport_width = 0
        self.viewport_height = 0
        self.adjust_panel = AdjustPanel(self, Vector2(400, 600))
        self.effect_panel = EffectPanel(self, Vector2(400, 600))
        self.crop_panel = CropPanel(self, Vector2(400, 600))
        self.menu_panel = MenuPanel(self, Vector2(100, 600))
        self.layer_panel = LayerPanel(self, Vector2(1300, 120))
        self.toolsPanel = ToolsPanel(self, Vector2(1300, 50))
        self.loginPage = LoginPage(self, Vector2(1300, 770))
        self.registerPage = RegisterPage(self, Vector2(1300,770))
        self.welcomePage = WelcomePage(self, Vector2(1300,770))
        self.vp_list = []
        

    def register(self, frame, tkComp):
        if frame == self.viewport:
            self.vp_list.append(tkComp)

    def setup(self):
        self.window = tk.Tk()
        self.window.geometry('1300x770')
        
        self.setup_pages()
        
    def draw_login(self):
        self.loginPage.setup(0, 0)
    
    def draw_register(self):
        if self.loginPage is not None:
                self.loginPage.clear()
        self.registerPage.setup(0, 0)
    
    def draw_welcome(self):
        self.welcomePage.setup(0, 0)
    
    def draw_mainApp(self):
        if self.welcomePage is not None:
            self.welcomePage.clear()
        
        self.menu_panel.setup(0, 50)
        self.viewport = tk.Frame(width=800, height=600)
        self.viewport.place(x=100, y=50)
        self.viewport_width = 800
        self.viewport_height = 600

        self.window.bind("<Button-1>", self.handle_mouse_click)
        self.window.bind('<KeyPress>', self.key_press)
        self.window.bind('<KeyRelease>', self.key_released)

        self.toolsPanel.setup(0, 0)
        self.adjust_panel.setup(900, 50)
        self.layer_panel.setup(0, 650)

    def setup_pages(self):
        if self.authenticated: # 登录了
            if self.welgo:
                self.draw_welcome()
            else:
                self.draw_mainApp()
        else: # 没登录
            if self.go_to_register_page:
                self.draw_register()
            else:
                self.draw_login()
        


    def switch(self, panel_name):
        self.adjust_panel.clear()
        self.effect_panel.clear()
        self.crop_panel.clear()

        if panel_name == 'adjust_panel':
            self.adjust_panel.setup(900, 50)
        elif panel_name == 'effect_panel':
            self.effect_panel.setup(900, 50)
        elif panel_name == 'crop_panel':
            self.crop_panel.setup(900, 50)

    def key_press(self, event):
        print(event)

    def key_released(self, event):
        print(event)

    def update(self):
        self.window.mainloop()

    def update_render(self):
        # update and merge all layers
        #layer = self.layer[self.current_layer_index]
        #result_image = layer.render()
        
        images = []
        for layer in self.layer[::-1]:
          layer.render()
          images.append(layer.result_image)
          
        # merge

        
        result = process.composite_image(images, self.viewport_width, self.viewport_height)
        

        

        # if cropping add crop layer on top of the merged result
        if self.crop_A_layer is not None and self.crop_B_layer is not None:
            merged_crop_image = process.merge_crop(self.crop_A_layer.image, self.crop_B_layer.image)
            result = process.render_crop(result, merged_crop_image)
        elif self.crop_A_layer is not None:
            result = process.render_crop(result, self.crop_A_layer.image)
        elif self.crop_B_layer is not None:
            result = process.render_crop(result, self.crop_B_layer.image)

        # display final result
        self.render_image(result)

    def destroy_if_have(self, component):
        if len(self.filename) != 0 and component is not None:
            component.destroy()

    def render_image(self, image):
        if image is None:
            return
        
        self.destroy_if_have(self.lblImage)
        image1 = ImageTk.PhotoImage(image)
        self.lblImage = tk.Label(master=self.viewport, image=image1)
        self.lblImage.image = image1

        #mid_x_pos, mid_y_pos = 0, 0
        # if self.original_image.width > self.original_image.height:
        #     mid_y_pos = self.viewport_height / 2 - self.original_image.height / 2 - 1
        # else:
        #     mid_x_pos = self.viewport_width / 2 - self.original_image.width / 2 - 1

        self.lblImage.place(x=0, y=0)
        self.register(self.viewport, self.lblImage)

    def update_current_layer(self, id):
        self.current_layer_index = id

    def screen_position_to_image_position(self, screen_position):
        cx, cy = -3, -5
        return [screen_position[0] + cx, screen_position[1] + cy]

    def handle_mouse_click(self, event):
        
        self.click_pos = (event.x, event.y)
        
        if self.on_selecting_A:
            if self.current_layer_index is None:
                return
            self.on_selecting_A = False
            img_pos = self.screen_position_to_image_position((event.x, event.y))
            current_layer = self.layer[self.current_layer_index]
            self.crop_A_layer = Layer()
            self.crop_A_layer.image = process.create_crop_layer(current_layer.image, 'h', img_pos[1], 'A', True)
            self.crop_A_layer.image = process.create_crop_layer(self.crop_A_layer.image, 'v', img_pos[0], 'A', False)
            self.update_render()
            self.A_pos = img_pos
            
        elif self.on_selecting_B:
            if self.current_layer_index is None:
                return
            self.on_selecting_B = False
            img_pos = self.screen_position_to_image_position((event.x, event.y))
            current_layer = self.layer[self.current_layer_index]
            self.crop_B_layer = Layer()
            self.crop_B_layer.image = process.create_crop_layer(current_layer.image, 'h', img_pos[1], 'B', True)
            self.crop_B_layer.image = process.create_crop_layer(self.crop_B_layer.image, 'v', img_pos[0], 'B', False)
            self.update_render()
            self.B_pos = img_pos

    def export_cropped_image(self, export_path):
        if self.crop_A_layer is not None:
            cropped_image = self.crop_A_layer.image
        elif self.crop_B_layer is not None:
            cropped_image = self.crop_B_layer.image
        else:
            return

        cropped_image.save(export_path)
        print(f"Image exported to: {export_path}")
