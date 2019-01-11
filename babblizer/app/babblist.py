import json


class Babble:
	def __init__(self, dict):
		self.dict = dict

	def read_dict(self):
		self.babbledict = json.load(open(self.dict))

	def babble(self):	
		return self.babbledict["babble"]

	def other(self):
		return self.babbledict["other"]

	def open_dicts(self):
		self.read_dict()
		return self.babble(), self.other()