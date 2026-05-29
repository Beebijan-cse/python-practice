# sum of natural even number formuls is n(n+1)
# sum of n natural odd number is formula is n*n
num = int(input("enter the number:-"))
sum = num *num
print(f" The sum of n Natural number  is { sum},")
if num % 2==0:
    print("it is not a odd number  ")
else:
    print(" it is odd number ")    
