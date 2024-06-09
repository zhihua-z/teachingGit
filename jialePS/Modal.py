import tkinter as tk
from tkinter import simpledialog
from PIL import Image, ImageTk

class Modal对话框(simpledialog.Dialog):
    def __init__(self, root, 提示):
        super().__init__(root)
        self.提示 = 提示
        
    def body(self, master):
        tk.Label(master, text="重命名").grid(row=0)
        self.entry = tk.Entry(master)
        self.entry.grid(row=0, column=1)
        return self.entry  # 设置初始焦点

    def apply(self):
        self.result = self.entry.get()

class modal新图层对话框(simpledialog.Dialog):
    def body(self, master):
        
        blackPng = Image.open('img/添加新图层.png')
        importPng = Image.open('img/导入新图层.png')
        
        blackPng = blackPng.resize((80, 80))
        importPng = importPng.resize((80, 80))
        
        blackIcon = ImageTk.PhotoImage(blackPng)
        importIcon = ImageTk.PhotoImage(importPng)
        
        l1 = tk.Button(master, image=blackIcon)
        l1.image = blackIcon
        l1.grid(row=0, column=1)
        
        l2 = tk.Button(master, image=importIcon)
        l2.image = importIcon
        l2.grid(row=0, column=2)
