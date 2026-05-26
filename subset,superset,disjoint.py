A={1,2,3}
B={1,2,3,4,5,6}
#check subset 
print("A is subset of B",A.issubset(B))
# chec"k superset
print("B is ssuperset of  A",A.issuperset(A))
# check disjoint (no comman elements)
print("A and B are disjoint:",A.isdisjoint(B))