# print the armstrong number ex = 153=1**=1
# 5**=125, 3**=27  1+125+27=153 this a armsstrong number

num =int(input("enter the number:-"))
sum=0
temp=num
while num>0:
    digit=num%10
    sum=sum + digit**3
    num=num//10
if sum==temp:
    print("it is a armsstrong number")  
else:
    print("it is not a armsstrong number")    
    


