class Employee:
    language = "python"
    salary = 10

    def __init__(self,name,salary,language): # dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    @staticmethod
    def greet():
        print("Good Morning")

zufra = Employee("zufra",5000,"pashto")

# zufra.name = "zufra jahan"
print(zufra.name,zufra.salary,zufra.language)

# init dunder method is called when an object is called


