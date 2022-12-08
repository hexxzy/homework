from tkinter import *

def click():
    name = entry_box.get()
    message = str("Hello, " + name)
    output_box["text"] = message

window = Tk()
window.title("Names")
window.geometry("720x480")
window["bg"] = "black"


photo = PhotoImage(file = "logo.gif")
photobox = Label(window, image = photo)
photobox.image = photo
photobox.place(x = 250, y = 70, width = 200, height = 150)

label = Label(text = "Enter your name: ")
label.place(x=20, y=300)

entry_box = Entry (text = 0)
entry_box.place(x=120, y=300, width=200)

button1 = Button(text = "Press me", command=click)
button1.place(x=20, y=400, width=100)

output_box = Message()
output_box.place(x=120, y=400, width=200)

window.mainloop()
