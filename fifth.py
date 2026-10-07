from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Reading Schedule Planner")
root.configure(bg="grey")
root.geometry("650x400")
l1 = Label(root,text="Hey user! Welcome to Reading Schedule Planner",bg="grey")
def topwindow():
    top = Toplevel()
    top.title("Reading Schedule Calculator")
    top.configure(bg="lightblue")
    top.geometry("600x600")
    l2 = Label(top,text="Enter total number of pages in the book",bg="blue")
    
    e = Entry(top)
    
    l3 = Label(top,text="Enter number of pages you plan to read each day",bg="blue")
    
    e5 = Entry(top)
    
    def calculate():
            try:
                
                pages = int(e.get())

                daily_pages = int(e5.get())
                if pages <= 0 or daily_pages <= 0:
                    messagebox.showerror("Error","Please enter numbers greater than 0")
                    return
                reading_days = pages // daily_pages
                remaining_pages = pages % daily_pages
                message = f"Remaining reading days are{reading_days} and the remaining pages are {remaining_pages}"
                #e7.delete(0, END)
                
                e7.insert(END, str(message))
                
            except ValueError:
                messagebox.showerror("Error","PLEASE ENTER VALID WHOLE NUMBERS")
                
    b2 = Button(top,text="Calculate",command=calculate)
    b2.place(x=260, y=190)
    e7 = Text(top,height = 4)
    e7.place(x= 10,y= 100)
    l2.place(x = 100,y = 280)
    l3.place(x= 100,y= 320)
    e.place(x=320, y=280)
    e5.place(x=320, y=320)
def message():
    box = messagebox.showinfo("Alert","Do you want to calculate your reading schedule?")
    if box == "ok":
        topwindow()
b1 = Button(root,text="Let's get started",bg="yellow",fg="black",command=message)
b1.place(x=260, y=360)
root.mainloop()
