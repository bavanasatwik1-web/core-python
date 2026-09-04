#  Create a class Animal with make_sound() and derived classes Dog, Cat, Cow that override it. 
# Demonstrate polymorphism by iterating over a list of different animal objects and calling make_sound(). 

# class Animal:
#     def make_sound(self):
#         print("Animal")
# class Dog(Animal):
#     def make_sound(self):
#         print("Dog")
# class cat(Animal):
#     def make_sound(self):
#         print("Cat")
# class Cow(Animal):
#     def make_sound(self):
#         print("Cow") 
# Animals=[Animal(),Dog(),cat(),Cow()]
# for i in Animals:
#     i.make_sound()
#                               
#  Write a function operate(device) that calls device.start().
# Pass in objects of Car, Computer, and WashingMachine — all of which define a start() method, but share no inheritance relationship. 
# Show that Python’s polymorphism works through behavior, not type. 

# class car:
#     def start(self):
#         print("car")
# class computer:
#     def start(self):
#         print("computer") 
# class washingmachine:
#     def start(self):
#         print("washing") 
# a1=washingmachine()
# a2=computer()
# a3=car()
# def operate(device):
#     device.start()
# operate(a1)
# operate(a2)
# operate(a3)

# Q3. Create a Vector class that supports: • + operator → add coordinates • == operator → 
# compare equality Show how operator overloading gives natural polymorphism to user-defined classes. 

# class Vector:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def __add__(self,other):
#         return Vector(self.x+other.x,self.y+self.y)
#     def __str__(self):
#         return f"x={self.x},y={self.y}"
# v1=Vector(1,9)
# v2=Vector(9,6)
# v3=Vector(8,9)
# print(v1+v2)
# print(v1+v2+v3)    
    
# Q4. Create a base class Transport with move() and derived classes Bus and
#  Bike that override it but also call the parent implementation using super().
#  Show the combination of reuse + custom behavior. 
    
# class Transport:
#     def move(self):
#         print("transport")
# class Bus(Transport):
#     def move(self):
#         super().move()
#         print("bus")
# class Bike(Transport):
#     def move(self):
#         super().move()
#         print("Bike")
# k=Bike()
# k.move()        
# l=Bus()
# l.move()

# Q8. Create: • Base Account → withdraw() • Subclass SavingsAccount → modifies withdraw()
# • Subclass PremiumSavingsAccount → overrides again but calls parent using super() Show how polymorphism works across multiple levels. 

# class Account:
#     def withdraw(self):
#         print("Account withdraw")
# class SavingsAccount(Account):
#     def withdraw(self):
#         super().withdraw()
#         print("Savngsacc withdraw")
# class premiumSavingsacc(SavingsAccount):
#     def withdraw(self): 
#         super().withdraw()
#         print("premium withdraw")
# k1=premiumSavingsacc()
# k1.withdraw()        


class Numbers:

    def __init__(self, n):
        self.n = n
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.num <= self.n:
            value = self.num
            self.num += 1
            return value
        else:
            raise StopIteration


# n = int(input("Enter N: "))

numbers = 5

for i in numbers:
    print(i)