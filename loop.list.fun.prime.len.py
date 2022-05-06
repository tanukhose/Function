
i=1
while i<=100:
    j=1
    count=0
    while j<=i:
        if i%j==0:
            count+=1
        j+=1
    if count==2:
        print(i,"prime")
    i+=1

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
  

# a=int(input("enter the number "))
# i=1
# count=0
# while i<=a:
#     if a%i==0:
#         count+=1
#     i+=1
# if count==2:
#     print("prime number ")
# else:
#     print("not ")