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
    file = open("assets/nederlands.txt", "r")
    data = file.read()

    for index in data.split("\n"):
        # Split key and value
        values = index.split(",")

        # Add translations to list
        _idx = Translation(values[0], values[1])
        translations.append(_idx)