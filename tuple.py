num=int(input("enter the number to create a tuple"))
lis=[]
for i in range(num):
    inp=int(input())
    lis.append(inp)
t=tuple(lis)  
print("tuple is",t)