from tkinter import *
def Picture():
  number = num_entry.get()
  if number == "1":
    img = PhotoImage(file="I.gif")
    image_box.image = img
    image_box["image"] = img
    image_box.update()
  elif number == "2":
    img = PhotoImage(file="love.gif")
    image_box.image = img
    image_box["image"] = img
    image_box.update()
  elif number == "3":
    img = PhotoImage(file="py.gif")
    image_box.image = img
    image_box["image"] = img
    image_box.update()
  else:
    print("ERROR")
    exit()


window = Tk()
window.title("Some pictures")
window.geometry("300x400")

num_entry = Entry(text="")
num_entry.place(x=100, y=200, width=75, height=20)

btn = Button(text="Switch picture", command=Picture)
btn.place(x=100, y=250, width=75, height=20)

img = PhotoImage(file="I.gif")
image_box = Label(image=img)
image_box.image = img
image_box.place(x=50, y=25, width=200, height=100)

window.mainloop()
