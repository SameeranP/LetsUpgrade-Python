'''
Panda has recently learned about ASCII values.He is very fond of experimenting. With his knowledge of ASCII values and character he has developed a special word and named it Panda's Magical word.

A word which consist of alphabets whose ASCII values is a prime number is an Dhananjay's Magical word. An alphabet is Panda's Magical alphabet if its ASCII value is prime.

Dhananjay's nature is to boast about the things he know or have learnt about. So just to defame his friends he gives few string to his friends and ask them to convert it to Panda's Magical word. None of his friends would like to get insulted. Help them to convert the given strings to Dhananjay's Magical Word.

Rules for converting:

1.Each character should be replaced by the nearest Panda's Magical alphabet.

2.If the character is equidistant with 2 Magical alphabets. The one with lower ASCII value will be considered as its replacement.

Input format:

First line of input contains an integer T number of test cases. Each test case contains an integer N (denoting the length of the string) and a string S.

Output Format:

For each test case, print Panda's Magical Word in a new line.

Constraints:

1 <= T <= 100

1 <= |S| <= 500

SAMPLE INPUT 
1
6
AFREEN

SAMPLE OUTPUT 
CGSCCO

Explanation
ASCII values of alphabets in AFREEN are 65, 70, 82, 69 ,69 and 78 respectively which are converted to 
CGSCCO with ASCII values 67, 71, 83, 67, 67, 79 respectively. All such ASCII values are prime numbers.
'''
import sympy

def fnc(num):
    prime_list = []
    for n in range(65, 123):
        if n > 1:
            for i in range(2, n):
                if (n % i) == 0:
                    break
            else:
                prime_list.append(n)
    x = min(prime_list, key=lambda x: abs(x-num))
    return x

def is_prime(num):
    num = int(num)
    if sympy.isprime(num):
        return num
    else:
        return 0

def main(k):
    N = int(input("Length of string: "))
    S = input("First name only: ")
    if N == len(S):   
        lst_final = []
        s_list = [char for char in S]
        for item in s_list:
            if ord(item) == is_prime(ord(item)):
                lst_final.append(ord(item)) 
            else:
                m = fnc(ord(item))
                lst_final.append(m)
        
        char_array = []
        for i in lst_final:
            char_array.append(chr(i))
        p = "".join(char_array)
        print(p,"\n")
        return k
    else:
        print("Please enter correct length of name")
        return k-1

T = int(input("No. of test cases: "))
if 1<=T<=100 :
    i = 0
    while i < T:
        main(i)
        
        i+=1

else:
    print("Enter number of test cases below 100 and above 1")