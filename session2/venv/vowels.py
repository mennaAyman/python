#counting the vowels in a certain string
vowels=['a','e','i','o','u'] # it's better to make it tuple because i don't want to change it.
#method 1
v2=input()
print(sum(1 for chr in v2 if chr in vowels ))

#method 2
input_string='aceviwxxih'
counter = 0
for chr in input_string:
    if chr in vowels:
        counter+=1
print("{} vowels found".format(counter))
