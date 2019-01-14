#!/usr/bin/python
import json
from babblist import Babble
import random

class LookUpBabble:
	def __init__(self, dict, gimme):
		self.babble, self.other = Babble(dict).open_dicts()
		self.gimme = gimme

	def rand_babble(self):
		rand_pair = (random.choice(self.babble))
		return rand_pair[0]


