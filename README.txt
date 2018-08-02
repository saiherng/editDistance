
-----------------------------------------------------------------------------------------
PROGRAMMING ASSIGNMENT 1 & 2 : Levenshtein Distance
-----------------------------------------------------------------------------------------

PROGRAM : editDistance.py
TEAM    : Sai Saing Toom Herng
DATE    : 2/27/2018
COMMENT : This program implements the Levenshtein Distance algorithm 
	  to compute the edit distance between two strings.  


Files Include
-------------
1. editDistance.py
2. weightMatrix.py
3. identity.txt
4. keyboard.txt
5. README.txt


---------
HOW TO RUN
---------

1 . Run "editDistance.py" program from Python3.0  
2 . Enter string1 and string 2
3 . Enter text file. Example: keyboard.txt  

******************************************************************************************************
Python Shell After Compile
----------------------------

This program computes the Levenshtein Distance of two strings.

Enter string 1: oslo 
Enter string 2: snow
Enter weighted matrix file name: identity.txt

oslo -> snow
[0, 1, 2, 3, 4]
[1, 1, 2, 2, 3]
[2, 1, 2, 3, 3]
[3, 2, 2, 3, 4]
[4, 3, 3, 2, 3]

distance:  3
oslo*
*snow

Continue? Enter 'y' or 'n': 

******************************************************************************************************
--------------------------------------------------------------------------------------
Structure of Program
--------------------------------------------------------------------------------------

editDistance.py  
---------------
def main(): 

	This is the main function in this program 

def editDistance(s1,s2) 
	
	This function takes in two strings as input. Implements the Levenshtein algorithm
	after initializing and creating a 2D array. 
	
	This function returns the computed matrix. 

def backTrack(m, s1, s2):

	This function takes in the computed matrix along side the two inputed strings.
	This function then backtracks the editDistance() function to find the operations 
	done on the two strings.

	This function returns trace (an inverted list of recorded operations),
	                      str1  (an inverted list containing the computed string1)
			      str2  (an inverted list containing the computed string2)
			      	

def printTrace(lst , str1, str2):

	This function takes in trace, str1 and str2 from above. 
	Prints the inverted list into non-inverted list to show operations done on the two strongs.
	

weightMatrix.py
---------------

class WeightedMatrix():

	This class takes in a matrix which contains the weight of each alphabets.

def __init__(self,filename):

	This function contructs and initializes the class. It takes in a filename 
	of the weight matrix. It processes the matrix into an array for indexing. 

def getWeight(self,ch1, ch2):

	This function takes in two characters (ch1, ch2) as input and indexes the weight from the array.
	
	Returns the weight of two alphabets 

def __str__(self):

	This is an extra function to print out the processed matrix from file.


_______________________________________________ END _______________________________________________________




