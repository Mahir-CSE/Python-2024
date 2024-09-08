#Check the type of variable assigned using input () function.

n = input("Enter something: ")
print(type(n))

# Use comparison operator to find out whether ‘a’ given variable a is greater than 
# ‘b’ or not. Take a = 34 and b = 80

a = 34
b = 80

print("Result: ", a>b)

# Write a python program to find an average of two numbers entered by the user.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

avg = (num1 + num2)/2
print("The avg: ",avg)

# Write a python program to calculate the square of a number entered by the user
num3 = int(input("Enter a number: "))
print( num3 ** 2)