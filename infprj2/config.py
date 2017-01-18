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
    settings.append(Setting("snd_enabled", "1"))