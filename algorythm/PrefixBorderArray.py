import re

class PrefixBorderArray:


    def __init__(self, string):
        self.string = string
        self.borderArray = [0 for i in range(0,len(self.string))]

        self.execute()


    def execute(self):
        n = len(self.string)
        self.borderArray[0] = 0
        for i in range(1,n):
            borderPrefixRight = self.borderArray[i - 1]

            while borderPrefixRight and (self.string[i] != self.string[borderPrefixRight]) :
                borderPrefixRight = self.borderArray[borderPrefixRight - 1]
            
            if self.string[i] == self.string[borderPrefixRight]: self.borderArray[i] = borderPrefixRight + 1
            else: self.borderArray[i] = 0
        

    def __str__(self):
        return "Border array is: " + re.sub(r'\[|\]', '', str(self.borderArray)) 
