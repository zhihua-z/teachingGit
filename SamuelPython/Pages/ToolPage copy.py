import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from Page import Page

class ToolPage(Page):
    
    def __init__(self, app):
        self.open_file_button = None
        self.right_panel_color = '#cccccc'
        self.app = app
    
    def draw(self):
        self.frame = tk.Frame(background=self.right_panel_color, width=400, height=700)
        self.frame.place(x=950, y=0)
        
        self.open_file_button = tk.Button(
            master=self.frame, 
            text='open file', 
            highlightbackground=self.right_panel_color,
            command=self.open_file, 
            )
        self.open_file_button.place(x = 10, y = 10)
        # self.register(self.open_file_button)

        self.save_file_button = tk.Button(
            master = self.frame,
            text = "save file",
            highlightbackground = self.right_panel_color,
            command = self.save_file, 
        )
        self.save_file_button.place(x = 110, y = 10)
        # self.register(self.save_file_button)

        self.font_panel = tk.Label(
            master = self.frame,
            text = 'Font', 
            highlightbackground = self.right_panel_color, 
        )
        self.font_panel.place(x=10, y=60)
        # self.register(self.font_panel)

        self.font_type = tk.Button(
            master = self.frame,
            text = 'Font type', 
            highlightbackground = self.right_panel_color, 
        )
        self.font_type.place(x = 10, y=100)
        # self.register(self.font_type)

        self.font_size = tk.Button(
            master = self.frame,
            text = 'Font size',
            highlightbackground = self.right_panel_color, 
        )
        self.font_size.place(x=110, y=100)
        # self.register(self.font_size)

        self.bold_text = tk.Button(
            master = self.frame, 
            text = "B", 
            highlightbackground = self.right_panel_color,
        )
        self.bold_text.place(x=10, y = 150)
        # self.register(self.bold_text)

        self.italic_text = tk.Button(
            master = self.frame, 
            text = "I", 
            highlightbackground = self.right_panel_color,
        )
        self.italic_text.place(x=60, y = 150)
        # self.register(self.italic_text)

        self.underline_text = tk.Button(
            master = self.frame, 
            text = "U", 
            highlightbackground = self.right_panel_color,
        )
        self.underline_text.place(x=110, y = 150)
        # self.register(self.underline_text)

        self.text_color = tk.Button(
            master = self.frame,
            text = 'Text color', 
            highlightbackground = self.right_panel_color, 
        )
        self.text_color.place(x = 10, y=200)
        # self.register(self.text_color)

        self.highlight_text = tk.Button(
            master = self.frame,
            text = "Highlight color",
            highlightbackground = self.right_panel_color,
        )
        self.highlight_text.place(x=110, y = 200)
        # self.register(self.highlight_text)

        self.align_panel = tk.Label(
            master = self.frame,
            text = 'Align', 
            highlightbackground = self.right_panel_color, 
        )
        self.align_panel.place(x=10, y=260)
        # self.register(self.align_panel)

        self.align_to_left = tk.Button(
            master = self.frame, 
            text = "Align text to left", 
            highlightbackground = self.right_panel_color,
        )
        self.align_to_left.place(x=10, y = 300)
        # self.register(self.align_to_left)

        self.align_to_right = tk.Button(
            master = self.frame, 
            text = "Align text to right", 
            highlightbackground = self.right_panel_color,
        )
        self.align_to_right.place(x=150, y = 300)
        # self.register(self.align_to_right)

        self.align_to_center = tk.Button(
            master = self.frame, 
            text = "Align text to center", 
            highlightbackground = self.right_panel_color,
        )
        self.align_to_center.place(x=10, y = 350)
        # self.register(self.align_to_center)

        self.justify_text = tk.Button(
            master = self.frame, 
            text = "Justify text", 
            highlightbackground = self.right_panel_color,
        )
        self.justify_text.place(x=175, y = 350)
        # self.register(self.justify_text)
    
    def handleLeftMousePress(self, event):
        self.save_file()

    def open_file(self):
        self.app.current_filename = askopenfilename()

        f = open(self.app.current_filename, "r")
        text = f.read()

        if self.app.current_filename:

           self.newFile = tk.Button(master=self.app.contentPage.frame, text="New file")
           self.newFile.place(x=5, y=5)
           # "<Button-1>" is event for left click on the mouse
           self.newFile.bind("<Button-1>", self.handleLeftMousePress)

        self.app.writeArea.content.delete("1.0", tk.END)
        self.app.writeArea.content.insert("1.0", text)


    def save_file(self):
        self.app.current_filename = asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
        )

        if not self.app.current_filename:
            return

        with open(self.app.current_filename, mode="w", encoding="utf-8") as output_file:
            
            writePage = self.app.getPage("WriteArea")
            
            if writePage:
                text = writePage.get_content()
                output_file.write(text)