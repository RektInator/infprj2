class Translation:
	def __init__(self,key,value):
		self.key = key
		self.value = value
	def GetKey(self):
		return self.key
	def GetValue(self):
		return self.value

translations = []

def translate(key):
	for idx in translations:
		if idx.GetKey() == key:
			return idx.GetValue()

	return "Error"

def init():
	translations.append(Translation("Q1", "Thijs is homo"))
	