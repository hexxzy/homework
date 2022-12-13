import sqlite3
from tkinter import *
def studentName():
    new_student = name_entry.get()
    new_grade = grade_entry.get()
    cursor.execute("""INSERT INTO Student(studentname, grade)VALUES(?, ?)""", (new_student, new_grade))
    db.commit()
    name_entry.delete(0, END)
    grade_entry.delete(0, END)
    name_entry.focus
def clearList():
    name_entry.delete(0, END)
    grade_entry.delete(0, END)
    name_entry.focus
with sqlite3.connect("TestScores.db") as db:
    cursor = db.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS Student(
    id integer PRIMARY KEY,
    studentname text ,
    grade integer);""")

window = Tk()
window.title("Ratings")
window.geometry("400x250")

name_label = Label(text="Enter student's name: ")
name_label.place(x = 40, y = 30, width=150, height=25)
grade_label = Label(text="Enter student's grade: ")
grade_label.place(x=40, y = 80, width=150, height=25)
name_entry = Entry(text="")
name_entry.place(x=170, y=30, width=150, height=25)
grade_entry = Entry(text="")
grade_entry.place(x=170, y=80, width=150, height=25)
add_button = Button(text="Add", command=studentName)
add_button.place(x=170, y=130, width=70, height=25)
clear_button = Button(text="Clear", command=clearList)
clear_button.place(x=250, y=130, width=70, height=25)


window.mainloop()
db.close()
