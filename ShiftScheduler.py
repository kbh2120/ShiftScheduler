###############################################################################
# ShiftScheduler.py
# Main file 
###############################################################################

from FileParser import *


class ShiftScheduler: 
	def __init__(self):
		#global shift array, must be passed into fileparser
		self.SHIFTS = []
		fp = FileParser('./sample_data.csv', self.SHIFTS)
		fp.create_SSProblem()

def main():
	ss = ShiftScheduler()


main()
