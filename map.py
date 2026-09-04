# l=[1,2],[3,4],[4,5]
# result=list(map(lambda x:x+[5],l))
# print(result)
# from functools import reduce
# l=[1,2,3,4,5]
# a=reduce(lambda x,y:x if x>y else y,l)
# print(a)

# a="satwik"
# result=list(map(lambda x:ord(x),a))
# print(result)

# s="satwikbavanaviratkohli"
# result=list(filter(lambda x:x not in "AEIOUaeiou",s))
# print(result)

# nums=[12,15,7,18,20,21,25]
# result=list(filter(lambda x:x if x%3==0 else x%5==0,nums))
# print(result)
# from functools import reduce
# nums=[1,2,3,4]
# a=reduce(lambda x,y:x+y,nums,10)
# print(a)

# n=6
# c=0
# for i in range(1,n+1):
#     if n%i==0:
#         c+=1
        
# if c<=2:
#     print("PRIME")
# else:
#     print('no prime')        

# Use map() to double every number in:
numbers = [1, 2, 3, 4, 5]

res=list(map(lambda x: x*x,numbers))
print(*res)