class Setting:
    def __init__(self, setting, value):
        self.s = setting
        self.v = value
    def setting():
        return self.s
    def value():
        return self.v

settings = []

def get(setting):
    # for x in settings:
    #    if x.setting() == setting:
    #        return x.value()
    return ""

# todo, parse config file
def init():
    # test setting
    file = open("config.cfg", "r")
    data = file.read()
   
    for index in data.split("\n"):
        # Split key and value
        values = index.split(",")

        # Add setting to list
        _idx = Setting(values[0], values[1])
        settings.append(_idx)