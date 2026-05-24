# su m of all items in the list
num=int(input("enter the num:"))
lis=[]
for i in range(num):
    inp=int(input())
    lis.append(inp)
print(lis) 

sum=0
for i in lis:
    sum+=i    
print("sum of all elements in the list is ",sum)    