#Prime or not: devided by 1 or the number itself to get in value

l = int(input("Enter the range: "))

#finding prime numbers within range

for num in range(2, l):
    for i in range(2, num):
        if num%i == 0:
            break
        else:
            print(num)
  