# 3 Create a function which takes 3 arguments(all integers) and prints their sum and average as 
#  shown below.
# Input:-
# Enter first number :-3

# Enter second number :-4

# Enter third number:-5

# Output :-

# Sum of three numbers :-12
# Average of three numbers :-4


def ave():
    i=1
    sum=0
    while i<=3:
        a=int(input("enter the number"))
        sum+=a
        i+=1
    print(sum,i)
    print(sum/i)
ave()