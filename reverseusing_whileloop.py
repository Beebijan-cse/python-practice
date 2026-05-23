num = int(input("enter the number:-"))
rev =0
while num>0: # 2>0
    val=num%10 #2%10
    rev=(rev*10)+val 
    num=num//10
    print(rev)
