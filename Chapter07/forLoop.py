for i in range(0,51, 5):
    print(i)
    
print("Concept of 'Break': ")
for i in range(10):
    if(i == 7):
        break
    print(i, end="")
    
print()    
print("Concept of 'Continue': ")
for i in range(10):
    if(i == 7):
        continue
    print(i, end="")

print()
for i in range(1, 6):
    for j in range(1 , i+1):
        print(j, end=" ")
        
    print()
        
    