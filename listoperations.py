lis=["Beebijan","Jaan","19","kishkinda university","weight= 59.67",]
print(lis)
print(type(lis))
lis.append("Python practice") # adding new item to the list
print("Updated list is",lis)
lis.pop(0)# pop is used for removing the item from the list
print("after removing the item from the list",lis)
lis.insert(3,"beautifull") # inserting the item at a specific position
print(lis)
lis.extend(["ndsmhgg",90])# used for adding multiple items to the list
print("after adding the multiple items into the list",lis)
lis.remove("19") # removing  items from the list
print("after removing ",lis)
del lis[0] # deleting item from the lis through index
print(lis)
