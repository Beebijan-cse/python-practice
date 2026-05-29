lis=list(map(int,input("enter the element:").split()))
print(lis)
# using slicing
result=lis[-1:]+lis[0:]
print("rotated lis is",result)
