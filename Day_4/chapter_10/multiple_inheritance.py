class Employee:
    company = "ITC"
    name = "zufra"
    def show(self):
        print(f"The name is {self.name} and the company is {self.company}")


class Coder:
    language = "python"
    def printLanguage(self):
        print(f"your language is {self.language}")


class Programmer(Employee , Coder):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The company is {self.company} and he is good with {self.language} language")

a = Employee()
b = Programmer()
b.show()
b.printLanguage()
b.showLanguage()