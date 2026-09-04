# Question 1: Bank Account Operations
# Create a class BankAccount with:
# •	attributes: account_holder, balance 
# •	instance method: deposit(amount) 
# •	instance method: withdraw(amount) 
# Implement these magic methods:
# •	__str__() → display account details 
# •	__add__() → add balances of two accounts 
# •	__sub__() → subtract balances 
# •	__eq__() → compare if two accounts have same balance 
# •	__lt__() → check which account has lower balance 
# •	__getattribute__() → print a message whenever an attribute is accessed 
# •	__setattr__() → prevent setting negative balance 
# Demonstrate creating two accounts and using all operations.

# class Bankacoount:
#     def __init__(self,account_holder,balance):
#         self.account_holder=account_holder
#         self.balance=balance
#     def deposit(self,amount):
#         print("AMOUNT DEPOSITED")
#         self.balance=self.balance+amount
#         return self.balance
#     def withdraw(self,amount):
#         print("---after withdraw---")
#         if self.balance<=amount:
#             return self.balance-amount
#         else:
#             return f"INSUFFICIENT FUNDS"
#     def __str__(self):
#         print("str used here")
#         return f"NAME:{self.account_holder}\n BALANCE={self.balance}"
#     def __add__(self,other):
#         print("add called here")
#         return self.balance+other.balance
#     def __sub__(self,other):
#         print("sub called here")
#         return self.balance-other.balance
#     def __eq__(self,other):
#         print("eq is called here")
#         return self.balance==other.balance
#     def __lt__(self,other):
#         print("Lt is called here")
#         return self.balance<other.balance
# a=Bankacoount("SATWIK",9000)
# print(a.deposit(500))
# print(a.withdraw(22000))
# b=Bankacoount("ADI",8500)
# b.deposit(499)
# b.withdraw(2100)
# print(a)
# print(a+b)
# print(a-b)
# print(a==b)
# print(a<b)


# Question 2: Product Price Comparison
# Create a class Product with:
# •	attributes: name, price, quantity 
# •	method: total_price() 
# Implement:
# •	__str__() 
# •	__add__() → add total prices of two products 
# •	__mul__() → multiply product price by a number 
# •	__gt__() → compare which product has greater total value 
# •	__eq__() → compare prices 
# •	__getattr__() → return "Attribute not found" for missing attributes 
# •	__setattr__() → do not allow price less than 0 
# ________________________________________

# Question 3: Student Marks
# Create a class Student with:
# •	attributes: name, marks 
# •	method: grade() 
# Implement:
# •	__str__() 
# •	__add__() → add marks of two students 
# •	__truediv__() → divide marks by a number 
# •	__ge__() → check if one student scored greater than or equal to another 
# •	__lt__() → check if one student scored less 
# •	__getattribute__() → track attribute access 
# •	__setattr__() → marks must be between 0 and 100 

# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def grade(self):
#         if self.marks>90:
#             return "A"
#         elif self.marks>80:
#             return "B"
#         elif self.marks>70:
#             return "C"
#         else:
#             return "D"
#     def __str__(self):
#         return(f"name={self.name} scored {self.marks}")
#     def __add__(self,other):
#         return self.marks+other.marks
#     def __truediv__(self, other):
#         return self.marks/2
#     def __ge__(self,other):
#         return self.marks>other.marks
#     def __lt__(self,other):
#         return self.marks<other.marks
# g=student("pujara",90)
# m=student("vihari",20)
# print(g.grade())
# print(m.grade())
# print(g)
# print(m)
# print(g+m)
# print(g/m)
# print(g>m)
# print(g<m)

# Question 4: Rectangle Area Comparison
# Create a class Rectangle with:
# •	attributes: length, breadth 
# •	method: area() 
# Implement:
# •	__str__() 
# •	__add__() → add areas of two rectangles 
# •	__sub__() → subtract areas 
# •	__eq__() → compare areas 
# •	__gt__() → check which rectangle has larger area 
# •	__getattr__() → handle missing attributes 
# •	__setattr__() → length and breadth must be positive 

