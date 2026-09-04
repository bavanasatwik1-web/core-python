# Create an iterator for the list [10, 20, 30, 40, 50] and print each element using next().
# n=[10,20,30,40,50]
# # it=iter(n)
# for i in n:
#     print(i)
# # print(next(it))
# # print(next(it))
# print(next(it))

# Create an iterator for the string "PYTHON" and print each character using next(

# k="PYTHON"
# k=iter(k)
# print(next(k))
# print(next(k))
# print(next(k))
# print(next(k))
# print(next(k))
# print(next(k))

# Create a custom iterator that prints numbers from 1 to N, where N is given by the user.

# class Numbers:
#     def __init__(self,num):
#         self.num=num
#         self.n=1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.n<=self.num:
#             k=self.n
#             self.n+=1
#             return k
#         else:
#             raise StopIteration 
# sat=Numbers(5)
# for i in sat:
#     print(i)

# Create a custom iterator that prints odd numbers from 1 to N.

# class B:
#     def __init__(self,num):
#         self.num=num
#         self.n=1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.n<=self.num:
#             if self.n%2==0:
#                 s= self.n
#                 self.n+=1
#                 return s
#         else:
#             raise StopIteration
# k=B(10)
# for i in k:
#     print(i)        

# create a custom iterator that prints numers from N to 1.

# class A:
#     def __init__(self,n):
#         self.n=n
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.n>=1:
#             k=self.n
#             self.n-=1
#             return k
#         else:
#             raise StopIteration
# j=A(9)
# for i in j:
#     print(i)            

# create a custom iterator that prints even numbers 

# class A:
#     def __init__(self,n):
#         self.n=n
#         self.num=1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.num<=self.n:
#             if self.num%2==0:
#                 k=self.num
#                 self.num+=1
#                 return k
#             else:
#                 self.num+=1
#                 return self.__next__()
#         else:
#             raise StopIteration
# j=A(9)
# for i in j:
#     print(i)            



class A:
    def __init__(self,n):
        self.n=n
        self.i=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.i<=len(self.n):
            if self.n[self.i-1]%2==0:
                k=self.n[self.i-1]
                self.i+=1
                return k
            else:
                self.i+=1
                return self.__next__()
        else:
            raise StopIteration
j=A([2,4,6,7,8])
for i in j :
    print(i)            
