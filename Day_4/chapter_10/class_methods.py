class Employee:
    a = 1
    # to show class attribute we @classmethod and instead of self we use cls
    @classmethod
    def show(cls):
        print(f"The class attribute is {cls.a}")

e = Employee()
e.a = 45
e.show()