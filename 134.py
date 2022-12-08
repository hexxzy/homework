import random
from tkinter import *

def answer():
 answer = answer_box.get()
 answer = int(answer)
 num1 = num_label["text"]
 num1 = int(num1)
 num2 = num_label2["text"]
 num2 = int(num2)
 ans = num1 + num2
 if answer == ans:
   img = PhotoImage(file="galka.gif")
   image_box.image = img
   image_box["image"] = img
   image_box.update()
 else:
   img = PhotoImage(file="krestik.gif")
   image_box.image = img
   image_box["image"] = img
   image_box.update()
def next():
 answer_box.delete(0, END)
 num1 = random.randint(10, 50)
 num_label["text"] = num1
 num2 = random.randint(10, 50)
 num_label2["text"] = num2
 img = PhotoImage(file = "")
 image_box.image = img
 image_box["image"] = img
 image_box.update()



root = Tk()
root.title("Сумма чисел")
root.geometry("720x480")

num_label = Label(text="0")
num_label.place(x = 50, y = 30, width=25, height=25)
plus = Message(text="+")
plus.place(x = 75, y = 30, width=25, height=25)
num_label2 = Label(text="0")
num_label2.place(x = 100, y = 30, width=25, height=25)
equal = Message(text="=")
equal.place(x = 125, y = 30, width=25, height=25)

answer_box = Entry(text = "")
answer_box.place(x = 150, y = 30, width = 25, height = 25)
checkbtn = Button(text = "Ответить", command = answer)
checkbtn.place(x = 50, y = 60, width = 75, height = 25)
nextbtn = Button(text = "Другой вопрос", command = next)
nextbtn.place(x = 130, y = 60, width = 100, height = 25)
img = PhotoImage(file = "")
image_box = Label(image = img)
image_box.image = img
image_box.place(x = 25, y = 100, width = 200, height = 150)
next()
root.mainloop()

