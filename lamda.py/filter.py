# numbers=[1,2,3,4,5,6,7,8,9,10]

# evens=list(filter(lambda x:x%2==1,numbers))
# print(evens)

# words=['cat','elephant','dog','python','ant']
# long_words=list(filter(lambda w:len(w)>4,words))
# print(long_words)

a=25
for i in range(1,a):
    num=i*(i+1)
    if num<25:
        print(num,end=" ")