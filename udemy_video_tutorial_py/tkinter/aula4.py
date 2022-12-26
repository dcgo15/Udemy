from tkinter import *

app = Tk()
app.title("App")
app.geometry("300x600")
app.resizable(0, 0)
app.config(bg="red")


def login():
    email = em.get()
    senha = sen.get()
    mensagem = mens.get("1.0", END)

    print(f"Seu email é: {email} \nSua senha é: {senha} \nSua mensagem é: {mensagem}")


lb = Label(app, text="LOGIN", bg="red", fg="white", font="Helvetica 20 bold").pack()

lb = Label(app, text="Email", bg="red", fg="white", font="Helvetica 10 bold").pack()

em = Entry(app, width=15)
em.pack()


lb = Label(app, text="Senha", bg="red", fg="white", font="Helvetica 10 bold").pack()

sen= Entry(app, width=15, show="*")
sen.pack()

lb = Label(app, text="Mensagem", bg="red", fg="white", font="Helvetica 10 bold").pack()

mens= Text(app, width=15)
mens.pack()


bt = Button(app, text="Continuar", bg="red", fg="white", command=login).pack()


app.mainloop()

