class Number:
    def __init__(self,n):
        self.n = n

    def __add__(self,num):
        return self.n + num.n
    

m = Number(1)
n = Number(4)

print(n+m)