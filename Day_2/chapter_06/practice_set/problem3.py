# prime number or not

n=int(input("enter a number: "))
for i in range(2,n):
    if(n%i) == 0:
        print("number is not prime")
        break
else:
    print("number is prime")