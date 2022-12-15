from tkinter import *
import random

app = Tk()
app.title("Pedra, Papel e Tesoura")
app.geometry("400x400")
app.resizable(0,0)


pont_vc = 0
pont_bot = 0 



#lista = ["Pedra", "Papel", "Tesoura"]
#escolha = random.choice(lista)


def pedra():
    global pont_vc
    global pont_bot

    
    lista = ["Pedra", "Papel", "Tesoura"]
    escolha = random.choice(lista)

    lb["text"] = f"A escolha foi:{escolha}"


    pedra = "pedra"


    if escolha == "Pedra":
        pont_vc += 0
        pont_bot += 0

        print("Empate", pont_vc, pont_bot)

    elif escolha == "Papel":
        pont_vc += 0
        pont_bot += 10

        print("Bot Ganhou", pont_vc, pont_bot)

    elif escolha == "Tesoura":
        pont_vc += 10
        pont_bot += 0

        print("Voce Ganhou", pont_vc, pont_bot)


    lb3["text"] = pont_vc
    lb4["text"] = pont_bot


def papel():

    global pont_vc
    global pont_bot
    
    lista = ["Pedra", "Papel", "Tesoura"]
    escolha = random.choice(lista)

    lb["text"] = f"A escolha foi:{escolha}"

    papel = "papel"

    if escolha == "Pedra":
        pont_vc += 10
        pont_bot += 0

        print("Voce ganhou", pont_vc, pont_bot)

    elif escolha == "Papel":
        pont_vc += 0
        pont_bot += 0

        print("Empate", pont_vc, pont_bot)

    elif escolha == "Tesoura":
        pont_vc += 0
        pont_bot += 10

        print("Bot Ganhou", pont_vc, pont_bot)


    lb3["text"] = pont_vc
    lb4["text"] = pont_bot
    

def tes():
    global pont_vc
    global pont_bot
    
    lista = ["Pedra", "Papel", "Tesoura"]
    escolha = random.choice(lista)

    lb["text"] = f"A escolha foi:{escolha}"

    tesoura = "tesoura"

    if escolha == "Pedra":
        pont_vc += 0
        pont_bot += 10

        print("Bot ganhou", pont_vc, pont_bot)

    elif escolha == "Papel":
        pont_vc += 10
        pont_bot += 0

        print("Voce Ganhou", pont_vc, pont_bot)

    elif escolha == "Tesoura":
        pont_vc += 0
        pont_bot += 0

        print("Empate", pont_vc, pont_bot)

    lb3["text"] = pont_vc
    lb4["text"] = pont_bot


lb5 = Label(app, text="você:", fg="black", font="arial 12 bold").place(x=10, y=10)
lb2 = Label(app, text="Bot:", fg="black", font="arial 12 bold").place(x=300, y=10)
lb3 = Label(app, text="0", fg="black", font="arial 30 bold")
lb3.place(x=10, y=80)
lb4= Label(app, text="0", fg="black", font="arial 30 bold")
lb4.place(x=300, y=80)


lb = Label(app, text="", font="arial 8 bold")
lb.place(x=100, y=130)



bt = Button(app, text="Pedra", width=10, command=pedra).place(x=10,y=200)
bt = Button(app, text="Papel", width=10, command=papel).place(x=150,y=200)
bt = Button(app, text="Tesoura", width=10,command=tes).place(x=310,y=200)



app.mainloop()
