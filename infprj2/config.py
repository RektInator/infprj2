class Setting:
    def __init__(self, setting, value):
        self.setting = setting
        self.value = value
    def setting():
        return self.setting
    def value():
        return self.value

settings = []

def get(setting):
    for x in settings:
        if x.setting() == setting:
            return x.value()

    return ""

# todo, parse config file
def init():
    # test setting
    settings.append(Setting("snd_enabled", True))