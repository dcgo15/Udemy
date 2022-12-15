from tkinter import *

app = Tk()
app.title("App1")
app.geometry("400x400")
app.resizable(0, 0)

lb = Label(app, text="Olá Usuário", font="arial 20 bold", fg='gray', bg="red")
lb.pack()

lb2 = Label(app, text="Tudo bem?", font="arial 10", fg="green", bg="pink")
lb2.pack()

app.mainloop()
