#varoiable Length Parameters
'''because there's an astric(*) then the sent variable is cosidered as a list'''
def fun(*X):
    for X in X:
        print(X)
fun(1,"menna",2,"id")
'''output:
1
menna
2
id
'''

'''because there are two stars (**) then the sent paranmeters is considered a dictionary :(Key & Value)'''
def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))

myFun(first='Geeks', mid='for', last='Geeks')
''' output:
first == Geeks
mid == for
last == Geeks
'''