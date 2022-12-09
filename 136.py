from tkinter import *
def Record():
  name = name_box.get()
  name_box.delete(0, END)
  genderselect = gender.get()
  gender.set("male/female")
  new_data = name + ", " + genderselect + "\n"
  name_list.insert(END, new_data)

window = Tk()
window.geometry("420x250")

gender = StringVar(window)
gender.set("male/female")
gender_label = Label(text="Выберите пол: ")
gender_label.place(x = 10, y = 100)
gender_list = OptionMenu(window, gender, "male", "female")
gender_list.place(x = 100, y = 100, height= 25)

name_label = Label(text="Введите имя: ")
name_label.place(x = 10, y = 50)
name_box = Entry(text="")
name_box.place(x = 100, y = 50, width=110)
name_list = Listbox()
name_list.place(x = 275, y = 50, width=100, height=150)

button = Button(text="Нажми для записи", command=Record)
button.place(x= 100, y = 150, height=25)

window.mainloop()
