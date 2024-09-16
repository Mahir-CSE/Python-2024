sub1 = int(input("Enter marks for sub1: "))
sub2 = int(input("Enter marks for sub2: "))
sub3 = int(input("Enter marks for sub3: "))

totalMarks = 300

result = 100 * (sub1 + sub2 + sub3) / totalMarks

if(result >= 40 and sub1 >=33 and sub2 >= 33 and sub3 >= 33):
    print("PASSED")
else:
    print("FAILED")
    