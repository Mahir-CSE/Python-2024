# find the greatest of three numbers by using function

def greatest():
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter a number: '))
    num3 = int(input('Enter a number: '))

    if(num1 > num2 and num1 > num3):
        return num1
    elif(num2 > num1 and num2 > num3):
        return num2
    elif(num3 > num1 and num3 > num2):
        return num3

great = greatest()
print("Output: ", great)