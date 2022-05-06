# If user's age is less than 18 , print “not eligible “,else if user's age is greater than 
# or equal to 18, print “you are eligible”
# Input:-
# 18
# 16
# Output :-

# “you are eligible”
# “not eligible”

def age (a):
    if a>=18:
        print("you are eligible")
    else:
        print("not eligible")
a=int(input("enter the number"))
age(a)