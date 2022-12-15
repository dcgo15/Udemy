from tkinter import *

app = Tk()
app.title("App1")
app.geometry("400x400")
app.resizable(0, 0)


def mudar_cor():
    lb["bg"] = 'blue'
    lb["fg"] = "white"
    lb["text"] = "Mudou a Cor"

def mudar_cor_lb2():
    lb2["bg"] = "blue"
    lb2["fg"] = "white"
    lb2["text"]= "Mudou a Cor"

lb = Label(app, text="Olá Usuário", font="arial 20 bold", fg='gray', bg="red")
lb.pack()

lb2 = Label(app, text="Tudo bem?", font="arial 10", fg="green", bg="pink")
lb2.pack()

bt = Button(app, text="Mudar cor lb1", command=mudar_cor)
bt.pack()

bt2 = Button(app, text="Mudar cor lb2", command=mudar_cor_lb2)
bt2.pack()

app.mainloop()
