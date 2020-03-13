import re

class NaiveMaxBorder:


    def __init__(self, string):
        self.string = string
        self.maxborder = 0

        self.execute()


    def execute(self):
        n = len(self.string)
        border = 0
        i = n-1
        while not border and i:
            j = 0;
            while j < i and self.string[j] == self.string[n-i+j]: j += 1 
            if j == i: border = i
            i -= 1
        
        self.maxborder = border;


    def __str__(self):
        return "Max border is: " + str(self.maxborder)
