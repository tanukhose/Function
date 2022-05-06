# def my(**kid):
#     print(kid["y"])
# my(f="t",z="a",y="n")


# def my(*kid):
#     print(kid[0])
# my("t","a","n")


# def add(a,b=3,d=1):
#     c=a+b+d
#     print(c)
# add(12,2,4)

# def add(a,d,s):
#     f=a+d+s
#     print(f)
# add(1,2,3)

# def add(a,c):
#     f=a+c
#     print(f)
# add(a=5,c=10)



# list = ["Z", "A", "A", "B", "E", "M", "A", "R", "D"]
# Output :-
# list = ["D", "R", "A", "M", "E", "B", "A", "A", "Z"]

def rev():
    list = ["Z", "A", "A", "B", "E", "M", "A", "R", "D"]
    i=1
    n=[]
    while i<=len(list):
        a=list[-i]
        n.append(a)
        i+=1
    print(n)
rev()
