#!/usr/bin/python
from babblist import Babble
from add_babble import AddBabble
from lookup_babble import LookUpBabble
import random


dict = "app/babbledict.json"


class BenTest():
	def __init__(self, words):
		if words.find(" ") != -1:
			self.words = words.lower()[:words.find(" ")]
		else: self.words = words.lower() 

		self.babble, self.other = Babble(dict).open_dicts()



	def fnord(self):
		for i in range(0, len(self.babble)):
			if self.babble[i][0] == self.words:
				return (self.babble[i][1]).capitalize() + "!"
			elif self.babble[i][1] == self.words:
				return (self.babble[i][0]).capitalize() + "!"
			
		return (random.choice(self.other)).capitalize() + "!"


class NewBabble:
	def __init__(self, yousay, isay):
		self.yousay = yousay
		self.isay = isay

	def new_babble(self):
		return AddBabble(dict, self.yousay, self.isay).add()

class GimmeBabble:
	def __init__(self, gimme):
		self.gimme = gimme

	def gimme_babble(self):
		return LookUpBabble(dict, self.gimme).rand_babble()



