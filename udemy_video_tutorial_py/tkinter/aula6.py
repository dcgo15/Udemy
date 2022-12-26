from tkinter import *


def App():
    app = Tk()
    app.title("App")


    def app2():
        app.destroy()
        app2 = Tk()
        app2.title("app2")

        def app_novo():
            app2.destroy()
            App()

        bt = Button(app2, text="Voltar", command=app_novo).pack()

        app2.mainloop()

    bt = Button(app, text="Ir para app2", command=app2).pack()

    app.mainloop()



App()
