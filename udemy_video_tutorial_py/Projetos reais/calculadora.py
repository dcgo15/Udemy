from tkinter import *

app = Tk()
app.title("Calculadora")
app.config(bg="white")
app.resizable(0, 0)
app.geometry("300x400")

def mais():
    num_1 = float(num1.get())
    num_2 = float(num2.get())

    resposta = num_1 + num_2

    result["text"] = "Seu resultado é:", resposta

def menos():
    num_1 = float(num1.get())
    num_2 = float(num2.get())

    resposta = num_1 - num_2

    result["text"] = "Seu resultado é:", resposta

def mult():
    num_1 = float(num1.get())
    num_2 = float(num2.get())

    resposta = num_1 * num_2

    result["text"] = "Seu resultado é:", resposta

def div():
    num_1 = float(num1.get())
    num_2 = float(num2.get())

    resposta = num_1 / num_2

    result["text"] = "Seu resultado é:", resposta



lb = Label(app, text="Calculadora", fg="blue", bg="white", font="arial 14 bold").pack()


lb = Label(app, text="Numero 1:", fg="blue", bg="white", font="arial 10 bold").place(x=30, y=50)
num1 = Entry(app, font="arial 12", width=10)
num1.place(x=120, y=50)


lb = Label(app, text="Numero 2:", fg="blue", bg="white", font="arial 10 bold").place(x=30, y=120)
num2 = Entry(app, font="arial 12", width=10)
num2.place(x=120, y=120)


bt1 = Button(app, text="+", bg="white", fg="blue", command=mais).place(x=30, y=180)
bt2 = Button(app, text="-", bg="white", fg="blue", command=menos).place(x=90, y=180)
bt3 = Button(app, text="*", bg="white", fg="blue", command=mult).place(x=150, y=180)
bt4 = Button(app, text="/", bg="white", fg="blue", command=div).place(x=210, y=180)


result = Label(app, text="Seu resultado é:", fg="blue", bg="white", font="arial 10 bold")
result.place(x=30,y=250)


app.mainloop()
