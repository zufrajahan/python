from functools import reduce
l = [1,3,4,5,6]
# map example
square = lambda x: x*x
sqlist=map(square,l)
print(list(sqlist))

# filter example
def even(n):
    if (n%2 == 0):
        return True
    return False

onlyEven = filter(even,l) #function, list
print(list(onlyEven))

# reduce example
def sum(a,b):
    return a+b
print(reduce(sum,l))