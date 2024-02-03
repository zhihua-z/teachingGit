from PIL import Image
from PIL import ImageTk
import tkinter as tk

window = tk.Tk()


image = Image.open('star.bmp')

image1 = ImageTk.PhotoImage(image)

panelA = tk.Label(image=image1, borderwidth=5, relief="sunken")
panelA.image = image1
panelA.grid(row= 1, column=1 , rowspan= 13, columnspan= 3, padx=20, pady=20)

def changeImage():
  image = Image.open('cat.webp')
  image = image.resize((500, 500))
  print(image.size)

  image1 = ImageTk.PhotoImage(image)

  panelA = tk.Label(image=image1, borderwidth=5, relief="sunken")
  panelA.image = image1
  panelA.grid(row= 1, column=1 , rowspan= 13, columnspan= 3, padx=20, pady=20)

btn = tk.Button(text='change', command=changeImage)
btn.grid(row=2, column=1, rowspan=2, columnspan= 3, padx=20, pady = 20)
window.mainloop()