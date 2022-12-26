from tkinter import *


app = Tk()
app.title("Calculadora")
app.geometry("300x400")
app.config(bg="white")
app.resizable(0, 0)


def soma():
    num_1 = float(num1.get())
    num_2 = float(num2.get())


    soma = num_1 + num_2

    resultado["text"] = f"Seu resultado é: {soma}"

def sub():
    num_1 = float(num1.get())
    num_2 = float(num2.get())

    sub = num_1 - num_2

    resultado["text"] = f"Seu resultado é: {sub}"

def mult():
    num_1 = float(num1.get())
    num_2 = float(num2.get())

    mult = num_1 * num_2

    resultado["text"] = f"Seu resultado é: {mult}"

def div():
    num_1 = float(num1.get())
    num_2 = float(num2.get())

    div = num_1 / num_2

    resultado["text"] = f"Seu resultado é: {div}"

lb = Label(app, text="Calculadora", bg="white", fg="blue", font="Helvetica 20 bold").pack()


lb = Label(app, text="Numero 1:", bg="white", fg="blue", font="Helvetica 12 bold").pack()


num1 = Entry(app, font="arial 13", width=15)
num1.pack()
lb = Label(app, text="Numero 2:", bg="white", fg="blue", font="Helvetica 12 bold").pack()

num2= Entry(app, font="arial 13", width=15)
num2.pack()

bt = Button(app, text="+", bg="white", fg="blue", command=soma).place(x=30, y=180)
bt2 = Button(app, text="-", bg="white", fg="blue", command=sub).place(x=90, y=180)
bt3 = Button(app, text="*", bg="white", fg="blue", command=mult).place(x=150, y=180)
bt4= Button(app, text="/", bg="white", fg="blue", command=div).place(x=210, y=180)

resultado = Label(app, text="", bg="white",
                      fg="blue", font="Helvetica 15 bold")
resultado.place(x=30, y=300)


app.mainloop()
