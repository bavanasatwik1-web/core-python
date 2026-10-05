'''• Create a class Person whose constructor takes age as an argument. Raise a ValueError if the age is less than 0'''
# class person:
#     def __init__(self,age):
#         self.age=age
#         if age<0:
#             raise ValueError("Age cannot be negative")
# c=person(-2)
# print(c.age)

'''Create a class Student with an attribute marks. 
Implement a method set_marks(marks) that raises a ValueError if marks are not in the range 0 to 100.'''

# class Student:
#     def __init__(self):
#         self.marks=0
#     def set_marks(self,marks):
#         if marks<0 or marks>100:
#             raise ValueError("marks must be in range of 0 and 100")
# L=Student()
# L.set_marks(101)

''' • Create a custom exception named InvalidAgeError. 
# Create a class Voter with a method check_eligibility(age) that raises this exception if age is less than 18.'''
# class InvalidAgeError(Exception):
#     pass
# class Voter:
#     def check_eleigibility(self,age):
#         if age<0:
#             raise InvalidAgeError("Age cannot be less than zero")
#         print(age)
# L=Voter()
# L.check_eleigibility(20)
# L.check_eleigibility(-2)
# L.check_eleigibility(2)

'''• Create a class BankAccount with an attribute balance.
Implement a method withdraw(amount) that raises an exception if the withdrawal amount is greater than the available balance.'''

# class BankAccount:
#     def __init__(self):
#         self.balance=100
#     def withdraw(self,amount):
#         if amount>self.balance:
#             raise ValueError("withdrawal amount is greater than the available balance.")
#         self.balance-=amount
#         print("withdraw Succesfull"
#               "and remaining balance=",self.balance)
# L=BankAccount()
# L.withdraw(50)        
        
'''• Create a class PasswordValidator with a method validate(password). Raise an exception if the password length is less than 8 characters.'''  
# class Passwordvalidator:
#     def validate(self,password):
#         if len(password)<8:
#             raise ValueError("password lengtgh must be 8 characters")
#         print("password is validated")
# A=Passwordvalidator()
# A.validate("SATWI")        

''' • Create a class UserInput with a method get_integer(value). Handle ValueError and TypeError using separate except blocks.'''

# class UserInput:
#     def get_integer(self,value):
#         try:
#             integer=int(value)
#             print("Number",integer)
#         except ValueError:
#             print("Cannot convert given value into integer")
#         except TypeError:
#             print("Cannot convert given value into integer") 
# L=UserInput()
# L.get_integer("20")   
# L.get_integer("Satwik")                

'''Create a class Transaction with a method process() that uses try, except, and finally blocks to ensure a cleanup message is always printed'''
# class Transaction:
#     def process(self,amout):
#         try:
#             trans_amount=int(amout)
#             print(amout)
#         except ValueError:
#             print("Amount must be in integer")
#         finally:
#             print("Transcation intiated")    
# K=Transaction()
# K.process("222")
# K.process("SATW")

'''• Write a function named find_length(obj) that uses a loop to calculate the length of the given object without using the built-in len() function.
The function should return the calculated length if the object is iterable. 
If a non-iterable object such as an integer is passed, the function should raise and handle a TypeError,
and print an appropriate error message explaining what happens when an integer is sent as input.'''

# def find_length(obj):
#     c=0
#     try:
#         for i in obj:
#             c+=1
#         if c>0:
#             print(c)
#     except TypeError:
#         print ("TypeErroe;This obj cannot be iterate")
# find_length("njfwnjwv")
# find_length([1,2,3])
# find_length(3)

'''• Create a class LoginSystem with a method login(password) that raises an exception for an incorrect password and handles the exception outside the class.'''
# class IncorrectPassword(Exception):
#     pass
# class LoginSystem:
#     def __init__(self):
#         self.password="SATWI18"
#     def login(self,password):
#         if password==self.password:
#             print(password,"is coreect")
#         else:
#             raise IncorrectPassword("IncorrectPassword entered")
# L=LoginSystem()        
# try:
#     L.login("ADI2")
# except IncorrectPassword as e:
#     print(e)         
            
'''• Create a class Service with a method that calls another method which raises an exception. Catch and handle the exception in the Service class.'''
# class Service:
#     try:
#         def method(self):
#             self.method2()
#         def method2(self):
#             raise ValueError("bfvwnjo")
#     except ValueError as s:
#         print(s)
# l=Service()
# l.method()

# class A:
#     def sound(self):
#         print("A class called")
# class B:
#     def sound(self):
#         print("B class Called")
# classes=[A(),B()]
# for i in classes:
#     i.sound()              
