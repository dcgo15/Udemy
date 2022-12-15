from tkinter import *

app = Tk()
app.title("App1")
app.geometry("400x400")
app.resizable(0, 0)

def login():
    print("Usuario logado \nEmail", entry.get(), "Senha", entry2.get(), "Mensagem", txt.get("1.0", END))


lb = Label(app, text="Login", font="arial 20 bold", fg='gray', bg="red")
lb.pack()

lb = Label(app, text="Email", font="arial 10 bold", fg='gray', bg="red")
lb.pack()

entry = Entry(app, font="arial 16 bold", width=10)
entry.pack()

lb = Label(app, text="Senha", font="arial 10 bold", fg='gray', bg="red")
lb.pack()

entry2 = Entry(app, font="arial 16 bold", width=10, show="*")
entry2.pack()

lb = Label(app, text="Mensagem", font="arial 10 bold", fg='gray', bg="red")
lb.pack()

txt = Text(app, font="arial 2")
txt.pack()


bt = Button(app, text="Logar", command=login)
bt.pack()


app.mainloop()
