
# # 3)question
# def fun(original_password):
#     def inner(another_password):
#         if original_password==another_password:
#             return "ACCESS GRANTED"
#         else:
#             return "ACCESS DENIED"
#     return inner
# s=fun("SATWIK123")
# print(s("SATWIK124"))



# class Book:
#     total_books = 0
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         Book.total_books += 1
#     @classmethod
#     def from_string(cls, book_str):
#         title, author = book_str.split("-")   # Split the string
#         if cls.is_valid_title(title):
#             return cls(title, author)
#         else:
#             print("Invalid Title")
#     @staticmethod
#     def is_valid_title(title):
#         return len(title) >= 3
#     def display(self):
#         print("Title :", self.title)
#         print("Author:", self.author)
# book1 = Book("centuries", "virat")
# book2 = Book.from_string("ego-satwik")
# book1.display()
# print()
# if book2:
#     book2.display()
# print("\nTotal Books:", Book.total_books)



# question 3

class Watertank:
    def __init__(self,tank_name,water_level=0):
        self.tank_name=tank_name
        self.water_level=water_level
    def __add__(self,other):
        return self.water_level+other.water_level
    def __sub__(self,other):
        return self.water_level-other.water_level
    def __truediv__(self, other):
        return self.water_level/other.water
    def __str__(self):
        return f"tank-name:{self.tank_name} water_level:{self.water_level}"
    def __repr__(self,other):
        return self.water_level-other.water_level
s=Watertank("TANK1",50)
b=Watertank("TANK2",20)
print(s+b)
print(s-b)
print(s)
print(b)

    

