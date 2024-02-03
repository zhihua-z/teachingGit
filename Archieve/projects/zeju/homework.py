import tkinter as tk
import math


def add():
  a = float(entry_a.get())
  b = float(entry_b.get())
  
  
  
  lbl_result['text'] = str(a + b)
  
def subtract():
  a = float(entry_a.get())
  b = float(entry_b.get())
  
  lbl_result['text'] = a - b
  
def divide():
  a = float(entry_a.get())
  b = float(entry_b.get())
  if b != 0:
    lbl_result['text'] = a / b
  else:
    return false
    
def times():
  a = float(entry_a.get())
  b = float(entry_b.get())
  lbl_result['text'] = a * b
  
window = tk.Tk()

mainFrame = tk.Frame()

mainFrame.pack()

entry_a = tk.Entry(master = mainFrame)
entry_a.pack(side=tk.LEFT)
lbl_a = tk.Label(text=' + ', master = mainFrame)
lbl_a.pack(side=tk.LEFT)

entry_b = tk.Entry(master = mainFrame)
entry_b.pack(side=tk.LEFT)
lbl_b = tk.Label(text='  ', master = mainFrame)
lbl_b.pack(side=tk.LEFT)



btn_convert = tk.Button(text='add', command=add)
btn_convert.pack()

btn_convert = tk.Button(text='subtract', command=subtract)
btn_convert.pack()

btn_convert = tk.Button(text='multiply', command=times)
btn_convert.pack()

btn_convert = tk.Button(text='divide', command=divide)
btn_convert.pack()

lbl_result = tk.Label(text='result=')
lbl_result.pack()



window.mainloop()
