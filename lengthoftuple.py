num=int(input("enter the number to create a Tuple"))
lis=[]
for i in range(num):
    inp=int(input())
    lis.append(inp)
t=tuple(lis)    
print("Tuple is ",t)
print("length of given tuple is",len(t))