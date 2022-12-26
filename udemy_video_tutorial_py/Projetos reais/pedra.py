from tkinter import *
import random




pont_vc = 0
pont_BOT = 0


app = Tk()
app.title("Pedra, Papel e Tesoura")
app.geometry("400x400")
app.resizable(0, 0)

def pedra():
    global pont_vc
    global pont_BOT
    
    lista = ["Pedra", "Papel", "Tesoura"]
    escolha = random.choice(lista)


    if escolha == "Pedra":
        escol["text"] = "Robô escolheu:pedra"
        pont_vc += 0
        pont_BOT += 0

        pontos_vc["text"] = f"{pont_vc}"
        pontos_bot["text"] = f"{pont_BOT}"

    elif escolha == "Papel":
        escol["text"] = "Robô escolheu:papel"
        pont_vc += 0
        pont_BOT += 10

        pontos_vc["text"] = f"{pont_vc}"
        pontos_bot["text"] = f"{pont_BOT}"

    elif escolha == "Tesoura":
        escol["text"] = "Robô escolheu:tesoura"
        pont_vc += 10
        pont_BOT += 0

        pontos_vc["text"] = f"{pont_vc}"
        pontos_bot["text"] = f"{pont_BOT}"
    

def papel():
    global pont_vc
    global pont_BOT
    
    lista = ["Pedra", "Papel", "Tesoura"]
    escolha = random.choice(lista)


    if escolha == "Pedra":
        escol["text"] = "Robô escolheu:pedra"
        pont_vc += 10
        pont_BOT += 0

        pontos_vc["text"] = f"{pont_vc}"
        pontos_bot["text"] = f"{pont_BOT}"

    elif escolha == "Papel":
        escol["text"] = "Robô escolheu:papel"
        pont_vc += 0
        pont_BOT += 0

        pontos_vc["text"] = f"{pont_vc}"
        pontos_bot["text"] = f"{pont_BOT}"

    elif escolha == "Tesoura":
        escol["text"] = "Robô escolheu:tesoura"
        pont_vc += 0
        pont_BOT += 10

        pontos_vc["text"] = f"{pont_vc}"
        pontos_bot["text"] = f"{pont_BOT}"

def tesoura():
    global pont_vc
    global pont_BOT
    
    lista = ["Pedra", "Papel", "Tesoura"]
    escolha = random.choice(lista)


    if escolha == "Pedra":
        escol["text"] = "Robô escolheu:pedra"
        pont_vc += 0
        pont_BOT += 10

        pontos_vc["text"] = f"{pont_vc}"
        pontos_bot["text"] = f"{pont_BOT}"

    elif escolha == "Papel":
        escol["text"] = "Robô escolheu:papel"
        pont_vc += 10
        pont_BOT += 0

        pontos_vc["text"] = f"{pont_vc}"
        pontos_bot["text"] = f"{pont_BOT}"

    elif escolha == "Tesoura":
        escol["text"] = "Robô escolheu:tesoura"
        pont_vc += 0
        pont_BOT += 0

        pontos_vc["text"] = f"{pont_vc}"
        pontos_bot["text"] = f"{pont_BOT}"

lb = Label(app, text="Pedra , Papel e Tesoura", font="Arial 15 bold").pack()

lb = Label(app, text="Você:", font="Arial 10 bold").place(x=10, y=50)
lb = Label(app, text="Robô:", font="Arial 10 bold").place(x=250, y=50)


pontos_vc = Label(app, text="0", font="Arial 30 bold")
pontos_vc.place(x=10, y=90)
pontos_bot = Label(app, text="0", font="Arial 30 bold")
pontos_bot.place(x=250, y=90)

escol = Label(app, text="", font="arial 13 bold")
escol.place(x=150, y=150)


bt = Button(app, text="Pedra", command=pedra).place(x=10, y=250)
bt2 = Button(app, text="Papel",command=papel).place(x=80, y=250)
bt3 = Button(app, text="Tesoura",command=tesoura).place(x=150, y=250)


app.mainloop()
