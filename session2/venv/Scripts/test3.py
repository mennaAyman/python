'''
problem : we want to count the number of zeros and ones in a list
'''
array=[0,1,1,1,0,0,1,0,1,7,11]
count_1 = 0
count_0 = 0
for i in range(len(array)):
    if array[i]==1:
        count_1+=1
    elif array[i]==0:
        count_0+=1
print("the number of zeros is: " ,count_0)
print("the number of ones is: " ,count_1)

print("the number of ones is: " ,array.count(1) , "the number of zeros is: " ,array.count(0))

'''x="helllllo"
print(x[0:2])'''
