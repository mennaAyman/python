'''
problem : we want to remove the last element in the list corresponding to the first key and add an element in
the fisrt position in the list corresponding to the second element
'''
dictionary={'K1':[1,2,3],'K2':[4,5,6]}
del(dictionary['K1'][-1])
dictionary['K2'].insert(0,11)
print(dictionary)