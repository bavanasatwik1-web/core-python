# Q1. Create a class Student with instance attributes name and marks.
# Add an instance method is_passed() that returns True if marks > 40.
# Then create 2 student objects and print whether each has passed or failed.

class student:
    def __init__(self,name,marks):
        self.marks=marks
        self.name=name
    def is_passed(self):
        if self.marks>40:
            print(self.name,"is passed")
        else:
            print(self.name,"is failed")
s1=student("Satwik",98)            
s1.is_passed()
#  
# Q2. Create a class Employee with attributes name and company_name = "TechCorp".
# Add a class method change_company(cls, new_name) to update the company name for all employees.
# Demonstrate how this change affects all instances.

# class employee():
#     company_name="techcorp"
#     def __init__(self,name):
#         self.name=name
#     @classmethod
#     def new_company(cls,new_name):
#         cls.company_name=new_name

# e1=employee("surya")

# print(e1.name, "=" ,e1.company_name)


# employee.new_company("Infosys")
# print(e1.company_name, "=", e1.name)


# Q3. Create a class MathOps with a static method is_even(num) that returns True if the number is even.
# Then call it both from the class and an instance.

# class mathops():
#     def is_even(num):
#         return num %2==0
# object=mathops
# print(object.is_even(10))
# print(object.is_even(9))

# Q4. Create a class Car with:
# •	instance attribute mileage
# •	class attribute wheels = 4
# Add an instance method display_specs() that prints mileage and wheels.
# Then change wheels using a class method, and print again.

# class car():
#     wheels=4
#     def __init__(self,mileage):
#         self.mileage=mileage
#     def display_specs(self):
#          print(self.wheels)
#          print(self.mileage)
#     @classmethod
#     def change(cls,new):
#         cls.wheels=new
# s1=car(200)
# s1.display_specs()
# s1.change(6)
# s1.display_specs()       

# Q5. Create a class Temperature with:
# •	instance attribute celsius
# •	a static method to_fahrenheit(celsius)
# •	an instance method show_conversion() that uses the static method to print both values.

# class temperature():
#     def __init__(self,celsius):
#         self.celsius=celsius
#     def to_fahrenheit(celsius):
#         return (celsius*9/5)+32
#     def show_conversion(self):
#         print(temperature.to_fahrenheit(self.celsius))
# e1=temperature(25)
# # print(obj.to_fahrenheit())
# e1.show_conversion()
#       

# Q6. Create a class Book with:
# •	instance attributes title, author
# •	a class variable total_books
# •	a class method from_string(cls, book_str) that creates an object from "title-author" format
# •	a static method is_valid_title(title) that checks if title has at least 3 characters
# •	increment total_books for every book created
# Demonstrate:
# •	Creating books using both the constructor and the class method
# •	Validating titles before creation

# class Book():
#     total_books=0
#     def __init__(self,title,author):
#         self.title=title
#         self.author=author
#         Book.total_books+=1
#     @classmethod
#     def from_string(cls,book_str):
#         title,author=book_str.split("-")
#         return cls(title,author)
#     def is_valid_title(title):
#         return len(title)>3
# # a1=Book("satwik","ego")    
# if Book.is_valid_title("satwik"):
#     a=Book("satwik","ego")
# if Book.is_valid_title("python"):
#     b=Book.from_string("python-shiva")
# print(a.title,a.author)
# print(b.author,b.title)
# print(Book.total_books)


# Q7. Create a class Employee with:
# •	instance attributes: name, base_salary
# •	class variable: bonus_rate = 0.1
# •	instance method: final_salary() → base_salary + (base_salary × bonus_rate)
# •	class method: update_bonus(cls, new_rate) → updates bonus for all employees
# •	static method: is_valid_salary(sal) → checks if salary > 0
# Create two employees, show final salaries, update bonus rate, and show again.




        
# Q8. Create a class Course with:
# •	class variable total_students
# •	instance variable student_name
# •	instance method enroll() → increments total_students
# •	class method show_total(cls) → prints total students
# •	static method is_eligible(age) → returns True if age ≥ 18
# Demonstrate enrolling multiple students and show total count.

# class course():
#     total_students=0
#     def __init__(self,student_name):
#         self.student_name=student_name
#     def enroll(self):
#         course.total_students+=1
#     @classmethod
#     def show_total(cls):
#         print("total_students=",course.total_students)
#     @staticmethod
#     def is_eligible(age):
#         return age >=18
# c1=course("satwik")
# c1.enroll()
# c1.show_total()
# print(c1.is_eligible(77))

    
# Q9. Create a class BankAccount with:
# •	class variable bank_name
# •	instance variables holder and balance
# •	instance method deposit(amount)
# •	class method change_bank_name(cls, new_name)
# •	static method validate_amount(amount) → returns True if amount > 0
# Show transactions and how static + class methods work together.

