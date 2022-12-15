from tkinter import *

app = Tk()
app.title("App1")

lb = Label(app, text="oi", bg="red").grid(row=0, column=1, columnspan=2, rowspan=1) #right, top, left, bottom

app.mainloop()
