# lists
data1 = ["apple", 7, False, "Rahim"]

print(data1[0])
print(data1[1])
print(data1[2])
print(data1[3])

data1.append("Dhaka")
print(data1)

data1[2] = True
print(data1)

#list methods
data1.insert(2, "Mahir")
print(data1)

data1.pop(2)
print(data1)

data1.remove("Dhaka")
print(data1)