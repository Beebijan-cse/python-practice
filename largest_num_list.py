# print the largest  digit digit in a given number
num=int(input("enter the number:-"))
largest_num=0
while num>0:
    digit=num%10
    if digit > largest_num:
        largest_num=digit
    num=num%10
print("largest number is",largest_num)      
        
