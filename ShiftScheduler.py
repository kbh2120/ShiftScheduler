###############################################################################
# ShiftScheduler.py
# Main file 
###############################################################################

from FileParser import *
from Tkinter import *


class ShiftScheduler: 
	def __init__(self, csv_path, out_path):
		# Global shift array, must be passed into FileParser
		self.SHIFTS = []
		fp = FileParser(csv_path, out_path, [])
		fp.read_file()
		fp.create_SSProblem()


def callback(csv_path, out_path, root):
	ss = ShiftScheduler(csv_path.get(), out_path.get())
	csv_path.delete(0, 'end')
	out_path.delete(0, 'end')
	root.destroy()


def main():
	# Create GUI to provide information about input and output files
	master = Tk()
	master.minsize(300,200)
	master.geometry("600x300")
	master.title("ShiftScheduler - COMS3101 Python")
	title = Label(master, text="Welcome to ShiftScheduler! \n", font=("Helvetica", 22))
	title.pack()


	fp = Label(master, text="Please enter the file path where you saved the results from your Google form. ", font=("Helvetica", 14))
	fp.pack()

	instructions = Label(master, text="For example, if your Google doc csv file is called sample_data.csv and is saved in \n this directory, you should input ./sample_data.csv. ", font=("Helvetica", 12))
	instructions.pack()	
	csv = StringVar()
	csv_path = Entry(master, textvariable=csv)
	csv.set("./sample_data.csv")
	csv_path.pack()
	csv_path.focus_set()

	op = Label(master, text="\n\nPlease enter the file path where you would like to save your results. ", font=("Helvetica", 14))
	op.pack()

	out = StringVar()
	out_path = Entry(master, textvariable=out)
	out.set("out.txt")
	out_path.pack()
	out_path.focus_set()

	b = Button(master, text="Schedule Us!", width=30, height=20, command=lambda: callback(csv_path, out_path, master))
	b.pack()
	mainloop()

main()
