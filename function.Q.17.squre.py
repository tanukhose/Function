# Create a function which takes one argument (a positive integer) and returns a dictionary which has 
# numbers from 1 to the integer (passed as parameter) as the keys and their respective squares as the 
# values as shown in the examble below.

# Input :-
# 20

# Output :-

# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25,
#  6: 36, 7: 49, 8: 64, 9: 81, 10: 100,
#   11: 121, 12: 144, 13:169, 14: 196, 15: 225,
#    16: 256, 17: 289, 18: 324, 19: 361, 20: 400}

def sq(a):
    i=1
    l=[]
    while i<=a:
        b=i,i**2
        i+=1
        l.append(b)
    print(l)
a=int(input("enter the num "))
sq(a)


# def sq(**a):
#     i=1
#     while i<=a:
#         print(i,i*2)
#         i+=1
# a=int(input("enter the num "))
# sq(a)


