import tkinter as tk

# default variable
def render_list(mainframe, lst, starting_pos = (0, 0)):
    for i in range(len(lst)):
        label = tk.Button(text=f'{lst[i]}')
        label.place(x = starting_pos[0] + i * 50, y = starting_pos[1])

# Create the main window
root = tk.Tk()
root.title("Cipher Program")

mainframe = tk.Frame(root, width=800, height=600)
mainframe.pack()

mylist = [4, 1, 9, 2, 5, 8, 3, 6, 7]

def swap(list, a, b):
    temp = list[a]
    list[a] = list[b]
    list[b] = temp

def one_step():
    global mylist, mainframe
    otherlist = mylist.copy()

    for i in range(1, len(otherlist)):
        if otherlist[i] < otherlist[i - 1]:
            swap(otherlist, i, i - 1)

    render_list(mainframe, mylist)
    render_list(mainframe, otherlist, (0, 50))

    mylist = otherlist

def bubble_sort():
    global mylist, mainframe
    sorted = False

    while not sorted:
        sorted = True
        for i in range(1, len(mylist)):
            if mylist[i] < mylist[i - 1]:
                swap(mylist, i, i - 1)
                sorted = False
    
    render_list(mainframe, mylist)

def reset():
    global mylist, mainframe
    mylist = [4, 1, 9, 2, 5, 8, 3, 6, 7]
    render_list(mainframe, mylist)
    

btn_step = tk.Button(text='step', master=mainframe, command=one_step)
btn_step.place(x=0, y=400)

btn_sort = tk.Button(text='bubble sort', master=mainframe, command=bubble_sort)
btn_sort.place(x=0, y=450)

btn_reset = tk.Button(text='reset', master=mainframe, command=reset)
btn_reset.place(x=0, y=500)

render_list(mainframe, mylist)

# Run the main loop
root.mainloop()