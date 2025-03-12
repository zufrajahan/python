class Employee:
    language = "python"
    salary = 10

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    @staticmethod
    def greet():
        print("Good Morning")

zufra = Employee()
zufra.name = " princess zufra jahan" #This is an object attribute
zufra.language = "javascript"

zufra.getInfo()
zufra.greet()
# Employee.getInfo(zufra)

