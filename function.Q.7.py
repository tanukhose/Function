# Write add_numbers function here
# num1 = 56
# num2 = 12
# add_numbers(num1,num2)

# Output :-
# 68

def add(num1,num2):
    c=num1+num2
    print(c)
add(56,12)




# Write a function named add_numbers_list which takes 2 lists of two integers and then prints the
#  sum of the integers with the same position.
# Use the add_numbers function given in Part 1 to count 2 integers that have the same position.

# If we give [50, 60, 10] and [10, 20, 13] to this function it will print this
# 60
# 80
# 23


def sum():
    a=[50,60,10]
    a1=[10,20,13]
    sum=0
    i=0
    while i<len(a):
        sum=a[i]+a1[i]
        print(sum)
        i+=1
sum()