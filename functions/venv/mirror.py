# MIRROR CHECKING METHODS

# method 1
def checkMirroredArray(x):
    '''
    function Description:
    recieves a list and checks on the item of the list to see if it's a mirrored array or not
    :param x: it's a list
    :return:true if mirrored , false if not
    '''
    if len(x)%2 != 0:
        return False

    for item in range(int(len(x)/2)):
        if x[item]!=x[len(x)-1-item]:
            return False
    return True

my_list=[1,2,3,4,4,3,2,1]
print(checkMirroredArray(my_list))
print(checkMirroredArray(['a','b','c','d','b','a']))

# method 2
def sumMirror(x):
    '''
     function description:
     calculate the sum of the times the elements is found mirrored and checks if it's equal to the length/2 or not.
    :param x: is the list
    :return: true if mirrored , false otherwise
    '''
    value=sum(1 for item in range(int((len(x)/2))) if  x[item]==x[len(x)-1-item])
    if value == (len(x)/2):
        return True
    else:
        return False
print(sumMirror(['a','b','c','d','b','a']))

# method 3
def reverseMirror(x):
    '''
    function description:
    recieves the list and if elements (0;lenght/2 -1) equals the part(lenght/2 : lenght -1 ) reversed then it's mirrored.
    :param x: is the list
    :return: true if mirrored , false otherwise
    '''
    if x[:(len(x)//2)-1] == x[(len(x))-1:(len(x)//2):-1]:
        return True
    else:
        return False
print(reverseMirror([1,2,3,4,4,3,2,1]))

# optimization for method 3
def optimizedMirror(x):
    return x[:(len(x)//2)-1] == x[(len(x))-1:(len(x)//2):-1]
print(optimizedMirror([1,2,3,4,4,3,2,1]))