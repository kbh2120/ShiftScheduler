# Represents a shift: includes start time, end time, name of shift, and a shift ID
class Shift:
	def __init__(self, id):
		self.id = id
		self.str_rep = ''

	def set_start(self, start):
		self.start = start

	def set_end(self, end):
		self.end = end

	def set_name(self, name):
		self.name = name

	def set_str(self, string):
		self.str_rep = string

	def __str__(self):
		return self.str_rep
		
