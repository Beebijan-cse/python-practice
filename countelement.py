t=(1,2,3,2,4,2)
count=0

num=int(input("enter the number to count"))
for i in t:
    if i==num:
        count+=1
print(f" {num} is repeated {count} times")        
