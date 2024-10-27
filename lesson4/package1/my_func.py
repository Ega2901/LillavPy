class MyClass():
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def summa(self):
        return self.a + self.b

    @classmethod
    def hello():
        return "Hello!"
    
    def __str__(self):
        return f"a = {self.a}, b = {self.b}"

    