num=int(input("enter the number to create a list:"))
lis=[]
for i in range(num):
    inp=int(input())
    lis.append(inp)
print("original list is ",lis)    

rev=[]

for i in lis: # i=1
    
    rev=[i]+rev # rev[1]+rev[0],rev[2]+rev[1]
print("reversed list is",rev)       