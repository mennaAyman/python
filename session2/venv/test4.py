#this problem is to convert the string into a list
s1="Hello"
s2=[]
#method 1
for i in s1:
    s2.append(i)
print(s2)

#method 2
s2=list(s1)
print(s2)

#method 3
s4=[ch for ch in s1]
print("solution is {}".format(s4))