# question 1: Fibonacci series
print("Question 1: Fibonacci series\n \n")
n = int(input("Enter the value of 'n': "))
a = 0
b = 1
sum = 0
count = 1
print("Fibonacci Series: ", end = " ")
while(count <= n):
  print(sum, end = " ")
  count += 1
  a = b
  b = sum
  sum = a + b

#Question 2 file handling
print("Question 2: File handling\n \n")
with open('myfile.bin', 'wb+') as file:
    b = bytearray(b'I love lets upgrade')
    file.write(b)

file.close()

with open('myfile.bin', 'rb') as file:
    p = file.read()
    print(p.decode("utf-8"))

with open('myfile.bin', 'ab+') as file:
    b = bytearray(b'\nWe all love python classes with LU')
    file.write(b)


with open('myfile.bin', 'rb') as file:
    p = file.read()
    print(p.decode("utf-8"))

file.close()


#Question3 : static movie recommendation system
print("Question3 : static movie recommendation system\n \n")
import random
Thriller = "Salt, No one killed Jessica, Ittefaq , Special 26,Talaash,Gupt,NH 10, Ugly,Mahal,Sangharsh,Black swann, War,Abduction, Drive, Resident,Hanna, Sherlock Holmes,Wrecked,Kahaani,Stolen, Taken 2,Chronicle,Drishyam,Cold pursuit, Batman, the dark knight, Raazi, Uri,Kidnap,Bluffmaster, Gupt"
RomCom = "Love Aaj kal, Cocktail, Wake up Sid, jab we met, Band baaja Baarat,the Photograph, Palm springs, love Simon, Mubarakan, Sweet live, Trainwreck, 2 States, Shudhh Desi romance, Luka chupi, Chhichore, YJHD, ZNMD, Kal ho na ho, Ajab prem ki gazab kahaani,Tanu weds Manu, Saathiya, Bunty Aur Babli, Yess boss" 
Action = "Dabaang, Bodyguard, Jai ho, Tubelight, Ra-one, Die hard, Black widow, BangBang, Day and knight, Bloodshot, malang, Taanhaji, Attack, X-men, Wasabi, Rush hour, Hero, MIB, Steal, XXX, Hulk, Daredeveil, Warzone,Matrix, Tube,Catwoman, Kung fu hustle,Wanted, Wolverine, Apocalypse, 2012, Matrix- revolution,"
Anime = "Cars, Finding nemo, Up, Finding Dory, Lion King, Aladdin, Frozen, Coco, Wreck it ralph, Moana, Zootopio, Madagascar, Shrek, Shrek 2, Planes, Brave, Ponyo, Tangled, Toy story, Bambi, Tarzan, Spiderman, Snow white, Cinderella, Kung fu panda, Naruto, Ben 10, Dragon ball Z, Avatar, HAunted house "
thriller = Thriller.split(",")
romcom = RomCom.split(",")
action= Action.split(",")
anime = Anime.split(",")

y = input("Type a genre(Thriller/RomCom/Action/Anime): ")
y.strip()
x = y.lower()

#print(x)
if x == "thriller":
    print(random.choice(thriller).capitalize())
    print(random.choice(thriller).capitalize())
    
elif x == "romcom":
    print(random.choice(romcom).capitalize())
    print(random.choice(romcom).capitalize())
    

elif x == "action":
    print(random.choice(action).capitalize())
    print(random.choice(action).capitalize())
elif x == "anime":
    print(random.choice(anime).capitalize())
    print(random.choice(anime).capitalize())
else:
    print("Please select genre from the given options")