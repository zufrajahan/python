a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))    
c = int(input("Enter the third number : "))
d = int(input("Enter the fourth number : "))

if(a>b and a>c and a>d):
    print(f"{a} is greater")
elif(b>a and b>c and b>d):
    print(f"{b} is greater")    
if(c>b and c>a and c>d):
    print(f"{c} is greater")
elif(d>a and d>c and d>b):
    print(f"{d} is greater")    