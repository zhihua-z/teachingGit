# as : create an alias for a library
import tkinter as tk

# create a tk window
window = tk.Tk()

# frame creates a section on the screen with width and height to hold something
frame_main = tk.Frame(width=800, height=600)
frame_main.pack()

# creating a new label widget and give a text
# pack() is a geometry manager, it is used to place your widget in your window
#  and shrink the parent component size to just fit its child size
# place() is a geometry manager too, placing the widget to a position
lbl = tk.Label(text='hi', master=frame_main)
lbl.place(x = 0, y = 0)

# Entry is a one line text field for you to write something 
entry_name = tk.Entry(master=frame_main)
entry_name.place(x = 50, y = 0)

def handle_keypress(event):
    print(event)

window.bind('s', handle_keypress)



def handle_click_entry():
    # entry_name.delete(0, tk.END)
    val = entry_name.get()
    output = ''
    for ch in val:
        output += str(ord(ch)) + ' '
        

    entry_name.delete(0, tk.END)
    entry_name.insert(0, output)

def handle_click_text():
    val = txt_content.get('1.0', tk.END)
    val = val.split('\n')
    print(val)

    output = ''
    for line in val:
      for ch in line:
          output += str(bin(ord(ch))) + ' '
      output += '\n'
        

    txt_content.delete('1.0', tk.END)
    txt_content.insert(tk.END, output)

btn_convert = tk.Button(text='convert', command=handle_click_text)

# <Button-1> means left click
# <Button-2> middle mouse click, <Button-3> right mouse click
# def handle_click(event):
#     print(event)
#     print('button clicked')
    
# btn_clear.bind('<Button-1>', handle_click)

btn_convert.place(x = 0, y = 30)

txt_content = tk.Text()
txt_content.place(x = 0, y = 60)

# start main event loop for this window
window.mainloop()
