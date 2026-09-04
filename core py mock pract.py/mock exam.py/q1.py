# # students=[{"name":"Ravi","score":45},
# #          {"name": "sneha","score":78},
# #          {"name":"kiran","score":60},
# #          {"name":"Divya","score":92}]
#
# # a=list(filter(lambda x:,students))
# # b=list(map(lambda x:x.append("grade","Pass"),a))
# # c=sorted(b,key=lambda x:x<=92,reverse=True)
#
# students = [
#     {"name": "Ravi", "score": 45},
#     {"name": "sneha", "score": 78},
#     {"name": "kiran", "score": 60},
#     {"name": "Divya", "score": 92}
# ]
#
# passed_students = [
#     {**student, "grade": "pass"}
#     for student in students
#     if student["score"] >= 60
# ]
# final_result = sorted(passed_students, key=lambda x: x["score"], reverse=True)
#
#
# import pprint
# pprint.pprint(final_result)
#
#
# from functools import reduce
# l=list((input()))
# print(reduce(lambda x,y:x if x>y else y,l))
#
#
# def func():
#     x=300
#     def func2():
#         nonlocal x
#         def fun3():
#             nonlocal x
#             print(x)
#         fun3()
#     func2()
# func()
#
#
# n=int(input())
# for i in range(1,n+1):
#     c=0
#     for i in range(1,i+1):
#         if n%i==0:
#             c+=1
#         if c==2:
#             print(i)

# def dec(func):
#     def inner(n):
#         print("satarting this function")
#         print(func.__name__)
# #         func(n)
# #         print("ending this function")
# #     return inner
# @dec
# def greet(name):
#     print(f"Hello {name}")
#
# print(greet.__name__)
# greet("Nikhil")
#
#
# def m(a):
#     return a%2==0
# n=int(input("Enter a number:"))
# if m(n):
#     print("even")
# else:
#     print("odd")


# def Upper(x):
#     for i in x:
#         if i.isupper():
#             return True
# #     return False
#
# def vaild(func):
#     uns = []
#     special_char = ['@',"!","#","$","%","^","&","*"]
#     def inner(us:str,psd:str,age:int):
#         nonlocal uns
#         if us not in uns:
#             if 8 <= len(psd) <= 15:
#                 k = list(filter(lambda x: x in special_char, psd))
#                 n = list(filter(lambda x: x.isdigit(), psd))
#                 up = Upper(psd)
#                 # print(k)
#                 # print(n)
#                 # print(up)
#
#                 if up and n and k:
#                     if age >= 18:
#                         uns.append(us)
#                         return func(us,psd,age)
#                     else:
#                         return "Age must be greater than 17"
#                 else:
#                     return "Invalid Password"
#             else:
#                 return "Minimum length of the password is 8 characters"
#         else:
#             return "Username already exists"
#     return inner
#
#
# @vaild
# def register(username,password,age):
#     return f"{username}'s Register Successful"
#
# print(register("praveen","Dhaya143$$",19))
# print(register("praveen","Dhaya143$$",19))

# def valid(func):
#     special_char=['@','!','#','$']
#     def inner(us,pw:str):
#         if 8 <=len(pw) <=15:
#             k=list(lambda x:x in special_char,pw)
#             l=list(lambda x:x.isdigit(),pw)
#             s=list(lambda x:x.isupper(),pw)
#             if k and l and s:
#                 return func(us,pw)
#             else:
#                 return "Invalid password"
#         else:
#             return "minimum length of the password is 8 characters"
#     return inner
# @valid
# def register(username,password):
#     return (f"{username},s Register successfull")
# register("satwik","satwik@18")
#
def make_greeter():
    def say_hi():
        print("Hi there")
    return say_hi
my_func = make_greeter()
my_func()
