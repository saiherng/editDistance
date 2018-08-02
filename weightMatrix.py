"""
FILE    : weightMatrix.py
AUTHOR  : Sai Saing Toom Herng
DATE    : 2/20/2018
COMMENT : This class processes matrix from file.

MODIFIED:  
"""


class WeightedMatrix():


    def __init__(self, filename):
        
        self.filename = filename
        self.alphabets = "0 a b c d e f g h i j k l m n o p q r s t u v w x y z"
        self.alphabetIndex = self.alphabets.split()
        self.matrix = []
        
                 
        file = open(self.filename,"r")
        for item in file:
            self.matrix.append(item.split())

        file.close()

       
    def getWeight(self, ch1, ch2):

        ch1 = ch1.lower()
        ch2 = ch2.lower()

        if (ch1 == " ") or (ch2 == " "):
            return 1
        
        else:
            index1 = self.alphabetIndex.index(ch1) 
            index2 = self.alphabetIndex.index(ch2)

        return int(self.matrix[index1][index2])

        
    def __str__(self):

        for item in self.matrix:
            print(item)
