# print the s((mallest number in a list
num=int(input("enter the num:"))
lis=[]
for i in range(num):
    inp=int(input())
    lis.append(inp)
print(i) 

smallest=lis[0]  
for i in lis:
    if i<smallest:
        smallest=i
print("smallest number in the list is",smallest)        
        
        
