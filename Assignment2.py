#Question 1: Pilot, if-else-elif
q = input("What is the altitude?")
p = int(q)
if p<1000:
     print("It's safe to land")
elif p>1000 and p<5000:
    print("Bring down to 1000")
else:
    print("Turn Around")

#Question 2: for loop to print prime numbers 1-200
list1 = []
for i in range(2,201):
    for j in range(2,i//2):
        if (i % j) == 0:
                break

    else:
        list1.append(i)
print(list1)

#Question 3: Armstrong Number between 1042000 and 702648265, use while loop
lower = 1042000
upper = 702648265

for num in range(lower, upper + 1):

   # order of number
   order = len(str(num))
    
   # initialize sum
   sum = 0

   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print(num)
       break
