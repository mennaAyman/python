'''
problem: checking if the diagonal of the given matrix is equal to one
'''
room_stud={ 0:[1,2,3] ,1:['a',1,'c'] , 2:[2,1,1]}
flag = 1
for key in room_stud:
   if room_stud[key][key] == 1:
        flag = 1
   else:
        flag=0
        break
if flag:
    print("yes")
else:
    print("No")