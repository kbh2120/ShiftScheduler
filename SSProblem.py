from logilab.constraint import *
import numpy

class SSProblem:
	def __init__(self, shifts, people):
		self.shifts = shifts
		self.people = people
	def solve(self):
		domains = {}

		print self.people

		for p in self.people:
			domains[p.attributes['Name']]=fd.FiniteDomain(self.shifts)
		constraints = []
		for p in self.people:
			for c in self.constraints:
				    constraints.append(fd.make_expression((p.attributes['Name'],),
                                          "%s[0] != '%s'"%(p.attributes['Name'],c.shift.start)))

		print constraints

		r = Repository(variables,domains,constraints)
		solutions = Solver().solve(r)

		print solutions

		#Printing solutions-- need to add to print to file instead of command line
		for s in solutions:
			dict = {}
			print "Solution " + str(solutions.index(s)) + ':'
			for a in s:
				print a + ':' + s[a][0]
				if s[a][0] in dict:
					dict[s[a][0]].append(a)
				else:
					dict[s[a][0]] = [a]
			list.append(dict)
			print '\n'
