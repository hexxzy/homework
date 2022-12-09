from tkinter import *

def changeColor():
  color_selection = color.get()
  window.configure(background = color_selection)

window = Tk()
window.title("Colors")
window.geometry("200x200")

color = StringVar(window)
color.set("Red")
color_menu = OptionMenu(window, color, "Red", "Green", "Blue")
color_menu.place(x= 50, y = 100)

btn = Button(text="Change color", command=changeColor)
btn.place(x = 50, y = 150)

window.mainloop()



