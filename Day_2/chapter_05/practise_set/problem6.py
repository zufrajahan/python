marks = int(input("ENter your marks :"))

if(marks <=100 and marks>=90):
    grade =  "Ex"
elif(marks <90 and marks>=80):
    grade = "A"
elif(marks <= 80 and marks >= 70):
    grade = "B"    
else:
    grade = "c"

print("Your grade is :",grade)
