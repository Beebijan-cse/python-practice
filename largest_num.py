num=int(input("enter the number:- "))
lis=[]
for i in range(num):
    inp=int(input())
    lis.append(inp)
print("list is :",lis)    
largest=list[0] # l=0

for i in lis:
    if i>largest: 
        largest=i
print("largest number in a list",largest)        
