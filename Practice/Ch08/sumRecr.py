l = int(input("Enter a number: "))

def sum(num):
    if num == 1:
        return 1
    result = num + sum(num - 1)

    return result

result = sum(l)
print("Summation: ", result)

