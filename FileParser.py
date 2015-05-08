from Person import *
from Shift import *
from pandas import *
from SSProblem import *

class FileParser:

	def __init__(self, in_file, out_path, shifts):
		self.in_file = in_file
		self.shifts = shifts
		self.all_people = []
		self.out_path = out_path

	# Read in CSV file and parse to create necessary objects for SS Problem
	def read_file(self):
		df = read_csv(self.in_file, skipinitialspace=True, true_values=[' Yes', 'Yes', 'Free', ' Free'], false_values=['No', ' No', 'Busy', ' Busy', ''])

		rows = map(list, df.values)
		num_ppl = len(rows)
		col_names = []
		shift_counter = 0
		first_shift_idx = len(rows)
		for i in range(len(df.columns)):
		    col_names.append(df.columns[i])
		    if df.columns[i].startswith('['):
		        if i < first_shift_idx:
		            first_shift_idx = i
		        # Create shift constraint
		        shift = Shift(shift_counter)
		        # Parse and add details
		        title = df.columns[i]
		        shift.set_str(title.strip('[]'))
		        a = title.strip('[]').split('(')
		       	if len(a) > 1:
			        shift_name = a[0][:-1]
			        shift_time = a[1].strip(')')
			        shift_start = shift_time.split(' - ')[0]
			        shift_end = shift_time.split(' - ')[1]
			        # set details
			        shift.set_name(shift_name)
			        shift.set_start(shift_start)
			        shift.set_end(shift_end)
		        self.shifts.append(shift)
		        shift_counter = shift_counter + 1
		        
		for row in rows:
		    p = Person()
		    # Add all attributes to Person object    
		    for j in range(1, first_shift_idx):
		        p.add_attribute(col_names[j], row[j])
		    # Add name attribute
		    p.add_name()

		    # List of available times
		    availability = row[first_shift_idx:]
		    for k in range(len(availability)):
		        if availability[k] == False:
		            p.add_constraint(self.shifts[k])
		    self.all_people.append(p)


	def create_SSProblem(self):
		self.read_file()

		self.prob = SSProblem(self.shifts, self.all_people)
		# Finds solution to problem given constraints, etc. from CSV file parsed above
		self.prob.solve(self.out_path)

