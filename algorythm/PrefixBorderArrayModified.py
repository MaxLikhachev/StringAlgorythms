import re
import algorythm.PrefixBorderArray

class PrefixBorderArrayModified:


    def __init__(self, string):
        self.string = string
        self.borderArray = algorythm.PrefixBorderArray(string).borderPrefixs
        self.borderArrayModified = [0 for i in range(0,len(self.string))]

        self.execute()


    def execute(self):
        n = len(self.string)
        self.borderArrayModified[0] = 0
        self.borderArrayModified[n-1] = self.borderArray[n-1]
        
        for i in range(1, n-1):
        
            if (self.borderArray[i] and (self.string[self.borderArray[i]] == self.string[i+1])):
                self.borderArrayModified[i] = self.borderArrayModified[self.borderArray[i] - 1]
            else: 
                self.borderArrayModified[i] = self.borderArray[i]
        

    def __str__(self):
        return "Modified border array is: " + re.sub(r'\[|\]', '', str(self.borderArrayModified)) 
