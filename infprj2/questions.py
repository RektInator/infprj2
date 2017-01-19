import pygame

class Question:
    def __init__(self,question,values):
        self.q = question
        self.v = values
    def Question(self):
        return self.q
    def Count(self):
        return self.v.count()
    def __getitem__(self,idx):
        return self.v[idx]

questions = []

def init():
    # open questions data
    file = open("assets\questions.txt", "r")
    data = file.read()
   
    for index in data.split("\n"):
        # Split key and value
        values = index.split(",")

        # Get amount of answers for this question
        cnt = int(values[1])

        # List of answer indices
        answers = []

        for i in range(1, cnt + 1):
            str = values[1] + "_ANSWER" + str(i)
            answers.append(str)

        # Create the question index
        _idx = Question(values[0], answers)
        questions.append(_idx)