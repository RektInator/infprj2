import config
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
    if config.get("lang_select") == "1":  #Check config voor taal
        file = open("assets/english.txt", "r") #Open Taal
        print("Engels Geladen")
    else:
        file = open("assets/nederlands.txt", "r") #Open Taal
        print("Nederlands Geladen")
    data = file.read() #Lees taal
    for index in data.split("\n"):
        # Split key and value
        values = index.split(",")

        # Add translations to list
        _idx = Translation(values[0], values[1])
        translations.append(_idx)