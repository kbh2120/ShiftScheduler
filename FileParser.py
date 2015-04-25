from Person import *
from Shift import *
from pandas import *

class FileParser:

	def __init__(self, in_file, shifts):
		self.in_file = in_file
		# url = './sample_data.csv'
		self.shifts = shifts
		self.all_people = []

	def read_file(self):
		df = read_csv(self.in_file, skipinitialspace=True, true_values=[' Yes', 'Yes', 'Free', ' Free'], false_values=['No', ' No', 'Busy', ])

		print df

		all_people = []
		rows = map(list, df.values)
		num_ppl = len(rows)
		# del df['Timestamp']
		col_names = []
		shift_counter = 0
		first_shift_idx = len(rows)
		for i in range(len(df.columns)):
		    col_names.append(df.columns[i])
		    if df.columns[i].startswith('['):
		        if i < first_shift_idx:
		            first_shift_idx = i
		        # create shift constraint
		        self.shifts.append(Shift(shift_counter))
		        shift_counter = shift_counter + 1
		        
		for row in rows:
		    p = Person()
		    # add all attributes to Person object    
		    for j in range(1, first_shift_idx):
		        p.add_attribute(col_names[j], row[j])
		        print '********'
		        print col_names[j]
		        print row[j]

		    # list of available times
		    availability = row[first_shift_idx:]
		    for k in range(len(availability)):
		        if availability[k] == False:
		            p.add_constraint(self.shifts[k])
		    all_people.append(p)


		print all_people[0].attributes
		print all_people[0].constraints[0].id

	def create_SSProblem(self):
		self.read_file()
		self.prob = SSProblem(self.shifts, self.all_people)
		#outputs txt file with solutions
		self.prob.solve()

