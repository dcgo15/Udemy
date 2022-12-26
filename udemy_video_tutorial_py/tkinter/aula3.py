from tkinter import *

app = Tk()
app.title("App")
app.geometry("300x600")
app.resizable(0, 0)
app.config(bg="red")

def mensagem():
    lb2['text'] = "Olá, tudo não"

lb = Label(app, text="Olá, tudo bem?", bg="red", fg="white", font="arial 10 bold").pack()
lb2 = Label(app, text="Olá, tudo sim", bg="red", fg="white", font="arial 10 bold")
lb2.pack()


bt = Button(app, text="Clica-me", bg="red", fg="white", font="arial 10 bold", width=15
           ,height=3, command=mensagem).pack()

app.mainloop()

