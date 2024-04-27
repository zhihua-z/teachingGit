import tkinter as tk
from PIL import Image, ImageTk
from Panel import Panel
from CYMath import Vector2

from Layer import Layer
from Mystring import find_last_of

from CYUI import CYLabel, CYButton
import styles

class LoginPage(Panel):
    def __init__(self, app, size: Vector2):
        super().__init__(app, size)
        self.titleFont = ('Sans-Serif' , 40 , 'bold')

    def setup(self, pos_x, pos_y):
        super().setup()
        self.master = tk.Frame(width=self.size.x, 
                           height=self.size.y, 
                           background=styles.app_background, 
                           highlightbackground=styles.app_background)
        self.master.place(x = pos_x, y = pos_y)
        self.register(self.master)

        self.title = tk.Label(master = self.master,
                               text = "Photo Editor",
                               font = self.titleFont, 
                               highlightbackground=styles.app_background, 
                               )
        self.title.place(x = 500, y = 50)

        # Username label and entry
        username_label = CYLabel(master=self.master, text="Username", position=(500, 200))
        self.register(username_label)
        self.username = tk.Entry(master=self.master, background=styles.light_text_color)
        self.username.place(x=600, y=200)
        self.register(self.username)

        # Password label and entry
        password_label = CYLabel(master=self.master, text="Password", position=(500, 250))
        self.register(password_label)
        self.password = tk.Entry(master=self.master, show="*", background=styles.light_text_color)
        self.password.place(x=600, y=250)
        self.register(self.password)

        # Login button
        login_button = CYButton(master=self.master, text="Login", position=(500, 300), command=self.login)
        self.register(login_button)

        # No account? Register button
        register_button = CYButton(master=self.master, text="No account? Register", position=(500, 350), command=self.show_register_page)
        self.register(register_button)
    
    def prompt_error(self):
        popup = tk.Toplevel(self.app.window)
        popup.title("Login failed")
        popup.geometry("200x100")
        
        label = tk.Label(popup, text="username / password incorrect")
        label.pack(pady=10)
        
        close_button = tk.Button(popup, text="Close", command=popup.destroy)
        close_button.pack()
    
    def login(self):
        username = self.username.get()
        password = self.password.get()
        
        print(username, password)
        
        auth = self.app.db.login(username, password)
        
        if auth:
            self.app.authenticated = True
            self.app.username = username
            self.app.setup_pages()
            
        else:
            self.prompt_error()
    
    def show_register_page(self):
        self.app.go_to_register_page = True
        self.app.setup_pages()