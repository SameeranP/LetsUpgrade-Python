# #Question 1 file handling
# import sys
# print("Question 1: File handling\n \n")
# f = open('myfile.txt', 'r')
# try:
    
#     f.write("Mumbo jumbo \n")

# except:
#     print("There is an error:", sys.exc_info()[0])

# finally:
#     f.close()

#Question 2 : is a given number prime or not and do Unit Testing on it using PyLint & Unittest Library
import sympy
'''
Module to check prime Number
'''
def checkPrimeNumber(num):
    '''
    Function to Check Prime takes a Input
    '''
    if sympy.isprime(num):
        '''
        if statement
        '''
        return num
    else:
        return "No Prime"