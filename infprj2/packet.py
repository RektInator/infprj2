class Packet:
    def __init__(self, data = ""):
        self.data = data
    def append(self, str):
        self.data += str
    def get(self):
        return bytes(self.data + "{END}", "utf-8")