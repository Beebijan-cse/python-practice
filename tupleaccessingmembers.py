num=int(input("enter the number to create a tuple"))
lis=[]
for i in range(num):
    inp=int(input())
    lis.append(inp)
t=tuple(lis)  
print("tuple is",t)
print(t[0])
print(t[1])
print(t[2])
print(t[3])
print(t[4])
print(t[::-1])  # reverse of a tuple

