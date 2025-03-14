from functools import reduce
l= [1,3,5,6789,534,67,89,90,59]

def greater(a,b):
    if(a>b):
        return a
    return b

print(reduce(greater,l))
