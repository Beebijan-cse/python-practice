lis=list(map(int,input("enter the element:").split()))
print(lis)

first=lis[0]
for i in range(len(lis)-1):
    lis[i]=lis[i+1]
lis[-1]=first               
print("rotated list lis",lis)   
