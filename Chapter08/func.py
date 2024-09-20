# function: group of statements performing a similar task
# two parts of function: 1. function definition and 2. function call

# functions without return type and argument
def avg(): #function definition
    a = int(input("Enter number: "))
    b = int(input("Enter number: "))
    c = int(input("Enter number: "))

    avg = (a + b + c) / 3
    print("The average is", avg)

avg()


# function with return type + arguments
def avg1(num1, num2, num3):
    avg = (num1 + num2 + num3) / 3
    return avg

result = avg1(5,10,15)
print("RESULT: ", result)

# function with default argument

def greet(name, ending = "Thank You"):
    print(f"Good Morning! {name}")
    print(ending)

greet("Fahim")   # Good Morning -> Thank You
greet("Rahim", "Thanks") # # Good Morning -> Thanks