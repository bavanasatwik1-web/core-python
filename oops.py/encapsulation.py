# class A:
#     def __init__(self):
#         self._x=5
#         self.__y=10
#     def getx(self):
#         if input()=="1234":
#             return self._x
#         return None
#     def setx(self, value):
#         if value >27:
#             self._x=value
#         else:
#             print("value of x should be greater than 27")
#     @property
#     def __ac(self):
#         return self._x
#     @__ac.setter
#     def fs(self, value):
#         self._x=value
#     def gety(self):
#         return self.__y
#     def sety(self, value):
#         self.__y=value
# obj=A()
# obj.fs=10
# print(obj.getx())
# print(obj._x)
# print(obj._A__y)#name mangling
# print(obj.getx())
# print(obj.gety())
# obj.setx(100)
# print(obj.getx())

# class BankAccount:
#     def __init__(self,name):
#         self.name=name
#         self._balance=0
#         self.__atmpin="1234"
#     def getbalance(self):
#         return self._balance
#     def setpin(self,pin):
#         if input("enter previous atm pin: ")==self.__atmpin:
#             self.__atmpin=pin
#         else:
#             print("pin incorrect")
# class UPI(BankAccount):
#     def sendmoney(self,amount):
#         if self._balance>amount:
#             self._balance=self._balance-amount
#         else:
#             print("insufficient balance")
#     def receivemoney(self,amount):
#         self._balance=self._balance+amount
# b1=BankAccount("madhu")
# print(b1.getbalance())
# upi=UPI("madhu")
# print(upi.getbalance())
# upi.sendmoney(100)
# upi.receivemoney(1000000000000)
# upi.sendmoney(100)
# print(upi.getbalance())
# b1.setpin("12345")
# b1.setpin("3456")

# 1.  Create a BankAccount class that stores:
#  • account number • balance (should not be directly modifiable) You must:
#  1. Make the balance attribute inaccessible from outside.
#  2. Provide functions to deposit/withdraw that validate the amount. 
#  3. Prevent withdrawal if balance becomes negative. 
#  4. Show what happens if someone tries to modify balance directly and why encapsulation prevents it

# class Bankaccount:

#     def __init__(self,account_number,balance):
#         self.account_number=account_number
#         self._balance=balance
#     def deposit(self,amount):
#          self._balance+=amount
#          return self._balance
#     def withdraw(self,with_amount):
#         if self._balance>0:
#             if self._balance>=with_amount:
#                 self._balance-=with_amount
#                 return self._balance
#             else:
#                 print("Insufficient funds")
#         else:
#             print("your balance in negative")            
# A=Bankaccount(89346,5000)
# print(A.deposit(2500))
# print(A.withdraw(5000))
# B=Bankaccount(93456246,700)
# print(B.deposit(2500))
# print(A.withdraw(9500))

# 2. Design a Student class where marks:
#  • should always be between 0 and 100 •
#  should never be set directly Enable updating marks only through a controlled method that performs range checks.
#  Demonstrate: • trying to assign marks manually
#  • why encapsulation protects invalid states 
# class student:
#     def __init__(self,marks):
#         if 0<=marks<=100:
#             self._marks=marks
#         else:
#             print("Invalid Marks")
#     def update_marks(self,marks):
#         if 0<=marks<=100:
#             self._marks=marks
#         else:
#             print("Invalid marks") 
# 3. Create a SecureFile class that: 
#  • stores content privately • provides a method read(password)
#  • refuses access if the password is incorrect • logs an "Unauthorized attempt" internally (cannot be accessed from outside

# class secureFile:
#     def __init__(self,name):
#         self._name=name
#         self.log=0
#     def check(self,password):
#         if password=="1234":
#             print(self._name)
#         else:
#             self.log+=1
#             print("Unauthorized attempt")
# D=secureFile("SATWIK")
# D.check("123")

# 4.Design an Employee class where:
#  • salary is hidden • outsiders cannot read salary directly 
#  • use getter method that logs each access attempt
#  • provide a method to update salary but only if the new salary is higher (prevent accidental downgrade

# class Employee:
#     def __init__(self,salary):
#         self._salary=salary
#     def     

# 5. Create a Product class where:
#  • price cannot be negative • discount cannot exceed 70% • 
#  internal final price calculation should not be directly exposed Provide only one public method get_final_price    
# class product:
#     def __init__(self,price,discount):
#         if price>=0:
#             self._price=price
#             self._discount=discount
#         else:
#             print("Invalid price")
#         if discount>=70:
#             self.discount=discount
#         else:
#             print("discount cannot exceed 70%")    
#     def get_final_price(self):
#         print(self._price*self._discount/100)
# P=product(200,65)
# P.get_final_price()
# # 
# 6. Create a Character class with:
#  • private _health • methods to damage(points) and heal(points)
#  • health cannot drop below 0 or exceed max limit 
#  • expose only current health through a read-only getter     

# class Character:
#     def __init__(self,health):
#         if 0<=health<=100:
#             self._health=health
#         else:
#             print("Invalid health")    
#     def damage(self,points):
#         self._health-=points
#     def heal(self,points):
#         self._health+=points
#     def get_health(self):
#         return self._health
# K=Character(70)
# K.damage(20)
# K.heal(30)
# print(K.get_health())           

# 7. Create: • An Engine class with private state like temperature
# • A Car class that uses an Engine but should: 
# o Not allow users to manipulate engine temperature o Only expose methods like start_car() or cool_engine() 
# Demonstrate why giving direct engine access is dangerous
