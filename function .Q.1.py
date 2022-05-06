# num=[3,5,7,34,28,89,2,5]
# o\p=89

def max():
    num=[3,5,7,34,28,89,2,5]
    i=0
    max=0
    while i<len(num):
        if num[i]>max:
            max=num[i]
        i+=1
    print(max)
max()