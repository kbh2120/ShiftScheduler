# global shift array, must be passed into fileparser

SHIFTS = []

from FileParser import *

fp = FileParser('./sample_data.csv', SHIFTS)
fp.read_file()