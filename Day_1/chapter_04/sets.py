s = {1,5,32}
e = set() # this is how we make empty set 



# set methods
e.add(1)
e.add(50)
e.add(100)
print(e,type(e))
e.remove(50)
print(e)

# e.pop will remove random element from set


# union and intersection
s1= { 1,4,6,7,9}
s2= { 4 ,6 ,8 ,9}
print("union of s1 and s2 is :")
print(s1.union(s2))
print("intersection of s1 and s2 is :")
print(s1.intersection(s2))

print(s2.discard(10))
print("difference od s1 and s2 is")
print(s1.difference(s2))
print(s2.difference_update(s1))

print(s1.issubset(s2))
print(s1.issuperset(s2))