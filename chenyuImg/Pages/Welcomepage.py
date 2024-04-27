import tkinter as tk
from PIL import Image, ImageTk
from Panel import Panel
from CYMath import Vector2

from Layer import Layer
from Mystring import find_last_of



from CYUI import CYLabel, CYButton
import styles

class WelcomePage(Panel):
    
    def __init__(self, app, size: Vector2):
        super().__init__(app, size)
        self.titleFont = ('Sans-Serif' , 40 , 'bold')


    def setup(self, pos_x, pos_y):
        super().setup()
        
        self.frame = None

        self.clear()
        
        self.master = tk.Frame(width=self.size.x,
                               height=self.size.y,
                               background=styles.app_background,
                               highlightbackground=styles.app_background)
        self.master.place(x=pos_x, y=pos_y)
        self.register(self.master)

        self.title = tk.Label(master = self.master,
                               text = "Welcome, " + self.app.username,
                               font = self.titleFont, 
                               highlightbackground=styles.app_background, 
                               )
        self.title.place(x = 500, y = 50)

        currpos = 100
        # draw a new project button
        t = CYButton(master=self.master, text="New Project +", command=self.open_project, position=(700, currpos))
        self.register(t)
        currpos += 80
        
        projects = self.app.db.findProjectByUsername(self.app.username)

        if len(projects) == 0:
            return
        else:
            for p in projects:
                # this is actually running the open_project function when you draw the button
                #t = CYButton(master=self.master, text=p[1], command=self.open_project(p[0]), position=(700, currpos))
                
                # this is creating a lambda function object when you draw the button
                # the function will only run when you trigger the command
                t = CYButton(master=self.master, text=p[1], command=lambda x=p[0]: self.open_project(x), position=(700, currpos))
                self.register(t)
                currpos += 50
    
    
    def open_project(self, projectid):
        print(projectid)
        