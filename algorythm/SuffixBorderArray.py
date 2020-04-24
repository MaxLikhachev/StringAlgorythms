import re

class SuffixBorderArray:


    def __init__(self, string):
        self.string = string
        self.borderSuffixs = [0 for i in range(len(self.string))]

        self.execute()


    def execute(self):
        n = len(self.string) 
        self.borderSuffixs[n - 1] = 0
        for i in range(n-2, -1, -1):
            borderSuffixLeft = self.borderSuffixs[i + 1]
            
            while borderSuffixLeft and (self.string[i] != self.string[n - borderSuffixLeft - 1]): 
                borderSuffixLeft = self.borderSuffixs[n - borderSuffixLeft]

            if self.string[i] == self.string[n - borderSuffixLeft - 1]:  
                self.borderSuffixs[i] = borderSuffixLeft + 1
            else:
                self.borderSuffixs[i] = 0

    def __str__(self):
        return "Border array is: " + re.sub(r'\[|\]', '', str(self.borderSuffixs)) 
