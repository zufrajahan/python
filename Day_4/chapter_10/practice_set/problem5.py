class Vector:
    def __init__(self, x, y ,z):
        self.x = x
        self.y = y
        self.z = z


    def __add__(self,other):
        result = Vector(self.x + other.x , self.y + other.y, self.z + other.z)
        return result
    
    def __mul__(self,other):
        result = self.x * other.x + self.y * other.y + self.z * other.z
        return result
    
    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"
    
# Test the implementations
v1 = Vector(1,2,3)
v2 = Vector(5,5,3)
v3 = Vector(1,5,9) #same dimension vector


print(v1 + v2)
print(v1 * v2)

print(v1 + v3)
print(v1 * v3)