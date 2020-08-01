# Question 1: bank account
print("Question1: bank Account")
class Bank():
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, balance):
        self.balance+=  balance
        return self.balance
    
    def withdraw(self,balance):
            if self.balance >= balance:
                self.balance-=balance
            else:
                return 'Only ' + str(self.balance) + ' is avaliable'
            return self.balance
a1 = Bank('a1',100)
print(a1.deposit(900))
print(a1.withdraw(5000))
print(a1.withdraw(200))

# Q2. Volume and surface area of cone
print("\n \n Q2. Volume and surface area of cone") 
import math
class Cone:
    def __init__(self,r=1,h=1):
        self.r = r
        self.h = h
        self.volume =0
        self.surface_area = 0
    def volume_fun(self):
        self.volume = math.pi * self.r * self.r * (self.h/3)
        return self.volume
    def surface_area_fun(self):
        base = math.pi * self.r * self.r
        side = math.pi * self.r * math.sqrt(self.r**2 + self.h**2)
        self.surface_area = base + side
        return self.surface_area

cone1 = Cone(5,7)
print(cone1.volume_fun())