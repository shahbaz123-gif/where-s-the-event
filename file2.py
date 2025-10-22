# imoprt necessary libraries
from tkinter import *
from tkinter import messagebox

#setup Tkinter window
root = Tk()
root.geometry("400x400")

#function for displaying warning message
#this will be called once the button is clicked
#messagebox.showwarning("eindow name", "text to be displayed")
def msg():
    messagebox.showwarning("alert", "stop! virus found.")

#adding button widgets to window
button = Button(root, text="scan for virus", command=msg)
button.place(x=40, y=80)
 
def msg2():
    messagebox.showinfo("information","there are here") 

button = Button(root, text="info", command=msg2)
button.place(x=50, y=80)    
def msg3():
    messagebox.showerror("error","something went wrong") 

button = Button(root, text="error", command=msg3)
button.place(x=60, y=80)
def msg4():
    messagebox.askquestion("question","why you here") 

button = Button(root, text="question", command=msg4)
button.place(x=70, y=80)
def msg5():
    messagebox.askokcancel("okcancel","press if you want to cancel") 

button = Button(root, text="cancel", command=msg5)
button.place(x=50, y=100)
def msg6():
    messagebox.askyesno("yes or no","yes or no") 

button = Button(root, text="yes or no", command=msg6)
button.place(x=40, y=80)
def msg7():
    messagebox.askretrycancel("retry or cancel","retry or cancel") 

button = Button(root, text="retry cancel", command=msg7)
button.place(x=40, y=80)

#entering main event loop
root.mainloop()