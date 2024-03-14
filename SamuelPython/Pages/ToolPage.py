import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from Page import Page


class ToolPage(Page):

    def __init__(self, app):
        super().__init__(app)
        self.open_file_button = None
        self.right_panel_color = "#cccccc"

    def draw(self):
        self.frame = tk.Frame(background=self.right_panel_color, width=300, height=700)
        self.frame.place(x=950, y=0)
        self.register(self.frame)

        self.open_file_button = tk.Button(
            master=self.frame,
            text="open file",
            highlightbackground=self.right_panel_color,
            command=self.open_file,
        )
        self.open_file_button.place(x=0, y=10)

        self.save_file_button = tk.Button(
            master=self.frame,
            text="save file",
            highlightbackground=self.right_panel_color,
            command=self.save_file,
        )
        self.save_file_button.place(x=100, y=10)

        self.font_panel = tk.Label(
            master=self.frame,
            text="Font",
            highlightbackground=self.right_panel_color,
        )
        self.font_panel.place(x=10, y=60)

        self.font_type_button = tk.Button(
            master=self.frame,
            text="Font type",
            highlightbackground=self.right_panel_color,
        )
        self.font_type_button.place(x=0, y=100)

        self.font_size_button = tk.Button(
            master=self.frame,
            text="Font size",
            highlightbackground=self.right_panel_color,
        )
        self.font_size_button.place(x=100, y=100)

        self.text_color_button = tk.Button(
            master=self.frame,
            text="Text color",
            highlightbackground=self.right_panel_color,
        )
        self.text_color_button.place(x=200, y=100)

        self.bold_text = tk.Button(
            master=self.frame,
            text="B",
            highlightbackground=self.right_panel_color,
        )
        self.bold_text.place(x=0, y=150)

        self.italic_text = tk.Button(
            master=self.frame,
            text="I",
            highlightbackground=self.right_panel_color,
        )
        self.italic_text.place(x=50, y=150)

        self.underline_text = tk.Button(
            master=self.frame,
            text="U",
            highlightbackground=self.right_panel_color,
        )
        self.underline_text.place(x=90, y=150)

        self.highlight_text = tk.Button(
            master=self.frame,
            text="Highlight color",
            highlightbackground=self.right_panel_color,
        )
        self.highlight_text.place(x=0, y=200)

        self.align_panel = tk.Label(
            master=self.frame,
            text="Align",
            highlightbackground=self.right_panel_color,
        )
        self.align_panel.place(x=10, y=260)

        self.align_to_left = tk.Button(
            master=self.frame,
            text="Align text to left",
            highlightbackground=self.right_panel_color,
        )
        self.align_to_left.place(x=0, y=300)

        self.align_to_right = tk.Button(
            master=self.frame,
            text="Align text to right",
            highlightbackground=self.right_panel_color,
        )
        self.align_to_right.place(x=150, y=300)

        self.align_to_center = tk.Button(
            master=self.frame,
            text="Align text to center",
            highlightbackground=self.right_panel_color,
        )
        self.align_to_center.place(x=0, y=350)

        self.justify_text = tk.Button(
            master=self.frame,
            text="Justify text",
            highlightbackground=self.right_panel_color,
        )
        self.justify_text.place(x=170, y=350)

    def open_file(self):
        self.app.current_filename = askopenfilename()

        f = open(self.app.current_filename, "r")
        text = f.read()

        self.app.writeArea.content.delete("1.0", tk.END)
        self.app.writeArea.content.insert("1.0", text)

        label_new = tk.Label(master=self.app.contentPage.frame, text="New file")
        label_new.place(x=5, y=5)

    def save_file(self):
        self.app.current_filename = asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
        )

        if not self.app.current_filename:
            return

        """
        为什么用context manager (with)
        当你打开一个文件用来写的时候，如果另一个程序也打开了同样的文件，那么如果程序往里面写东西，你这个文件里的内容就不是最新的了。
        导致一个版本不匹配的问题。
        所以windows / mac都有一个file lock。当你打开一个文件进行编辑的时候，这个文件就会被锁上。
        被锁了的文件， 可以被打开阅读，但是不能被打开，然后写东西。
        所以我们每次打开一个文件进行编辑之后，你都要使用一个Function讲file close，来把这个打开了的文件关掉，所以别人就可以使用这个文件了
        但是很多时候我们打开了一个文件之后都会忘记去关掉，它就会导致这个文件一直被锁着，那这是一个很不好的事情。
        为什么用context manager就可以帮你去自动关闭一个文件。
        """
        with open(self.app.current_filename, mode="w", encoding="utf-8") as output_file:
            
            '''
            在这边我们使用另外一个页面的里面的组件的内容，这个是非常不好的，因为他会让我们的程序的不同的组件，互相依赖
            '''
            writePage = self.app.getPage("WriteArea")
            
            if writePage:
                text = writePage.get_content()
                output_file.write(text)

        # output_file = open(self.app.current_filename, mode='w', encoding='utf-8')
        # text = self.app.writeArea.content.get("1.0", tk.END)
        # output_file.write(text)
        # output_file.close()
