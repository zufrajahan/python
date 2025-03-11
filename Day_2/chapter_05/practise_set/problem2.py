marks1 = int(input("Enter marsks 1 :"))
marks2 = int(input("Enter marsks 2 :"))
marks3 = int(input("Enter marsks 3 :"))

total_percentage = (marks1 + marks2 + marks3)/300 *100

if(total_percentage >= 40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33):
    print("You are passed")
    print(f"{total_percentage}% is your total percentage")
else:
    print("Yor are failded, try again next year")    