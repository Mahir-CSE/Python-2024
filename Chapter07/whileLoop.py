print("Loop Start")

i = 1

while (i<5 + 1):
    print(i)
    i += 1

print("Loop End")

# print a list by while loop

l = ["A", "B", "C", "D", "E"]

i = 0
while(i<len(l)):
    print(l[i])
    i = i+1
    
# Nested While Loop

row = 1
while (row <= 5):
    col = 1
    while (col <= row):
        print(col , end="")
        col = col + 1 
    
    print()
    row = row + 1