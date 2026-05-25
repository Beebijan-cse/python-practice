num=int(input("enter the num:"))
lis=[]
for i in range(num):
    inp=int(input())
    lis.append(inp)
print("list is",lis) 
updated_list=[]
for i in lis:
    if i not in updated_list:
        updated_list.append(i)
print(updated_list)