# unlike strings lists are mutable
friends = ["zufra", "lavaiza","sara","sana"]
print(friends[3])
friends[3]= "sumaya"
print(friends[3])


# ****************************************
# list methods
friends.append("aimen")
print(friends)


l1 = [1,34,78,45,6,75,6,7,5]
l1.sort()
print(l1)
l1.reverse()
print(l1)

l2=[1,3,4,5,6,7]
l2.insert(1,2) # insert 2 at index 1
l2.pop(3)
l2.remove(7)
print(l2)