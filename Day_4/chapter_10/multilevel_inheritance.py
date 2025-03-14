class Employee:
    a = 1

class Programmer(Employee):
    b = 2 

class Manager(Programmer):
    c = 3

o =  Employee()
print(o.a)

z= Programmer()
print(z.a,z.b)

f = Manager()
print(f.a,f.b,f.c)