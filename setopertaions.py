s1={1,2,3,4}
s2={5,6,7,8,4}
s3=s1 |s2 # union
print("union : ",s3)
s4=s1 & s2
print(" intersection ",s4) #intersection
print("differnce of s1-s2",s1 - s2) # difference (print the all elements in s1 except comman elements)
print("differnce of s2 -s1 ",s2-s1)
print("symmetric differnce",s1^s2) #symmetric difference