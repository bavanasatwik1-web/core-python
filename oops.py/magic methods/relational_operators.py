# class Student:
#     def __init__(self,marks):
#         self.marks=marks
#     def __ge__(self,o2):
#         return self.marks>=o2.marks
#     def __lt__(self,o2):
#         return self.marks<o2.marks
#     def __le__(self,o2):
#         return self.marks<=o2.marks
#     def __gt__(self,o2):
#         return self.marks>o2.marks
# s1=Student(99)
# s2=Student(79)
# print(s1>=s2)
# print(s1<s2)
# print(s1<=s2)
# print(s1>s2)

 

class Emp:
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def __eq__(self,o2):
        return self.id==o2.id and self.name==o2.name
c1=Emp(188,"sai")
c2=Emp(188,"sai")
