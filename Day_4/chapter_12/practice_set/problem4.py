def divisible5(n):
    if(n%5 == 0):
        return True
    return False

a = [1,3,5,6789,534,67,89,90,59]

f = list(filter(divisible5,a))
print(f)