# celcius to farenhite

def converter(cels):
    # c/5 = (f-32)/9
    farenhite = ((cels / 5) * 9) + 32
    return farenhite

temp = float(input("Enter temperature: "))
farn = converter(temp)
print("Farenhite: ", farn)