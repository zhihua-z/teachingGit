import tkinter as tk
import math

def handle_button_press(event):
  print(event)
  
window = tk.Tk()

mainFrame = tk.Frame(width=320, height=250)

mainFrame.pack()

entry_a = tk.Entry(master = mainFrame, width=25)
entry_a.place(x = 20, y = 20)

# for i in range(1, 10):
#   btn_1 = tk.Button(master=mainFrame, text=f'{i}', width=1, height=2)
#   btn_1.place(x = 20 + ((i - 1) % 3 * 50), y = 70 + ((2 - (i - 1) // 3) * 50))

#   # i = 1: x = 20, y = 150
#   # i = 2: x = 70, y = 150
#   # i = 3: x = 120, y = 150
#   # i = 4: x = 20, y = 100
#   # i = 5: x = 70, y = 100
#   # i = 6: x = 120 y = 100
#   # i = 7: x = 20, y = 50

# window.bind('<Button-1>', handle_button_press)
def click_1():
  entry_a.insert(tk.END, '1')
btn_1 = tk.Button(master=mainFrame, text='1', width=1, height=2, command=click_1)
btn_1.place(x = 20, y = 170)

def click_2():
  entry_a.insert(tk.END, '2')
btn_2 = tk.Button(master=mainFrame, text='2', width=1, height=2, command=click_2)
btn_2.place(x = 70, y = 170)

def click_3():
  entry_a.insert(tk.END, '3')
btn_3 = tk.Button(master=mainFrame, text='3', width=1, height=2, command=click_3)
btn_3.place(x = 120, y = 170)

def click_4():
  entry_a.insert(tk.END, '4')
btn_4 = tk.Button(master=mainFrame, text='4', width=1, height=2, command=click_4)
btn_4.place(x = 20, y = 120)

def click_5():
  entry_a.insert(tk.END, '5')
btn_5 = tk.Button(master=mainFrame, text='5', width=1, height=2, command=click_5)
btn_5.place(x = 70, y = 120)

def click_6():
  entry_a.insert(tk.END, '6')
btn_6 = tk.Button(master=mainFrame, text='6', width=1, height=2, command=click_6)
btn_6.place(x = 120, y = 120)

def click_7():
  entry_a.insert(tk.END, '7')
btn_7 = tk.Button(master=mainFrame, text='7', width=1, height=2, command=click_7)
btn_7.place(x = 20, y = 70)

def click_8():
  entry_a.insert(tk.END, '8')
btn_8 = tk.Button(master=mainFrame, text='8', width=1, height=2, command=click_8)
btn_8.place(x = 70, y = 70)

def click_9():
  entry_a.insert(tk.END, '9')
btn_9 = tk.Button(master=mainFrame, text='9', width=1, height=2, command=click_9)
btn_9.place(x = 120, y = 70)

def click_0():
  entry_a.insert(tk.END, '0')
btn_0 = tk.Button(master=mainFrame, text='0', width=1, height=2, command=click_0)
btn_0.place(x = 170, y = 170)

def click_clear():
  entry_a.delete(0, tk.END)
btn_clear = tk.Button(master=mainFrame, text='AC', width=1, height=2, command=click_clear)
btn_clear.place(x = 170, y = 70)

def click_add():
  entry_a.insert(tk.END, ' + ')
btn_add = tk.Button(master=mainFrame, text='+', width=1, height=2, command=click_add)
btn_add.place(x = 170, y = 120)

def click_minus():
  entry_a.insert(tk.END, ' + ')
btn_minus = tk.Button(master=mainFrame, text='+', width=1, height=2, command=click_add)
btn_minus.place(x = 170, y = 120)

def click_times():
  entry_a.insert(tk.END, ' + ')
btn_times = tk.Button(master=mainFrame, text='+', width=1, height=2, command=click_add)
btn_times.place(x = 170, y = 120)

def click_divide():
  entry_a.insert(tk.END, ' + ')
btn_divide = tk.Button(master=mainFrame, text='+', width=1, height=2, command=click_add)
btn_divide.place(x = 170, y = 120)



window.mainloop()
