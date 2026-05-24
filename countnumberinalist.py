num=int(input("enter the number:"))
lis=[]
for i in range(num):
    inp=int(input())
    lis.append(inp)
print(lis)
count=0
n=int(input("enter the number to count:"))

for i in lis:
    if i == n:
        count+=1
    
print(f" count of {n} is {count}")    
