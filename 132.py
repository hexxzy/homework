from tkinter import *
def Save():
    file = open("name&ages.csv", "a")
    fullName = entry_name.get() + " " + entry_age.get()
    file.write(fullName + "\n")
    file.close()
def Output():
   file = open("name&ages.csv", "r")
   lst = file.read()
   msg = Message(window, text = f"Список:\n {lst}", bg="pink")
   msg.place(x = 250, y = 50)
   file.close()


window = Tk()
window.title("Таблица людей")
window.geometry("450x200")
window["bg"] = "grey"

entry_name = Entry()
entry_name.insert(0, "Введите имя")
entry_name.place(x = 20, y = 30, width= 200, height=30)
entry_age = Entry()
entry_age.insert(0, "Введите возраст")
entry_age.place(x = 20, y = 70, width= 200, height=30)
button = Button(text = "Сохранить", command = Save)
button.place(x = 50, y = 100, width = 100, height = 20)
button = Button(text = "Показать список", command = Output)
button.place(x = 50, y = 130, height = 20)
window.mainloop()
