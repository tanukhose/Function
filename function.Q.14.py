# Define a function which takes one parameter(positive integer). This function returns the sum of
#  all multiples of 3 and 5 (not neccessary common multiples) in the range 1 to the integer passed
#  as the parameter.
# Input:-
# 10
# 3 aur 5 ke multiples => 3, 5, 6, 9, 10
# Output :-
# 33


# a=int(input("enter the num "))
# i=1
# while i<=a:
#     if a%i==0:
#         print(i)
#     i+=1


# def sum():
#     a=int(input("enter the num "))
#     i=1
#     sum=0
#     while i<=a:
#         if i%3==0:
#             sum+=i
#         i+=1
# sum()


# def sum(a):
#     i=0
#     sum=0
#     while i<=a:
#         s=0
#         s1=0
#         if i%3==0:
#             print(i)
#             s+=i
#         elif i%5==0:
#             print(i)
#             s1+=i
#         sum+=s+s1
#         i+=1
#     print(sum)
# a=int(input("enter the num "))
# sum(a)

def sum(a):
    i=0
    sum=0
    while i<=a:
        s=0
        s1=0
        if i%3==0:
            print(i)
            s=s+i
        elif i%5==0:
            print(i)
            s1=s1+i
        sum+=s+s1
        i=i+1
    print(sum)
a=int(input("enter number"))
sum(a)

