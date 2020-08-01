# Question 1 : function for prime number, filter out primes from 1-2500
print("Question 1 : function for prime number, filter out primes from 1-2500\n\n")
def isPrime(num):
    if num>1:
        for i in range(2,num):
            if num % i == 0:
                return False
        else:
            return True
    else:
        return False

numlist = list(range(1,2501))
primelist = filter(isPrime, numlist)
print(list(primelist))

# Question 2: Lambda function for Capitalizing whole sentence passed as arg. Map all sentences in the list with lambda function
print("Question 2: Lambda function for Capitalizing whole sentence passed as arg. Map all sentences in the list with lambda function\n\n")
lst1 = ["hey this is sai","i am in mumbai","how are you"]
newlst = list(map(lambda x: x.title(), lst1 ))
print(newlst)