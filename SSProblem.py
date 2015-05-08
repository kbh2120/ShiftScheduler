from logilab.constraint import *
import numpy
from FileWriter import *

class SSProblem:
	def __init__(self, shifts, people):
		self.shifts = shifts
		self.people = people
	def solve(self, out_path):
		domains = {}
		names = []
		
		shift_ids = []
		for s in self.shifts:
			shift_ids.append(str(s.id))

		for p in self.people:
			domains[p.attributes['Name']]=fd.FiniteDomain(shift_ids)
			names.append(p.attributes['Name'])

		names = tuple(names)

		constraints = []
		for p in self.people:
			for c in p.constraints:
				    constraints.append(fd.make_expression((p.attributes['Name'],),
                                          "%s[0] != '%s'"%(p.attributes['Name'],c.id)))

		r = Repository(names,domains,constraints)
		solutions = Solver().solve(r)

		if not solutions:
			print 'No solutions found'
			return


		f = FileWriter(solutions, self.shifts)
		f.writeFile(out_path)
