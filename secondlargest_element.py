num=int(input("enter the num:"))
lis=[]
for i in range(num):
    inp=int(input())
    lis.append(inp)
print("list is",lis) 
largest=lis[0]
second=lis[0]
for i in lis:
    if i>largest:
        second=largest
        largest=i
    elif  i>second and i!=largest: #is this number bigger than current second,not equal to largest
        second=i
        print("second largest is ",second)
    
        
        
        