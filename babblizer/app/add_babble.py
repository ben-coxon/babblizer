import json


class AddBabble:
	def __init__(self, dict, yousay, isay):
		self.old_dict = dict
		self.dict = json.load(open(dict))
		self.babble = self.dict["babble"]
		self.other = self.dict["other"]
		self.yousay = unicode((str(yousay)).lower(), 'utf_8')
		self.isay = unicode((str(isay)).lower(), 'utf_8')


	def check_babble_isay(self):  # to see if words already exist for isay
		for i in range(0, len(self.babble)):
			if self.babble[i][0] == self.isay:
				return True, 0
			elif self.babble[i][1] == self.isay:
				return True, 1
		return False

	def check_babble_yousay(self):  # to see if words already exist for isay
		for i in range(0, len(self.babble)):
			if self.babble[i][0] == self.yousay:
				return True, 0
			elif self.babble[i][1] == self.yousay:
				return True, 1
		return False

	def check_other(self, say):
		for i in self.other:
			if i == say:
				return True


	def organize(self):
		change = False
		if not self.check_babble_isay():
			if not self.check_babble_yousay():
				self.babble.append([self.yousay, self.isay])
				
				if self.check_other(self.yousay):
					self.other.remove(self.yousay)
				if self.check_other(self.isay):
					self.other.remove(self.isay)

				self.update_dict()
				return "Babble added!"


		if not self.check_babble_isay() and self.check_babble_yousay():
			if not self.check_other(self.isay):
				self.other.append(self.isay)
			change = True
			resp = "One of them is already a babble."

		elif self.check_babble_isay and not self.check_babble_yousay():
			if not self.check_other(self.yousay):
				self.other.append(self.yousay)
			change = True
			resp = "One of them is already a babble."

		if change:
			self.update_dict()
			return resp
		else:
			return "Great minds think alike!"


	def update_dict(self):
		new_dict = {"babble" : self.babble, "other" : self.other}
		print new_dict
		with open(self.old_dict, 'w') as fp:
   			json.dump(new_dict, fp)


	def add(self):
		return self.organize()





