numbers=[1,2,3,4,5]
from functools import reduce
total= reduce(lambda a,b:a+b,numbers)
print(total)