# class bankAccount():
#     bank_name="sbi"
#     def __init__(self,holder,balance):
#         self.holder=holder
#         self.balance=balance
    
#     def deposit(self,amount):
#         if bankAccount.validate_amount(amount):
#             self.balance += amount
#             print("Balance:", self.balance)
#         else:
#             print("Invalid Amount")

#     @classmethod
#     def change_bank_name(cls,new_name):
#         cls.bank_name=new_name
#     @staticmethod
#     def validate_amount(amount):
#         return amount >0
# s=bankAccount("satwik",2000)
# s.deposit(90000)    
        

# Q10. Create a class Student with:
# •	class variable passing_marks = 40
# •	instance attributes name, marks
# •	instance method result() → prints pass/fail using class variable
# •	class method update_passing_marks(cls, new_marks)
# •	static method grade_category(marks) → returns "A", "B", "C" based on score ranges
# Use all three in a program that:
# 1.	Creates students
# 2.	Updates the passing criteria
# 3.	Displays grade category and result

# class student():
#     passing_marks=40
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def result(self):
#         if self.marks >= student.passing_marks:
#             print(self.name,"is passed")
#         else:
#             print(self.name," is passed")
#     @classmethod
#     def update_passing_marks(cls,new_marks):
#         cls.passing_marks=new_marks
#     def grade_category(marks):
#         if marks>=80:
#             return "A"
#         elif marks>=60:
#             return "B"
#         else:
#             return "C"
# s1=student("satwik",118)
# print(s1.name,"Grade=",student.grade_category(s1.marks))


# Q11. Create a class Student that:
# •	Keeps track of the total number of students created.
# •	Determines whether a student passed or failed based on a shared passing mark.
# •	Provides a method to curve marks by increasing everyone’s marks by a percentage.
# •	Has a utility to convert marks (0–100) into letter grades (A, B, C, etc.).

# class studentt:
#     pass_mark=35
#     total_students=0
#     def __init__(self,student,marks):
#         self.student=student 
#         self.marks=marks
#         studentt.total_students+=1
#     def result(self):
#         if self.marks>=studentt.pass_mark:
#             print(self.student,"is passed")
#         else:
#             print(self.student,"is failed")
#     @classmethod
#     def increase_marks(cls,marks,percentage):
#         return marks+(marks*percentage/100)
#     @staticmethod
#     def utility(marks):
#         if marks >=90:
#             return "A"
#         elif marks >=80:
#             return "B"
#         else:
#             return "c"
# s1=studentt("Satwik",92)
# s1.result()
# print(s1.increase_marks(80,9))

# Q12. Design a class Product that:
# •	Maintains a base tax rate applicable to all products.
# •	Each product has a name and base price.
# •	Has a method to compute final price including tax.
# •	Can change tax rate for all products using one method.
# •	Includes a function to check whether a given price is valid or not (non-negative and realistic).
# Demonstrate:
# 1.	Creating multiple products.
# 2.	Changing the tax rate.
# 3.	Showing updated prices and validity checks.

# class product:
#     base_tax=500
#     def __init__(self,name,base_price):
#         self.name=name
#         self.base_price=base_price
#     def final_price(self):
#         return self.base_tax+self.base_price    
#     @classmethod    
#     def change_base_tax(cls,new_tax_rate):
#         cls.base_tax=new_tax_rate
#     def realistic(base_price):
#         if base_price>=100:
#             return "Valid product"
#         else:
#             return "Not a Valid Product"
# s1=product("satwik",20)
# print(s1.final_price())
# print(product.realistic(191))

# Q13. Create an Employee class that:
# •	Keeps a minimum experience required for promotion (shared across all employees).
# •	Stores employee name, experience, and department.
# •	Has a method to check eligibility for promotion.
# •	Provides a function to update promotion criteria globally.
# •	Offers a general tool that checks if a given department is valid (like “HR”, “Tech”, “Admin”).
# Demonstrate:
# 1.	Creating employees from different departments.
# 2.	Changing promotion criteria.
# 3.	Displaying eligibility results and department validation.

# class Employee:
#     min_exp=5
#     def __init__(self,name,experience,department):
#         self.name=name
#         self.experiance=experience
#         self.department=department
#     def check(self):
#         if self.experiance>=self.min_exp:
#             return "eligible"
#         else:
#             return "Not eligible"
#     @classmethod
#     def update_promotion(cls,update_promotion):
#         min_exp=update_promotion
#     def valid(department):
#         s=["HR","TECH","ADMIN"]
#         if department in s:
#             return "valid"
#         else:
#             return "Invalid"
# s1=Employee("Satwik",9,"HR")
# print(s1.check())
# Employee.update_promotion(7)
# print(Employee.update_promotion(7))



