# Write a function named check_numbers which takes two numbers and then print "both are even" if
#  both numbers are even (divide by 2) otherwise print "both numbers are not even".

# def oddeve(a,b):
#     if a%2==0 and b%2==0:
#         print("both are even")
#     else:
#         print("both aer not even")
# a=int(input("enter the number"))
# b=int(input("enter the number"))
# oddeve(a,b)






# If you call your function [2, 6, 18, 10, 3, 75] and [6, 19, 24, 12, 3, 87] then it should
# give this output:

# both are even
# both are not even
# both are even
# both are even
# both are not even
# both are not even


def even():
    a=[2, 6, 18, 10, 3, 75] 
    b=[6, 19, 24, 12, 3, 87]
    i=0
    while i<len(a):
        if a[i]%2==0 and b[i]%2==0:
            print("both are even   ",a[i],",",b[i])
        else:
            print("both are not even   ",a[i],",",b[i])
        i+=1
even()











































# def add_numbers(number_x, number_y):
#     number_sum = number_x + number_y
#     return number_sum

# sum1 = add_numbers(20, 40)
# print(sum1)
# sum2 = add_numbers(560, 23)
# a = 1234
# b = 12
# sum3 = add_numbers(a, b)
# print(sum2)
# print(sum3)
# number_a = add_numbers(20, 40) / add_numbers(5, 1)
# print(number_a)