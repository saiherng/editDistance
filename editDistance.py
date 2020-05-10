

"""
FILE    : editDistance.py
AUTHOR  : Sai Saing Toom Herng
DATE    : 2/12/2018
COMMENT : This program computes the Levenshtein Distance between two strings.

MODIFIED: A lot of little bugs fixed. Such as, unequal string lengths error - in progress
"""

from weightMatrix import*

def main():

     print("This program computes the Levenshtein Distance of two strings.\n")

     loop = 'y'
     while True:

        string1 = input("Enter string 1: ")
        string2 = input("Enter string 2: ")
        #fileName = input("Enter weighted matrix file name: ")

        #change matrix file name
        fileName = "identity.txt"


        global weightMatrix
        weightMatrix = WeightedMatrix(fileName)

        print()
        print(string1, "->", string2, end="\n")

        editMatrix = editDistance(string1,string2) #computes matrix
        distance = editMatrix[len(string1)][len(string2)] #extracts distance from matrix

        #prints the matrix
        for item in editMatrix:
            print(item)

        print()
        print("distance: ", distance, end= "\n")

        #backtracking matrix
        if (string1 != "" and string2 != ""):
            trace, str1, str2 = backTrack(editMatrix,string1, string2)
            printTrace(trace, str1, str2)
            print()


        loop = input("Continue? Enter 'y' or 'n': ")
        print()

        if (loop == 'n'):
             break



def editDistance(s1, s2):


    s1_r = len(s1) + 1  #string1 row
    s2_c = len(s2) + 1  #string2 column

    #initializing 2D array
    m = [[0 for a in range(s2_c)] for b in range(s1_r)]

    #initializing rows
    for i in range(1,s1_r):
        m[i][0] = i

    #initializing columns
    for i in range(1,s2_c):
        m[0][i] = i


    for j in range(1,s2_c):
        for i in range(1,s1_r):

            #checks if letters are similar
            if (s1[i-1] == s2[j-1]):
                cost = weightMatrix.getWeight(s1[i-1], s2[j-1])
                m[i][j] = m[i-1][j-1] + cost

            else:
                cost = weightMatrix.getWeight(s1[i-1],s2[j-1])

                #finds minimum of the three and adds one
                m[i][j] = min( m[i-1][j-1],     #substitute
                               m[i-1][j],       #delete
                               m[i][j-1] ) + cost  #insert

    return m


def backTrack(m, s1, s2):

    #sets index of latest minimum value in matrix
    i = len(s1)
    j = len(s2)

    s1 = " " + s1  #starting string index from 1
    s2 = " " + s2  #starting string index from 1

    trace = []  #array of operation in descending order
    str1 = []   #array of changes that will be made to string 1
    str2 = []   #array of changes that will be made to string 2

    while True:
        cost = weightMatrix.getWeight(s1[i],s2[j])
        mini = m[i][j]  #sets index of last traced minimum



        if s1[i] == s2[j]:
            #keeps track of equal letters
            trace.append(0)
            str1.append(s1[i])
            str2.append(s2[j])

            #changes index of i,j
            if i >= 0:
                 i = i-1
            if j >= 0:
                 j = j-1

        else:

            if ( mini == (m[i-1][j-1] +  cost) ) :

                #keeps track of substitution and letters
                trace.append(1)
                str1.append(s1[i])
                str2.append(s2[j])

                #changes index of i,j to minimum value
                if i >= 0:
                     i = i-1
                if j >= 0:
                     j = j-1

            elif ( mini == (m[i-1][j] + cost) ) :
                #keeps track of deletion and letters
                trace.append(2)
                str1.append(s1[i])
                str2.append("*")

                if i >= 0:
                     i = i-1 #changes index of i

            elif ( mini == (m[i][j-1]) + cost ):

                #keeps track of insertion and letters
                trace.append(3)
                str1.append("*")
                str2.append(s2[j])

                if j >= 0:
                     j = j-1 #changes index of j

        #loop breaks if backtrack reaches the last index
        if (i == 0 and j == 0):
            break


    return trace, str1, str2


def printTrace(lst, str1, str2):

    #prints operation executed 0-equals, 1-sub, 2- del, 3-insert
##    for i in reversed(lst):
##        print(i, end="")
##    print()

    #prints string1 changed list
    for i in reversed(str1):
        print(i,end="")
    print()

    #prints string2 changed list
    for i in reversed(str2):
        print(i,end="")
    print()


main()
