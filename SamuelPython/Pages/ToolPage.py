import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename


class ToolPage:
    
    def __init__(self, app):
        self.open_file_button = None
        self.right_panel_color = '#cccccc'
        self.app = app
    
    def draw(self):
        self.frame = tk.Frame(background=self.right_panel_color, width=200, height=700)
        self.frame.place(x=950, y=0)
        
        self.open_file_button = tk.Button(
            master=self.frame, 
            text='open file', 
            highlightbackground=self.right_panel_color,
            command=self.open_file)
        self.open_file_button.place(x = 10, y = 10)
    
    
    def open_file(self):
        self.app.current_filename = askopenfilename()
        
        f = open(self.app.current_filename, 'r')
        text = f.read()
        
        self.app.writeArea.content.delete("1.0", tk.END)
        self.app.writeArea.content.insert("1.0", text)
        
        label_new = tk.Label(master=self.app.contentPage.frame, text='新文档')
        label_new.place(x=5, y=5)