a= (1,45,67,"zufra","zufra") # tuple cannot be changed they are immutable
# t=type(a)
# print(t)
num = a.count("zufra")
print(num)

i = a.index("zufra") # it only gives the index of first occurance
print(i)
print(45 in a)
print(456 in a)

b,c,d,e,f = a
print(b,c,d,e,f)
print(b)