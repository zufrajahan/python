marks = {
    "zufra":100,
    "khalil":20,
    "ihtesham":50,
    0:"mashu"
}
# print(marks,type(marks))
# print(marks["zufra"])


# +++++++++++++++++++++++++++++++++++
# Dictionary Methods
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"khalil":50,"hasna":80})
print(marks)


# get method
# print(marks.get("ihtesham2")) # prints none
# print(marks["ihtesham2"]) # returns an error

p = marks.pop(0)
print(p)
print(marks)
#popitem will return and remove the last item
print(marks.popitem())

print("elements in marks2 will be")
marks2 = marks.copy()
print(marks2)
marks2.setdefault("princess",True)
print(marks2)

print(marks.clear())