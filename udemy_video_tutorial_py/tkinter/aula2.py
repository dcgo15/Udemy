from tkinter import *

app = Tk()
app.title("App")
app.geometry("300x600")
app.resizable(0, 0)
app.config(bg="red")

lb = Label(app, text="Olá, tudo bem?", bg="red", fg="white", font="arial 10 bold").pack()
lb2 = Label(app, text="Olá, tudo sim", bg="red", fg="white", font="arial 10 bold").pack()

app.mainloop()
