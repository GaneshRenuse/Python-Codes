from tkinter import *
from PIL import ImageTk, Image


if __name__ == "__main__":
    root = Tk()
    root.configure(background='light blue')
    root.title("test image app")
    root.geometry("600x300")

    frame = Frame(root, width=300, height=500, background="light blue")
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)

    # Create an object of tkinter ImageTk
    img = (Image.open("bank logo.png"))
    resizeimg = img.resize((150, 150), Image.LANCZOS)

    newimg = ImageTk.PhotoImage(resizeimg)
    label = Label(frame, image=newimg)
    label2 = Label(frame, text="GR\n Bank", background="light blue", font=('Helvatical bold', 40))

    label.grid(row=0, column=1)
    label2.grid(row=0, column=2)

    # start the gui
    root.mainloop()
