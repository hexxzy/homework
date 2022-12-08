import tkinter as tk

def createNewWindow():
    file = open("Numbers.txt", "w")
    file.write("123")
    file.close()
    name = open("Numbers.txt", "r")
    list = name.read
    newWindow = tk.Toplevel(app)
    MessageExample = tk.Message(newWindow, text = f"\n{list}")

    MessageExample.pack()

app = tk.Tk()
buttonExample = tk.Button(app,
              text="Create new window",
              command=createNewWindow)
buttonExample.pack()

app.mainloop()
