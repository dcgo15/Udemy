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

    yt_ti = str(yt.title)
    
    lb2["text"] = f"Titulo:{yt_ti}"
    lb3["text"] = f"Link:{linkk}"


    yt.streams.filter().first().download()

lb = Label(app, text="Youtube downloader", fg="red", font="arial 14 bold").pack()

lb = Label(app, text="Cole o link aqui:", fg="red", font="arial 9 bold").pack()

link = Entry(app)
link.pack()

bt = Button(app, text="Baixar",command=baixar).pack()


lb2 = Label(app, text="Titulo:", fg="red", font="arial 6 bold")
lb2.place(x=20, y=150)
lb3 = Label(app, text="Link:", fg="red", font="arial 6 bold")
lb3.place(x=20, y=180)



app.mainloop()
