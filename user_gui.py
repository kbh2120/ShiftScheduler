from Tkinter import *
from ShiftScheduler import * 

master = Tk()
master.minsize(300,300)
master.geometry("500x500")

fp = Label(master, text="Enter full csv path: ")
fp.pack()
csv_path = Entry(master)
csv_path.pack()
csv_path.focus_set()

op = Label(master, text="Enter full outfile path: ")
op.pack()
out_path = Entry(master)
out_path.pack()
out_path.focus_set()



def callback():
    print csv_path.get() + outfile.get()

b = Button(master, text="Schedule Us!", width=30, height=20, command=callback)
b.pack()
mainloop()
