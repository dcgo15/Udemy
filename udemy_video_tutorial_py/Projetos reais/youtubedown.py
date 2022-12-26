from tkinter import *
from pytube import YouTube


link_ = "https://www.youtube.com/watch?v=6QFyxwe9IlY"


app = Tk()
app.title("Youtube downloader")
app.geometry("300x400")
app.resizable(0, 0)

def baixar():
    linkk = link.get()

    yt = YouTube(linkk)

    titulo = yt.title

    lin["text"] = f"Link:{linkk}"
    nom["text"] = f"Nome:{titulo}"

    yt.streams.filter().first().download()


lb = Label(app, text="Youtube Downloader",font="arial 15 bold", fg="red").pack()

lb = Label(app, text="Cole o link do vídeo aqui:", fg="red").pack()

link = Entry(app)
link.pack()

bt = Button(app, text="Baixar", fg="red", command=baixar).pack()

nom = Label(app, text="Nome:", fg="red")
nom.pack()
lin = Label(app, text="Link:", fg="red")
lin.pack()

app.mainloop()
