list1=[10,20,30,40,50]
num=int(input("enter the number you want to find:"))
i=0
for i in range(len(list1)):
    if list1[i]==num:
        print("found",i)
        break
else:
    print("not found")

l=list1[::-1]
print(l)
