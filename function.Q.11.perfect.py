# Perfect Number?
# A perfect number is the one which is equal to the sum of all it's factors(including 1 and 
# excluding itself).

# Define a function named perfect() which takes one argument(integer) and checks if it is 
# a perfect number or not. Now use this code to write a program that prints all the perfect
#  numbers between 1-1000. 

def per():
    a=int(input("enter the number = "))
    i=1
    sum=0
    n=a 
    while i<a:
        if a%i==0:
            sum=sum+i
        i=i+1
    if n==sum:
        print("prefect")
    else:
        print("not perfect number")
per()