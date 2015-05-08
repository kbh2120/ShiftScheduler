# Prints output file with all possible schedules in two formats-- by name and by shift
class FileWriter:
	def __init__(self, soln, shifts):
		self.solutions = soln
		self.shifts = shifts
	def writeFile(self, out_path):
		# Print all possible schedules-- put shift for each name
		f = open(out_path,'w')
		f.write('Schedule by Name\n')
		f.write('----------------\n\n')
		for s in self.solutions:
			f.write('Solution ' + str(self.solutions.index(s)) + ':\n')
			for curr in s:
				f.write(curr+': ')
				f.write(str(self.shifts[int(s[curr])]))
				f.write('\n')
			f.write('\n')

		# Add solutions to dictionary in order to print by shift instead
		list = []
		for s in self.solutions:
			dict = {}
			for curr in s:
				tmp = str(self.shifts[int(s[curr])])
				if tmp in dict:
					dict[tmp].append(curr)
				else:
					dict[tmp] = [curr]
			list.append(dict)


		# Print all possible schedules-- put names that correspond to each shift
		f.write('Schedule by Shift\n')
		f.write('----------------\n\n')

		for l in list:
			f.write('Solution: '+str(list.index(l))+'\n')
			for curr in l:
				s = ''
				for a in l[curr]:
					s = s + a + ', '
				f.write(curr + ': ' + s[:-2]+'\n')
			f.write('\n')

		f.close()
