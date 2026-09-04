           

# 1) Create a base class Animal with a method sound(). Create a derived class Dog that overrides the sound() method.
#  Demonstrate method overriding
# class Animal:
#     def sound(self):
#         print("animal is dog")
# class dog(Animal):
#     def sound(self):
#         print("Dog is Barking")
#         super().sound()
# obj=dog()
# obj.sound()
        

# 2) Create class A with method show(). Create class B(A) that overrides show() and also calls the parent method using super()
# class A:
#     def show(self):
#         print("A is big")
# class B(A):
#     def show(self):
#         super().show()
#         print("B is Big")
# s=B()
# s.show()


# Create multi-level inheritance with classes A → B → C, each having a method display() printing the class name. 
# Create object of C and call display(), showing method resolution.

# class A:
#     def display(self):
#         print("A is first")
        
# class B(A):
#     def display(self):
#         print("B is second")
#         super().display()
# class C(B):
#     def display(self):
#         print("C is third")
#         super().display() 
# t=C()
# print(C.mro())

         
# • Implement hierarchical inheritance using a base class Vehicle and two child classes Car and Bike, each defining a method wheels().

# class Vechicle():
#     def wheels_info(self):
#         print("a has 3wheels")
# class car(Vechicle):
#     def wheels_information(self):
#         print("B has 4wheels")
# class Bike(Vechicle):
#     def wheels(self):
#         print("c has 5wheels")

# class vechicle():
#     def __init__(self,wheels=0):
#         self.wheels=wheels
# class car(vechicle):
#     def display(self):
#         super().__init__(self.wheels+4)
#         print("car has=",self.wheels,"wheels")
# class bike(vechicle):
#     def display(self):
#         super().__init__(self.wheels+2)
#         print("bike has=",self.wheels,"wheels")
# k=bike()
# k.display()
# l=car()
# l.display()

      

# c1=Bike()
# c1.wheels()            
# c1.wheels_info()    
# c1.wheels_information()

# • Create class Employee with an instance method salary().
# Create class Manager(Employee) that overrides salary() and adds an incentive. Demonstrate both outputs.
# class Employee:
#     def salary(self):
#         return 500
# class manager(Employee):
#     def salary(self):
#         print("total salary")
#         return super().salary()+500 
# B1=manager()
# print(B1.salary())      

# class Employee:
#     def salary(self):
#         print("Employee salary=30,000")
# class manager(Employee):
#     def salary(self):
#         super().salary()
#         print("incentive added=5,000")
#         print("Total=35,000")
        
# B1=manager()
# B1.salary()   

# • Create class University with a class variable and a class method. 
# Inherit it into class College and access the parent’s class variable from the child class.

# class university():
#     name="Anits"
#     @classmethod
#     def study(cls):
#         print("a is first")
# class collage(university):
#     def show(cls):
#         print('cls',cls.name)
#     def show1(self):
#         print('self',self.name)
#         print('university',university.name)
# c1=collage()
# c1.show()
# c1.show1()
#     # print("collage name="{cls.name})
# # print(collage.name)
# # print(university.name)
    
# Create class MathOps with a static method add(a, b).
#  Create class AdvancedOps(MathOps) and use the static method without overriding it

# class mathops:
#     def add(a,b):
#         return a+b
# class advanceMathops(mathops):
#     pass

# b1=advanceMathops
# print(b1.add(5,10))

# • Create two classes Father and Mother, both defining a method skills().
# Create class Child(Father, Mother) and check which skills() runs using MRO.

# class Father:
#     def skills(self):
#         print("nanna")
#         super().skills()
# class Mother:
#     def skills(self):
#         print("amma")
# class son(Father,Mother):
#     def skills_s(self):
#         print("satwik")
#         super().skills        
# print(son.mro())
# n=son()
# n.skills()
# • Create an abstract class Shape with an abstract method area(). 
# Create class Rectangle(Shape) that implements the area() method.

#  Create class Person with a constructor __init__(name).
#   Create class Student(Person) with constructor __init__(name, roll). Use super() to call the parent constructor.

# class person:
#     def __init__(self,name):
#         self.name=name
# class student(person):
#     def __init__(self,name,roll):
#         super().__init__(name)
#         self.roll=roll
# mm=student("satwik",101)
# print(mm.name)
# print(mm.roll)

# 1. Bank Management System Create a Bank class with:
#  • balance variable • deposit() • withdraw() • check_balance() Create a User class that inherits Bank and displays the user's name.
#  Perform deposit, withdrawal, and balance check.

# 2. Employee Salary System 
# Create an Employee class with:
#  • emp_name  • salary • display_details()
#  Create a Manager class that inherits Employee and adds a bonus(). Display the total salary

# class Employee:
#     def __init__(self,emp_name,salary):
#         self.emp_name=emp_name
#         self.salary=salary
#     def display_details(self):
#         print("emp_name=", self.emp_name)
#         print("salary=",self.salary)
# class manager(Employee):
#     def __init__(self,emp_name,salary,bonus):
#         super().__init__(emp_name,salary)
#         self.bonus=bonus
#     def final_salary(self):
#         total_salary=self.salary+self.bonus
#         return "after_bonus",total_salary
# k=manager("satwik",2000,1000)
# k.display_details()
# print(k.final_salary())

# 1. Student Result System 
# Create a Student class with: • Name  • marks • display_marks() 
# Create a Result class that inherits Student and calculates whether the student has passed or failed.

# class students:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def display(self):
#         print("name=",self.name)
#         print("marks=",self.marks)
    
# class Result(students):
#     def check(self):
#         if self.marks>34:
#             print(self.name,"is passed")
#         else:
#             print(self.name,"is failed")
# s=Result("satwik",65)
# s.display()            
# s.check()

# 4. Food Ordering System Using Multilevel Inheritance 
# Class 1: Restaurant 
# Create a method menu(item) that returns the price of the selected food item.  
# Class 2: FoodCourt (inherits Restaurant)
# Create the following methods: 
# • display_menu() – Display the available food items. 
# • order() – Accept the food item from the user and allow multiple orders.
# • billing() – Display the total bill and add a packing charge of ₹20.
# Class 3: Customer (inherits FoodCourt)
# • Create an object of the Customer class. 
# • Call the order() method.  


# class a:
#     def venkey(self):
#         print("hii")
#         super().venkey()
# class b:
#     def venkey(self):
#         print("hello")
# class c(a,b):
#     def venkey(self):
#         print("venkey")
#         super().venkey()
# s1=c()
# s1.venkey()



class A:
    def __init__(self,ph):
        self.ph=ph
class B(A):
    def __init__(self,roll,gender,ph):
        self.roll=roll
        super().__init__(gender,ph)
class C(A):
    def __init__(self,gender,ph):
        self.gender=gender
        super().__init__(ph)

class D(B,C):
    def __init__(self,name,roll,gender,ph):
        self.name=name
        super().__init__(roll,gender,ph)
    def display(self):
        print(f"{self.name}\n{self.roll}\n{self.gender}\n{self.ph}")


g1=D("Satwik",21,"Male",346465287456)
print(g1.display())
