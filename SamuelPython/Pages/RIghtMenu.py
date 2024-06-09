import tkinter as tk

from Page import Page

class RightMenu(Page):
    
    def __init__(self, app):
        super().__init__(app)
        
        self.frame = None
        
    def draw(self):
        self.clear()
        
        self.menu = tk.Menu(self.app.window, tearoff = 0) 
        self.menu.add_command(label = "New Chapter") 
    
    def popup(self, event):
        print(event)
        # 计算出点了哪个东西，然后把这个东西保存在程序里
        try: 
            self.menu.tk_popup(event.x_root, event.y_root) 
        finally: 
            self.menu.grab_release() 
     
    
    