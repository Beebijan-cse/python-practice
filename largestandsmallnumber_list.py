num=int(input("enter the num:"))
lis=[]
for i in range(num):
    inp=int(input())
    lis.append(inp)
print("list is",lis) 
max_val=lis[0]
min_val=lis[0]
for i in lis:
    if i>max_val:
        max_val=i
    if i<min_val:
        min_val=i
print("maximum value is",max_val)
print("minimum value is",min_val)

s