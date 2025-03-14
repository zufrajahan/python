a = int(input("enter a number:"))
b = int(input("enter a second number:"))

if(b == 0):
    raise ZeroDivisionError("gadhe kya kar rahe ho")
else:
    print(f"The division is a/b is {a/b}")