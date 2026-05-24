num = int(input("enter the number:-"))
a = num%10
num=num //10
b=num%10
num=num//10
c=num%10
num=num//10
reverse=a,b,c
print(reverse)