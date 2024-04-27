import tkinter as tk
from PIL import Image, ImageTk
from Panel import Panel
from CYMath import Vector2

from Layer import Layer
from Mystring import find_last_of

from CYUI import CYLabel, CYButton
import styles

class RegisterPage(Panel):
     def __init__(self, app, size: Vector2):
        super().__init__(app, size)

        self.titleFont = ('Sans-Serif' , 40 , 'bold')
        
     def setup(self, pos_x, pos_y):
        super().setup()
        self.register_page = tk.Frame(width=self.size.x,
                                   height=self.size.y,
                                   background=styles.app_background,
                                   highlightbackground=styles.app_background)
        self.register_page.place(x=0, y=0)  

        self.title = tk.Label(master = self.frame,
                               text = "photo editor",
                               font = self.titleFont, 
                               highlightbackground=styles.app_background, 
                               )
        self.title.place(x = 350, y = 200)

        username_label = CYLabel(master=self.master, text="Username", position=(500, 200))
        self.register(username_label)
        self.username = tk.Entry(master=self.master, background=styles.light_text_color)
        self.username.place(x=600, y=200)
        self.register(self.username)


        Determine_password_button = CYButton(master=self.master, text="determine_password", position=(500, 300), command=self.determine_password)
        self.register(Determine_password_button)
        self.password = tk.Entry(master=self.master, show="*", background=styles.light_text_color)
        self.password.place(x=600, y=250)
        self.register(self.password)

        register_button = CYButton(master=self.master, text="back", position=(500, 380), command=self.show_login_page)
        self.register(register_button)
        
     def determine_password(self):
        username = self.username.get()
        password = self.password.get()
        
        querystr1 = '''
        select id from user
        where name = ?
        '''
        result = self.app.cursor.execute(querystr1, (username,)).fetchall()
        
        if len(result) != 0:
            if self.message is not None:
                self.message.destroy()
                
            self.message = tk.Label(master=self.frame, 
                                    text="user already exists", 
                                    foreground='red',
                                    background=styles.app_background)
            self.message.place(x = 500, y = 230)
            return
        
        querystr = '''
        insert into user (name, password)
        values (?, ?)
        '''
        self.app.cursor.execute(querystr, (username, password))
        self.app.connection.commit()

        if self.message is not None:
            self.message.destroy()
            
        self.message = tk.Label(master=self.frame, 
                                text="successfully registered user", 
                                foreground='green',
                                background=styles.app_background)
        self.message.place(x = 500, y = 330)

     def show_login_page(self):
        self.signin == True
