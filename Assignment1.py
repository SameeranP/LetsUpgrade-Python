list1 = ["Harry", 1, "Delhi"]
list2 = ["salman", "sanjay", "salman"]

list1.append(list2) #appends the entire list as one single element
print(list1)

list1.reverse() #reverse the order of list
print(list1)

list1.pop() #last elemnt deleted
print(list1)

list1.extend(list2) #appends every element of other list as different elements
print(list1)

count = list1.count("salman") #number of times "salman" element occurs
print(count)

#####################################################################################################################################################
'''Dictionary'''

car = {"brand": "Kia", "model": "Celtos","year": 2019}

yr = car.get("year")
print(yr)

val = car.items()
print(val)

key = car.keys()
print(key)

car.pop("year")
print(car)

car.clear()
print(car)
#########################################################################################################################################################
'''Sets'''

set1 = {"apple", "banana", "cherry"}
set1.add("orange")
print(set1)

set1.discard("cherry")
print(set1)

y = {"google", "microsoft", "apple"}
z = set1.union(y)
print(z)

set1.clear()
print(set1)

a = {"a", "b", "c"}
b = {"f", "e", "d", "c", "b", "a"}
c = a.issubset(b)
print(c)
######################################################################################################################################################
'''Tuples'''
thistuple = ("apple", "banana", "cherry","apple","apple")
print(thistuple)

x = thistuple.count("apple")
print(x)

y = thistuple.index("cherry")
print(y)

##############################################################################################################################################################
'''Strings'''
txt = "Toh Kaise hai aap loG"
x = txt.upper()
print(x)

y = x.lower()
print(y)

print(y.capitalize())

j = txt.split()
print(j)

k = ' # '.join(j)
print(k)

print(txt.find("G"))

f = txt.replace("Toh","Woh")
print(f)

swapped = txt.swapcase()
print(swapped)