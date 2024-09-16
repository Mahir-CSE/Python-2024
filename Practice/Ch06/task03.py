marks = float(input("Enter yours marks: "))

if (marks>= 97 and marks <= 100):
    grade = "A+"
    
elif(marks >= 90 and marks <97):
    grade = "A"
    
elif(marks >= 85 and marks <90):
    grade = "A-"
    
elif(marks >= 80 and marks <85):
    grade = "B"
    
elif(marks >= 75 and marks <80):
    grade = "B-"
    
elif(marks >= 70 and marks <75):
    grade = "C"
    
elif(marks >= 65 and marks <70):
    grade = "C-"
    
elif(marks >= 60 and marks <65):
    grade = "D"

elif(marks >= 55 and marks <60):
    grade = "D-"
    
elif(marks >= 50 and marks <55):
    grade = "E"
    
else:
    grade = "F"
    
print("Your grade is: ",grade)