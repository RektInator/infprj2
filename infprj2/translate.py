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


def languageselect(x):
    if x == 1:
       return open("assets/nederlands.txt", "r")
    elif x == 2:
       return open("assets/english.txt", "r")
    else: return "No language specified"

def init():
    file = languageselect(1)
    data = file.read()
    for index in data.split("\n"):
        # Split key and value
        values = index.split(",")

        # Add translations to list
        _idx = Translation(values[0], values[1])
        translations.append(_idx)