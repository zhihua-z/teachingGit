# import tkinter library and rename it as tk
from curses import color_content
from distutils.dist import command_re
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from turtle import back

'''
Event based design
your application will not do anything until an event happens

'''

def handle_add():
    val = myEntry.get()
    txt_content.insert(tk.END, val + '\n')
    myEntry.delete(0, tk.END)


# main app window
myWindow = tk.Tk()
current_file = ''

# Frame : div 
frame_main = tk.Frame(width=500, height=500)
frame_main.pack(side=tk.LEFT)

# Text : multi line text field
txt_content = tk.Text(master=frame_main, height=40)
txt_content.pack()






frame_right = tk.Frame(width=200, height=500)
frame_right.pack(side=tk.LEFT)

# bg - background
# fg - foreground
myLabel = tk.Label(text='name', master=frame_right)
# pack your component into the main window
myLabel.place(x=0, y=20)

# Entry stands for text field
myEntry = tk.Entry(master=frame_right, width=10)
myEntry.place(x=50, y=20)

# Button
btn_clear = tk.Button(text='clear', master=frame_right)
btn_clear.place(x=0, y=50)

# Add Button
btn_add = tk.Button(text='add', master=frame_right, command=handle_add)
btn_add.place(x=70, y = 50)

def fn_open_file():
    global current_file
    # open a system dialog to ask user to open a file
    filepath = askopenfilename(
        # we specify the open file type must be a .txt
        filetypes=[('Text Files', '*.txt')]
    )

    # if user did not select any file, stop
    if not filepath:
        return
    
    # clear the content of the text area
    txt_content.delete('1.0', tk.END)

    # open the selected file path in reading mode, read the content and write
    # the content into our text area
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
        txt_content.insert(tk.END, text)

    current_file = filepath
    myWindow.title(f"Simple Text Editor - {filepath}")

btn_open = tk.Button(text='open file', master=frame_right, command=fn_open_file)
btn_open.place(x = 0, y = 100)

def fn_save_file():
    global current_file

    if current_file == '':
        fn_save_as_file()
        return

    with open(current_file, 'w', encoding='utf-8') as f:
        text = txt_content.get('1.0', tk.END)
        f.write(text)
        
    

btn_open = tk.Button(text='save file', master=frame_right, command=fn_save_file)
btn_open.place(x = 0, y = 130)


def fn_save_as_file():
    global current_file
    filepath = asksaveasfilename(
        filetypes=[('Text Files', '*.txt')]
    )

    if not filepath:
        return
    
    with open(filepath, 'w', encoding='utf-8') as f:
        text = txt_content.get('1.0', tk.END)
        f.write(text)

    current_file = filepath
    myWindow.title(f"Simple Text Editor - {filepath}")

btn_open = tk.Button(text='save as file', master=frame_right, command=fn_save_as_file)
btn_open.place(x = 0, y = 160)


# def handle_S(event):
#     print(event.char)

# myWindow.bind('S', handle_S)
# myWindow.bind('s', handle_S)

def handle_clear(event):
    # single deletion
    # myEntry.delete(0)
    # for Entry, since it is just one line, so character position we just need one number
    myEntry.delete(0, tk.END)

btn_clear.bind("<Button-1>", handle_clear)


# run your application and start event loop
# each time you press a button, or you modify something in the text box, they 
# are all treated as an Event, so your application will listen to these events
# and react accordingly
myWindow.mainloop()


'''
add a label, an entry, a new button called search
pressing this button will try to search for text in the new entry in the main text area
if found: print found in the console
if not found: print not found in the console (print('not found'))
'''