class Employee:
    def __init__(self):
        print("constructor of employee")
    a = 1

class Programmer(Employee):
    def __init__(self):
        print("constructor of Programmer")
    b = 2 

class Manager(Programmer):
    
    def __init__(self):
        super().__init__()
        print("constructor of manager")
    c = 3

o =  Employee()
print(o.a)

z= Programmer()
print(z.a,z.b)

f = Manager()
print(f.a,f.b,f.c)