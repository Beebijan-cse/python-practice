num=int(input("enter the number to create a  list"))
lis=[]
for i in range(num):
    inp=int(input())
    lis.append(inp)
print(i)    
second_largest=lis[0]
first_largest=lis[0]

for i in lis:
    if i >first_largest:
        second=first_largest

        
        