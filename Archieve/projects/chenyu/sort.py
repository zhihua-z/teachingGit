import tkinter as tk

# default variable
def render_list(mainframe, lst, starting_pos = (0, 0)):
    for i in range(len(lst)):
        label = tk.Button(text=f'{lst[i]}')
        label.place(x = starting_pos[0] + i * 50, y = starting_pos[1])


def render_pointer(index):
    print(index)
    global mainframe
    lbl_pointer = tk.Label(text="^", master=mainframe)
    lbl_pointer.place(x = index * 50 + 25, y = 100)

# Create the main window
root = tk.Tk()
root.title("Cipher Program")

mainframe = tk.Frame(root, width=800, height=600)
mainframe.pack()

mylist = [4, 1, 9, 2, 5, 8, 3, 6, 7]
insertion_sort_step_index = 1

def swap(list, a, b):
    temp = list[a]
    list[a] = list[b]
    list[b] = temp

def bubble_one_step():
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

def insertion_one_step():
    global mylist, mainframe, insertion_sort_step_index

    if insertion_sort_step_index >= len(mylist):
        return

    otherlist = mylist.copy()

    for j in range(insertion_sort_step_index, 0, -1): #处理东西
        if otherlist[j] < otherlist[j - 1]:
            swap(otherlist, j, j - 1)

    render_list(mainframe, mylist)
    render_list(mainframe, otherlist, (0, 50))

    mylist = otherlist
    print('here')
    render_pointer(insertion_sort_step_index)
    insertion_sort_step_index += 1

def insertion_sort():
    global mylist, mainframe

    for i in range(1, len(mylist)): # 控制我们在处理第几个东西
        for j in range(i, 0, -1): #处理东西
            if mylist[j] < mylist[j - 1]:
                swap(mylist, j, j - 1)

    render_list(mainframe, mylist)
            

def reset():
    global mylist, mainframe
    mylist = [4, 1, 9, 2, 5, 8, 3, 6, 7]
    render_list(mainframe, mylist)

btn_step = tk.Button(text='bubble step', master=mainframe, command=bubble_one_step)
btn_step.place(x=0, y=400)

btn_sort = tk.Button(text='bubble sort', master=mainframe, command=bubble_sort)
btn_sort.place(x=0, y=450)

btn_reset = tk.Button(text='reset', master=mainframe, command=reset)
btn_reset.place(x=0, y=500)

btn_insert_step = tk.Button(text='insert step', master=mainframe, command=insertion_one_step)
btn_insert_step.place(x=100, y=400)

btn_insertion_sort = tk.Button(text='insertion sort', master=mainframe, command=insertion_sort)
btn_insertion_sort.place(x=100, y=450)

render_list(mainframe, mylist)

# Run the main loop
root.mainloop()