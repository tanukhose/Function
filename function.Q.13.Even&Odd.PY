# Define a function which takes one argument which is the limit upto which the function has
# to print the numbers and their label(even or odd) as shown below.
# For example :-
# Input:-
# 3
# Output :-
# 0 EVEN
# 1 ODD
# 2 EVEN
# 3 ODD

def evodd():
    a=int(input("enter the number "))
    i=0
    while i<=a:
        if i%2==0:
            print(i,"even")
        else:
            print(i,"odd")
        i=i+1
evodd()





# i=1
# while i<=100:
#     j=1
#     count=0
#     while j<=i:
#         if i%j==0:
#             count+=1
#         j+=1
#     if count==2:
#         print(i,"prime")
#     i+=1

# i=1
# l=[]
# while i<=100:
#     j=1
#     c=0
#     while j<=i:
#         if i%j==0:
#             c+=1
#         j+=1
#     if c==2:
#         l.append(i)
#     i+=1
# print(l)





# a=["tanu","vaishali","art","dhanashree"]
# i=0
# while i<len(a):
#     print(len(a[i]),a[i])
#     i+=1
  