# class Rectangle:
#     def __init__(self,length,breadth):
#         self.length=length
#         self.breadth=breadth
#         # area=length*breadth
#     def rect_area(self):
#         return self.length*self.breadth
#         # self.area=self.length*self.breadth
#         # return self.area
#     def __str__(self):
#         print("--"*8)
#         return (f"length of rectangle={self.length}\nbreadth of rectangle={self.breadth}") 
#     def __add__(self,other):
#         print("--"*8)
#         return self.rect_area()+other.rect_area()
#     def __sub__(self,other):
#         print("--"*8)
#         return self.rect_area()-other.rect_area()
#     def __eq__(self,other):
#         print("--"*8)
#         return self.rect_area()==other.rect_area()
#     def __gt__(self,other):
#         return self.rect_area()>other.rect_area()
# s=Rectangle(10,20)
# print(s.rect_area())
# p=Rectangle(5,20)
# print(p.rect_area())
# print(p)
# print(s)
# print(s+p)
# print(s-p)
# print(s==p)
# print(s>p)


# Question 5: Employee Salary System
# Create a class Employee with:
# •	attributes: name, salary 
# •	method: annual_salary() 
# Implement:
# •	__str__() 
# •	__add__() → add salaries of two employees 
# •	__mul__() → calculate salary after multiplying by months 
# •	__ne__() → check if salaries are not equal 
# •	__le__() → check if one salary is less than or equal to another 
# •	__getattribute__() → log every attribute access 
# •	__setattr__() → salary cannot be below 10000 
# ________________________________________
# class Employee_sal:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def annual_salary(self):
#         return self.salary*12
#     def __str__(self):
#         print("--"*12)
#         return f"name of the Emp={self.name} and her annual salary={self.salary}"
#     def __add__(self,other):
#         print("--"*12)
#         return self.annual_salary()+other.annual_salary()
#     def __mul__(self,other):
#         print("--"*12)
#         return self.annual_salary()*other.annual_salary()
#     def __ne__(self,other):
#         print("--"*12)
#         return self.annual_salary()!=other.annual_salary()
#     def __le__(self,other):
#         print("--"*12)
#         return self.annual_salary()<=other.annual_salary()
# d=Employee_sal("smrithi",4500)
# r=Employee_sal("perry",3500)
# print(d)
# print(r)
# print(d+r)
# print(d*r)
# print(d!=r)
# print(d<=r)

# Question 6: Book Object Comparison
# Create a class Book with:
# •	attributes: title, author, pages 
# •	method: reading_time()
# Assume 1 page takes 2 minutes. 
# Implement:
# •	__str__() 
# •	__add__() → add pages of two books 
# •	__floordiv__() → divide pages by number of days 
# •	__gt__() → compare books based on pages 
# •	__eq__() → compare books based on title 
# •	__getattr__() → return custom message for missing attribute 
# •	__setattr__() → title cannot be empty and pages must be positive 
# ________________________________________

# class Book:
#     def __init__(self,title,author,pages):
#         self.title=title
#         self.author=author
#         self.pages=pages
#     def reading_time(self):
#         print("._"*12)
#         return self.pages*2
#     def __str__(self):
#         print("._"*12)
#         return f"title={self.title}\nauthor={self.author}\npages={self.pages}"
#     def __add__(self,other):
#         print("._"*12)
#         return self.pages+other.pages
#     def __floordiv__(self,other):
#         print("._"*12)
#         return  self.pages//other
#     def  __gt__(self,other):
#         print("._"*12)
#         return self.pages>other.pages
#     def __eq__(self,other):
#         print("._"*12)
#         return self.title==other.title
# x=Book("male_ego","virat",22)
# z=Book("master_mind","dhoni",33)
# print(x.reading_time())
# print(z.reading_time())
# print(x+z)
# print(x//10)
# print(x>z)
# print(x==z)

# Question 7: Shopping Cart
# Create a class CartItem with:
# •	attributes: item_name, price, quantity 
# •	method: final_amount() 
# Implement:
# •	__str__() 
# •	__add__() → add final amounts of two cart items 
# •	__mod__() → find remainder after applying a discount value 
# •	__lt__() → compare item total amount 
# •	__ge__() → compare quantity 
# •	__getattribute__() → display which attribute is being accessed 
# •	__setattr__() → quantity cannot be less than 1 
# ________________________________________



















