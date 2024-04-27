import tkinter as tk

from Page import Page

import Styles

class LoginPage(Page):
    
    def __init__(self, app):

        super().__init__(app)
        
        self.frame = None
        self.message = None

        self.titleFont = ('Sans-Serif' , 60 , 'bold')
        
    def draw(self):
        self.clear()
        
        self.frame = tk.Frame(width = 1250, 
                              height = 750, 
                              background=Styles.backgroundColor)
        self.frame.place(x = 0, y = 0)
        self.register(self.frame)

        self.title = tk.Label(master = self.frame,
                               text = "Online  Text  Editor",
                               font = self.titleFont, 
                               highlightbackground=Styles.backgroundColor, 
                               )
        self.title.place(x = 350, y = 200)

        self.usernameText = tk.Label(master = self.frame,
                                     text = "Username: ",
                                     highlightbackground = Styles.backgroundColor)
        self.usernameText.place(x = 450, y = 400)

        self.username = tk.Entry(master=self.frame)
        self.username.place(x = 550, y = 400)
        
        self.passwordText = tk.Label(master = self.frame,
                                     text = "Password: ",
                                     highlightbackground = Styles.backgroundColor)
        self.passwordText.place(x = 450, y = 450)

        self.password = tk.Entry(master=self.frame, show="*")
        self.password.place(x = 550, y = 450)
        
        t = tk.Button(master=self.frame,
                      text="register",
                      command=self.registerUser,
                      highlightbackground=Styles.backgroundColor)
        t.place(x = 550, y = 500)
        
        t = tk.Button(master=self.frame,
                      text="login",
                      command=self.login,
                      highlightbackground=Styles.backgroundColor)
        t.place(x = 650, y = 500)

    def registerUser(self):
        
        username = self.username.get()
        password = self.password.get()
        
        # ensure no such user exist
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
                                    background=Styles.backgroundColor)
            self.message.place(x = 550, y = 480)
            return
        
        # insert into db
        querystr = '''
        insert into user (name, password)
        values (?, ?)
        '''
        self.app.cursor.execute(querystr, (username, password))
        self.app.connection.commit()
    
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
        querystr1 = '''
        select id from user
        where name = ?
        '''
        result = self.app.cursor.execute(querystr1, (username,)).fetchall()
        
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
        querystr2 = '''
        select id from user
        where name = ? and password = ?
        '''
        result = self.app.cursor.execute(querystr2, (username, password)).fetchall()
        
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