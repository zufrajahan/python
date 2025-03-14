try:
    a = int(input("enter a: "))
    b = int(input("enter a: "))
    print(a/b)
except ZeroDivisionError as v:
    print("infinite")