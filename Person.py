
# person has constraints and information

class Person:
	def __init__(self): 

		# any other information about the person you want to add
		self.attributes = {} 
		
		# list of shifts the person cannot make
		self.constraints = [] 

	# add attribute method, contains a dictionary of any person attribute you want to add
	def add_attribute(self, attribute_name, attribute_value):
		self.attributes[attribute_name] = attribute_value

	def add_constraint(self, shift):
		self.constraints.append(shift)

	def add_name(self):
		if 'First Name' in self.attributes and 'Last Name' in self.attributes:
			self.attributes['Name'] = self.attributes['First Name'] + ' ' + self.attributes['Last Name']
