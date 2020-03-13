import re

class Naive:


    def __init__(self, string, pattern):
        self.string = string
        self.pattern = pattern
        self.positions = []

        self.execute()


    def execute(self):
        n = len(self.string)
        m = len(self.pattern)
        for i in range(0, n - m):
            j = 0
            while j < m and self.pattern[j] == self.string[i + j]: j += 1
            if j == m: self.positions.append(i)


    def __str__(self):
        if self.positions.__len__() == 0: return "String to small or no found pattern \"" + self.pattern + "\"" 
        return "Find pattern \"" + self.pattern + "\" in positions: " + re.sub(r'\[|\]', '', str(self.positions))
