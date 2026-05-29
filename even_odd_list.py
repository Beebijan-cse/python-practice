num=int(input("enter the numbers to create a list :"))
lis=[]
for i in range(num):
    inp=int(input())
    lis.append(inp)
print(" list is :", lis)

even=[]
odd=[]
for i in lis:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("even numbers in the list is",even)
    
print("odd numbers in the list is",odd)
        
            
        
