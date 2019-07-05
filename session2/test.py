''''#sum and multiply of numbers
num1 = int(input())
num2 = int(input())
num3 = int(input())

print(num1 + num2 + num3)
print(num1 * num2 * num3)
print((num1 - num2)*num3)
print(num1 - num2 * num3)
print("the sum of the three numbers is " + str(num1 + num2 + num3) + ", the multiplication result of the three numbers is " + str(num1 * num2 * num3))

#Apple Sharing
students_num = int(input())
apples_num = int(input())
print("the number of distributed apples equals " + str(students_num//apples_num))
print("the remaining apples in the basket equals to " + str(students_num % apples_num)

#area of right angled triangle
base_lenght = float(input())
height_lenght = float(input())

print("area of triangle is " + str(round(0.5*base_lenght*height_lenght, 2)))'''

'''[a,b,c] = [int(i) for i in input().split(',')]
print("sum : {} \nmultiply : {}" .format(a+b+c , a*b*c))'''

x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]
# Output: False
print(x1 is not y1)
# Output: True
print(x2 is y2)
# Output: False
print(x3 is y3)
