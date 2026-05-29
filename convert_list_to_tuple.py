num=int(input("enter the number to create a list:"))
lis=[]
for i in range(num):
    inp=int(input())
    lis.append(inp)
print("list is ",lis)    
t=tuple(lis)
print("tuple is ",t)
