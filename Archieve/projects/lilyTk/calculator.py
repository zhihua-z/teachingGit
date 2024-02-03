
# import tkinter library and rename it as tk
import tkinter as tk

# main app window
myWindow = tk.Tk()

# Frame : div
frame_main = tk.Frame(width=500, height=500)
frame_main.pack()

entry_display = tk.Entry(width=30, master=frame_main)
entry_display.place(x=20, y=20)

myWindow.mainloop()
