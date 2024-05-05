import tkinter as tk

from Page import Page
from UI.ImageButton import ImageButton, Button, Label

import Styles

class LoginPage(Page):
    
    def __init__(self, app):

        super().__init__(app)
        
        self.frame = None
        self.message = None

        self.titleFont = ('Sans-Serif' , 60 , 'bold')
        self.textFont = ('Times New Roman', 18)
        
    def draw(self):
        self.clear()
        
        self.frame = tk.Frame(width = 1250, 
                              height = 750, 
                              background=Styles.backgroundColor)
        self.frame.place(x = 0, y = 0)
        self.register(self.frame)

        self.title = Label(
            master = self.frame, 
            text = "Online Text Editor", 
            font = self.titleFont, 
            position = ((375, 250))
        )

        self.usernameText = Label(
            master = self.frame, 
            text = "Username: ", 
            font = self.textFont, 
            position = ((450, 400))
        )

        self.username = tk.Entry(master=self.frame)
        self.username.place(x = 550, y = 400)

        self.passwordText = Label(
            master = self.frame, 
            text = "Password: ", 
            font = self.textFont, 
            position = ((455, 450))
        )

        self.password = tk.Entry(master=self.frame, show="*")
        self.password.place(x = 550, y = 450)
        
        t = tk.Button(master=self.frame,
                      text="Register",
                      command=self.registerUser,
                      highlightbackground=Styles.backgroundColor)
        t.place(x = 550, y = 500)
        
        t = tk.Button(master=self.frame,
                      text="Login",
                      command=self.login,
                      highlightbackground=Styles.backgroundColor)
        t.place(x = 655, y = 500)

    def registerUser(self):
        
        username = self.username.get()
        password = self.password.get()
        
        # ensure no such user exist
        result = self.app.db.retrieveUserByUsername(self.username)
        
        if len(result) != 0:
            if self.message is not None:
                self.message.destroy()
                
            self.message = tk.Label(master=self.frame, 
                                    text="user already exists", 
                                    foreground='red',
                                    background=Styles.backgroundColor)
            self.message.place(x = 550, y = 480)
            return
        
        # insert into db
        self.app.db.saveUser(username, password)
    
        # return successful registration
        if self.message is not None:
            self.message.destroy()
            
        self.message = tk.Label(master=self.frame, 
                                text="successfully registered user", 
                                foreground='green',
                                background=Styles.backgroundColor)
        self.message.place(x = 550, y = 480)

    def login(self):
        username = self.username.get()
        password = self.password.get()
        
        # find such user record
        result = self.app.db.retrieveUserByUsername(username)
        
        if len(result) == 0:
            if self.message is not None:
                self.message.destroy()
                
            self.message = tk.Label(master=self.frame, 
                                    text="user does not exist", 
                                    foreground='red',
                                    background=Styles.backgroundColor)
            self.message.place(x = 550, y = 480)
            return
        
        # verify password
        result = self.app.db.verifyPassword(username, password)
        
        if len(result) == 0:
            if self.message is not None:
                self.message.destroy()
                
            self.message = tk.Label(master=self.frame, 
                                    text="wrong password", 
                                    foreground='red',
                                    background=Styles.backgroundColor)
            self.message.place(x = 550, y = 480)
            return

        # login successfully
        self.app.loggedin = True
        self.app.username = username
        self.app.userid = result[0][0]
        self.app.draw()