'''
problem : we wannt to print the number of the itrms in the lidt that its lenght is equal or greater than 2, and
the first char in the item string equal to the last char in this item string
'''

list=['abc','aba','1221','xyz']

#method one
print(sum(1 for i in range(len(list)) if(len(list[i])>= 2 and list[i][0]==list[i][-1])))

#method two
print(sum(1 for i in list if(len(i)>= 2 and i[0]==i[-1])))

#method three
count=0
for i in range(len(list)):
    if len(list[i])>= 2 and list[i][0]==list[i][-1]:
        count+=1
print(count)