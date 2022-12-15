from tkinter import *


def App1():
    app = Tk()
    app.title("Janela 1")

    def App2():
        app.destroy()

        app2 = Tk()
        app2.title("Janela 2")

        Label(app2, text="Janela 2").pack()

        Button(app2, text="Voltar", command=App1).pack()

        app2.mainloop()
        

    Label(app, text="Janela 1").pack()

    Button(app, text="Ir pra janela 2", command=App2).pack()
    
    app.mainloop()


App1()