# Question 8: Time Duration
# Create a class TimeDuration with:
# •	attributes: hours, minutes 
# •	method: total_minutes() 
# Implement:
# •	__str__() 
# •	__add__() → add two time durations 
# •	__sub__() → subtract two time durations 
# •	__eq__() → compare total minutes 
# •	__gt__() → check longer duration 
# •	__getattr__() → handle invalid attribute access 
# •	__setattr__() → minutes must be between 0 and 59 
# ________________________________________


# Question 9: Laptop Specification
# Create a class Laptop with:
# •	attributes: brand, ram, price 
# •	method: upgrade_ram(extra_ram) 
# Implement:
# •	__str__() 
# •	__add__() → add prices of two laptops 
# •	__mul__() → multiply price for bulk purchase 
# •	__lt__() → compare price 
# •	__eq__() → compare RAM 
# •	__getattribute__() → print access message 
# •	__setattr__() → RAM and price must be positive 
# ________________________________________


# Question 10: Game Player
# Create a class Player with:
# •	attributes: name, health, attack_power 
# •	method: attack(enemy) 
# Implement:
# •	__str__() 
# •	__add__() → combine attack powers 
# •	__sub__() → reduce health after attack 
# •	__gt__() → compare health 
# •	__eq__() → compare attack power 
# •	__getattr__() → return custom message for unavailable player stat 
# •	__setattr__() → health cannot go below 0 

# class player:
#     def __init__(self,name,health,attack_power):
#         self.name=name
#         self.health=health
#         self.attack_power=attack_power
#     def attack(self,enemy):
#         enemy.heath=enemy.health-self.attack_power
#         return enemy.health
#     def __str__(self):
#         print("-------BEFORE ATTACK---------")
#         return f"player_name={self.name} | player_health={self.health} | attack_power={self.attack_power}"
#     def __add__(self,other):
#         print("-----AFTER ADDING POWERS-------")
#         return self.attack_power+other.attack_power
#     def __sub__(self,other):
#         print(f"---AFTER ATTACK----")
#         return f"player_health={self.health-other.attack_power}"
# a=player("Satwik",100,80)
# b=player("Harsha",90,70)
# a.attack(b)
# print(a)
# print(a+b)
# print(a-b)
# print(a.attack(b))

# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def annual_salary(self):
#         return self.salary*12
#     def __str__(self):
#         return f'name:{self.name}\nsalary:{self.salary}\n'
#     def __add__(self, other):
#         return Employee("t",self.salary+other.salary)
#         # return f'addition of both salaries:{self.salary+other.salary}'
#     def __mul__(self, other):
#         return f'Multiplication of  both salary :{self.salary*other.salary}'
#     def __ne__(self, other):
#         if self.salary!=other.salary:
#             return f'{self.name} & {other.name} Salaries are not Equal'
#         else:
#             return f'{self.name} & {other.name} Salaries are Equal'

#     def __le__(self, other):
#         if self.salary<other.salary:
#             return f'{self.name} has Less salary than {other.name}'
#         elif self.salary==other.salary:
#             return f'{self.name} & {other.name} have equal salaries'
#         else:
#             return f'{self.name} & {other.name}  salaries are not <= to each other'

# # e1=Employee('Aadhya',5000)
# # e2=Employee('paaru',4000)
# # e3=Employee('shiva',5000)
# # e4=Employee('shiva',5000)
# # e5=Employee('shiva',5000)

# print(e1<=e2)
# print(e1!=e2)
# print(e1==e3)
# print(e1*e3)
# print(e1+e2+e3+e4+e5)

# class satwik:
#     def __init__(self,name,score,id):
#         self.name=name
#         self.score=score
#         self.id=id
#     def __str__(self):
#         return f"{self.name} {self.score}"
#     def __add__(self,other):
#         return satwik("suraj",self.score+other.score)
# d=satwik("sarath",99,9)
# f=satwik("sagar",88,8)
# k=satwik("kjadhf",99,99)
# print(d+f+k)   


