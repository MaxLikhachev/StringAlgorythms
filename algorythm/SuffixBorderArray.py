import re

class SuffixBorderArray:


    def __init__(self, string):
        self.string = string
        self.borderArray = [0 for i in range(0,len(self.string))]

        self.execute()


    def execute(self):
        n = len(self.string) 
        self.borderArray[n - 1] = 0
        for i in range(n-2,0):
            borderSuffixLeft = self.borderArray[i + 1]
            
            while borderSuffixLeft and (self.string[i] != self.string[n - borderSuffixLeft - 1]): 
                borderSuffixLeft = self.borderArray[n - borderSuffixLeft]

            if self.string[i] == self.string[n - borderSuffixLeft - 1]:  
                self.borderArray[i] = borderSuffixLeft + 1
            else:
                self.borderArray[i] = 0

    def __str__(self):
        return "Border array is: " + re.sub(r'\[|\]', '', str(self.borderArray)) 
