# num=[1,2,3,4,5]
# o\p=15

def sum():
    num=[1,2,3,4,5]
    i=0
    sum=0
    while i<len(num):
        sum+=num[i]
        i+=1
    print(sum)
sum()