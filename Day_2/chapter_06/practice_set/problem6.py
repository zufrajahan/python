# star pattern

'''
  *
 ***
*****

'''
n= int(input("enter a number: "))
for i in range(1, n+1):
    print(""*(n-i) , end="")
    print("*"* (2*i-1 ), end="") #end is used to print in same line
    print("")