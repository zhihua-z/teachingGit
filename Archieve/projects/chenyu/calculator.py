# as : create an alias for a library
import tkinter as tk

# create a tk window
window = tk.Tk()

# frame creates a section on the screen with width and height to hold something
frame_display = tk.Frame(width=400, height=100, background='yellow')
frame_display.pack(side=tk.TOP)

# tk.Entry
entryDisplay = tk.Entry(width=20, master=frame_display, font=('Arial', 25))
entryDisplay.place(x=10, y=10)


frame_keyboard = tk.Frame(width=400, height=450, background='cyan')
frame_keyboard.pack(side=tk.TOP)



# start main event loop for this window
window.mainloop()
