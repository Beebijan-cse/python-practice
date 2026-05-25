num=int(input("enter the num:"))
lis=[]
for i in range(num):
    inp=int(input())
    lis.append(inp)
print("list is",lis) 
# another way to take input from the user
num=list(map(int, input("enter the values:").split()))
print(list)