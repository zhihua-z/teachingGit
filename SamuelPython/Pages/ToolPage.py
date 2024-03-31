import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

from Page import Page

from UI.ImageButton import ImageButton

class ToolPage(Page):
    
    def __init__(self, app):
        super().__init__(app)
        self.open_file_button = None
        self.right_panel_color = '#cccccc'
        self.app = app
    
    def draw(self):
        self.clear()
        
        self.frame = tk.Frame(background=self.right_panel_color, width=400, height=700)
        self.frame.place(x=950, y=0)
        self.register(self.frame)
        
        t = ImageButton(
            master=self.frame, 
            filename='open_file.png', 
            size=(25, 25), 
            position=(10, 10), 
            command=self.open_file,
            text='Open file'
        )
        self.registerUI(t)

        t = ImageButton(
            master = self.frame, 
            filename = 'save_file.png',
            size = (25, 25),
            position = (110, 10),
            command = self.save_file,
            text = 'Save file'
        )
        self.registerUI(t)
        
        t = ImageButton(
            master = self.frame, 
            filename = 'new_file.png',
            size = (25, 25),
            position = (210, 10),
            command = self.new_file,
            text = 'New file'
        )
        self.registerUI(t)

        t = tk.Label(
            master = self.frame,
            text = 'Font', 
            highlightbackground = self.right_panel_color, 
        )
        t.place(x=10, y=100)
        self.register(t)

        t = tk.Button(
            master = self.frame,
            text = 'Font type', 
            highlightbackground = self.right_panel_color, 
        )
        t.place(x = 10, y=135)
        self.register(t)

        t = tk.Button(
            master = self.frame,
            text = 'Font size',
            highlightbackground = self.right_panel_color, 
        )
        t.place(x=110, y=135)
        self.register(t)

        t = ImageButton(
            master = self.frame, 
            filename = 'bold.png',
            size = (25, 25),
            position = (10, 185),
            command = None,
            text = 'Bold text'
        )
        self.registerUI(t) 

        t = ImageButton(
            master = self.frame, 
            filename = 'italic.png',
            size = (25, 25),
            position = (95, 185),
            command = None,
            text='Italic text'
        )
        self.registerUI(t) 

        t = ImageButton(
            master = self.frame, 
            filename = 'underline.png',
            size = (25, 25),
            position = (180, 185),
            command = None,
            text='Underline text'
        )
        self.registerUI(t) 

        t = tk.Button(
            master = self.frame,
            text = 'Text color', 
            highlightbackground = self.right_panel_color, 
        )
        t.place(x = 10, y=260)
        self.register(t)

        t = tk.Button(
            master = self.frame,
            text = "Highlight color",
            highlightbackground = self.right_panel_color,
        )
        t.place(x=110, y = 260)
        self.register(t)

        t = tk.Label(
            master = self.frame,
            text = 'Align', 
            highlightbackground = self.right_panel_color, 
        )
        t.place(x=10, y=315)
        self.register(t)

        t = ImageButton(
            master = self.frame, 
            filename = 'align_left.png',
            size = (25, 25),
            position = (10, 360),
            command = None,
            text='Align text to left'
        )
        self.registerUI(t) 

        t = ImageButton(
            master = self.frame, 
            filename = 'align_right.png',
            size = (25, 25),
            position = (160, 360),
            command = None,
            text='Align text to right'
        )
        self.registerUI(t) 

        t = ImageButton(
            master = self.frame, 
            filename = 'align_center.png',
            size = (25, 25),
            position = (10, 440),
            command = None,
            text='Align text to center'
        )
        self.registerUI(t) 

        t = ImageButton(
            master = self.frame, 
            filename = 'justify.png',
            size = (25, 25),
            position = (160, 440),
            command = None, 
            text='Justify text'
        )
        self.registerUI(t) 

    def open_file(self):
        self.app.current_filename = askopenfilename()
        f = open(self.app.current_filename, "r")
        text = f.read()

        if self.app.current_filename:

            self.app.contentPage.addChapter(content = text, filePath = self.app.current_filename)
            # To get the last page as the current page 
            self.app.currentChapter = self.app.book.chapters[-1]
            self.app.writeArea.draw()
            self.app.refresh()


    def save_file(self):

        if self.app.currentChapter.filePath:
            self.app.current_filename = self.app.currentChapter.filePath
        else:
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

    def new_file(self):
        # 1. 在左边开一个新章节
        # 2. 如果内容被修改，在章节名字后面加一个*
        # 3. 如果没保存就退出，提示是否不保存就离开
        self.app.contentPage.addChapter()
        self.app.currentChapter = self.app.book.chapters[-1]
        self.app.writeArea.draw()
        self.app.refresh()