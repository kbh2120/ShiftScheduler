from logilab.constraint import *
import numpy

variables = ('p1', 'p2', 'p3')
values = ['11 AM', '12 PM', '1 PM', '2 PM', '3 PM']

domains = {}
for v in variables:
    domains[v]=fd.FiniteDomain(values)

constraints = []

for conf in ('c03','c04','c05','c06'):
    constraints.append(fd.make_expression((conf,),
                                          "%s[0] != 'room C'"%conf))

for conf in ('c03','c04','c05','c06'):
    constraints.append(fd.make_expression((conf,),
                                          "%s[0] != 'room B'"%conf))

r = Repository(variables,domains,constraints)
solutions = Solver().solve(r)

list = []

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

stdevs = []

for i in list:
	sum = 0
	l = []
	for k in i.keys():
		l.append(len(i[k]))
	stdevs.append(numpy.std(l))

print stdevs
