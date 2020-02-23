import re

class Naive:


    def __init__(self, text, pattern):
        self.text = text
        self.pattern = pattern
        self.positions = []

        self.execute()


    def execute(self):
        n = len(self.text)
        m = len(self.pattern)
        for i in range(0, n - m):
            j = 0
            while j < m and self.pattern[j] == self.text[i + j]: j=j+1
            if j == m: self.positions.append(i)


    def __str__(self):
        return "Find pattern \"" + self.pattern + "\" in positions: " + re.sub(r'\([^()]*\)', '', str(self.positions))
#   """   

# if __name__ == '__main__':
#     filepath = input("Enter file's name: ")
#     file = open(filepath)
#     text = '_'.join(file.readlines())

#     pattern = input("Enter pattern: ")

#     print("Text: ", text)
#     print("Pattern: ", pattern)
#     print("Found pattern in positions:", naive_string_matcher(text,pattern))
#  """