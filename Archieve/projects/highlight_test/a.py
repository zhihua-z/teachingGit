#Import tkinter library
from tkinter import *
#Create an instance of tkinter frame
win= Tk()
win.geometry("750x450")
#Define a function to highlight the text
def add_highlighter():
   text.tag_add("start", "1.11","1.17")
   text.tag_config("start", background= "black", foreground= "white")
#Create a Tex Field
text= Text(win);
text.insert(INSERT, "Hey there! Howdy?")
text.pack()
#Create a Button to highlight text
Button(win, text= "Highlight", command= add_highlighter).pack()
win.mainloop()
