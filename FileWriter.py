class FileWriter:
	def __init__(self, soln, shifts):
		self.solutions = soln
		self.shifts = shifts
	def writeFile(self):
		f = open('output.txt','w')
		for s in self.solutions:
			f.write('Solution ' + str(self.solutions.index(s)) + ':\n')
			for curr in s:
				f.write(curr+': ')
				f.write(str(self.shifts[int(s[curr])]))
				f.write('\n')
			f.write('\n')
		f.close()
