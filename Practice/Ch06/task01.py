n1 = int(input("Enter number:"))
n2 = int(input("Enter number:"))
n3 = int(input("Enter number:"))
n4 = int(input("Enter number:"))

if(n1>n2 and n1>n3 and n1>n4):
    print("Greatest number: ",n1)
    
if(n2>n1 and n2>n3 and n2>n4):
    print("Greatest Number: ",n2)
    
elif(n3>n1 and n3>n2 and n3>n4):
    print("Greatest Number: ",n3)
    
elif(n4>n1 and n4>n2 and n4>n3):
    print("Greatest Number: ",n4)