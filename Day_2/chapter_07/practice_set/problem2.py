def f_to_c(f):
    return 5*(f-32)/9

f = int(input("Enter the temperature in Fahrenheit: "))
c =f_to_c(f)
print(round(c,3))