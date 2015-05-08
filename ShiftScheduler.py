###############################################################################
# ShiftScheduler.py
# Main file 
###############################################################################

from FileParser import *
from Tkinter import *


class ShiftScheduler: 
	def __init__(self, csv_path, out_path):
		#global shift array, must be passed into fileparser
		self.SHIFTS = []
		fp = FileParser(csv_path, out_path, [])
		fp.read_file()
		fp.create_SSProblem()

def callback(csv_path, out_path):
	ss = ShiftScheduler(csv_path, out_path)
	##fp = FileParser(csv_path, out_path, [])
	#fp.create_SSProblem()

def main():
	master = Tk()
	master.minsize(300,300)
	master.geometry("500x500")
	fp = Label(master, text="Welcome to ShiftScheduler! Please enter a csv file and an output file. ")
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
	b = Button(master, text="Schedule Us!", width=30, height=20, command=lambda: callback(csv_path.get(), out_path.get()))
	b.pack()
	mainloop()

main()