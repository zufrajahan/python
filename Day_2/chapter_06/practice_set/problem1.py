# print table of any number using for loop

n= int(input("Enter a number: "))

for i in range(1,11):
    print(f"{n} * {i} = {n*i}")


# table using while loop    
input_num = int(input("enter num"))
i=1
while(i<=10):
    print(f"{input_num} * {i} ={input_num*i}")
    i+=1