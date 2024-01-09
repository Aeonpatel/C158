from tkiinter import*
from PIL import ImageTK, Image
from tkinter import messagebox

root=Tk()
root.title("Credit Card Checking")
root.geometry("600x400")
root.configure(background = "gold")

input_box = Entry(root)
input_box.pack()

img = ImageTk.PhotoImage(Image.open(""))
label = Label( root , image=img )

def Authentication():
    try:
        input_b = int(input_box.get())
        messagebox.showinfo("Credit Card number is valid")
    except(ValueError):
        messagebox.showinfo("Your Credit Card number is not valid")

btn_1 = Button(root,text="Check Credit Card",command=Authentication)
btn_1.pack()
label.pack()

root.mainloop()