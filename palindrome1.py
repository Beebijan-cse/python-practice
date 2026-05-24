# palindrome (means = 121=121
num=int(input("enter the number:-"))
rev=0
temp=num
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
if temp==rev:
    print(rev,"it is a palindrome number")
else:
    print(rev,"it is not  a palindrome number")
        