# Q14. Build a Loan class that:
# •	Has a common interest rate for all loans.
# •	Each object stores borrower name and principal.
# •	Calculates total payable amount.
# •	Provides a function to update the interest rate.
# •	Provides a static function to check loan eligibility (e.g., salary > certain threshold).
# Demonstrate:
# 1.	Creating multiple loan accounts.
# 2.	Updating interest rates.
# Checking eligibility and total repayment for borrowers

# class Loan:
#     intrest=20
#     def __init__(self,name,principal):
#         self.name=name
#         self.principal=principal    
#     def Total(self):
#         return self.principal+self.intrest
#     @classmethod
#     def update_intrest(cls,new_intrest):
#         cls.intrest=new_intrest
#     def eligibility(salary,threshold):
#         threshold>salary
# s1=Loan("SATWIK",2000)
# print(s1.Total())
# Loan.update_intrest(30)
# print(s1.Total())


# Q15. Create a class Course that:
# •	Tracks total courses created.
# •	Each course has a title, duration, and enrolled_students.
# •	Provides a method to enroll a new student.
# •	Allows updating the minimum duration for a valid course across all instances.
# •	Has a static function to check if a given duration is realistic (not negative, not too large).
# Demonstrate:
# 1.	Creating multiple courses.
# 2.	Enrolling students.
# 3.	Updating minimum duration and checking durations.

# class course:
#     total_courses=0
#     minimum_duration = 30
#     def __init__(self,title,duration,enrolled_students):
#         self.title=title
#         self.duration=duration
#         self.enrolled_students=0
#         self.total_courses+=1
#     def student(self):
#         self.enrolled_students+=1
#         print("Student enrolled succesfully")
#     @classmethod
#     def update_min_duration(cls,new_min_duration):
#         new_min_duration=new_min_duration
#     def releastic(duration):
#         if duration>45:
#             return "valid"
#         else:
#             return"not valid"
# s1=course("satwik",29,5)
# s1.student()
# print(s1.releastic())          
                
# Q16. Design a class Vehicle that:
# •	Keeps a record of service charge rate common to all vehicles.
# •	Each vehicle has a model, kilometers_run, and service history.
# •	Has a function to calculate service charge based on km and rate.
# •	Provides a method to update the service rate for all vehicles.
# •	Provides a static tool to check if a vehicle model is eligible for service (not older than 15 years).
# Demonstrate:
# 1.	Creating vehicles with different km and models.
# 2.	Updating the service rate.
# 3.	Showing charges and eligibility checks.

# class vehicle:
#     service_charge=500
#     def __init__(self,model,kilometers_run,service_history):
#         self.model=model
#         self.kilometers_run=kilometers_run
#         self.service_history=service_history
#     def calculate(self):
#         return self.kilometers_run+self*vehicle.service_history
#     @classmethod
#     def update_ser_charge(cls,new_charge):
#         cls.service_charge=new_charge
#     def eligibility(model):
#         if model>15:
#             print("vechicle is eligible for service")
#         else:
#             print("Not eligible")
# v1 = vehicle(2018, 200, 3)
# print(v1.calculate())


# Q17. Build an Inventory class that:
# •	Tracks the total number of items across all inventories.
# •	Each instance maintains its own stock dictionary ({"item": quantity}).
# •	Provides a method to add or remove stock.
# •	Allows updating a minimum stock threshold globally.
# •	Offers a static checker to verify if a stock level is below threshold.
# Demonstrate:
# 1.	Managing multiple inventories.
# 2.	Adjusting stock threshold.
# 3.	Using static validation inside the instance logic.

# Q8. Create a HotelRoom class that:
# •	Keeps a base price per night (shared).
# •	Each room has room_number, nights_booked, and guest_name.
# •	Has a method to calculate total bill.
# •	Allows updating the base price across all rooms.
# •	Provides a static utility to check if a number of nights is valid (e.g., positive integer only).
# Demonstrate:
# 1.	Creating rooms and bookings.
# 2.	Changing base price.
# 3.	Checking bill updates and validation.

# class Hotelroom:
#     base_price=100
#     def __init__ (self,room_number,nights_booked,guest_name):
#         self.room_number=room_number
#         self.nights_booked=nights_booked
#         self.guest_name=guest_name
#     def calculate(self):
#         return self.base_price+self.nights_booked
#     @classmethod
#     def update_base_price(cls,new_base):
#         cls.base_price=new_base
#     def calculate_valid(nights_booked):
#         if nights_booked>0:
#             return "valid"
#         else:
#             return "Invalid"
# s1=Hotelroom(49,2,"satwik")
# print(s1.calculate())
# print(s1.calculate_valid())




