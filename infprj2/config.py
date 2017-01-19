class ConfigSetting:
    def __init__(self, setting, value):
        self.s = setting
        self.v = value
    def setting(self):
        return self.s
    def value(self):
        return self.v
    def set(self, value):
        self.v = value

settings = []

def get(setting):
    for x in settings:
       if x.setting() == setting:
           return x.value()
    return ""

def set(setting, value):
    for x in settings:
        if x.setting() == setting:
            x.set(value)
            break

# todo, parse config file
def init():
    # test setting
    file = open("config.cfg", "r")
    data = file.read()

    if not len(data):
        return
   
    for index in data.split("\n"):

        if not len(index):
            continue
        
        # Split key and value
        values = index.split(",")

        # Add setting to list
        _idx = ConfigSetting(values[0], values[1])
        settings.append(_idx)

# todo, rewrite config file on exit
def quit():
    file = open("config.cfg", "w")
    
    for index in settings:
        file.write(index.setting())
        file.write(",")
        file.write(index.value())
        file.write("\n")

    print("Saving new configuration...")

    pass