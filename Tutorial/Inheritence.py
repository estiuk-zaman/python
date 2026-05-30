class Mammal:
    def Walk(self):
        print("Walk")

class Dog(Mammal):
    def Bark(self):
        print("Bark")

class Cat(Mammal):
    def Meow(self):
        print("Meow")

dog1=Dog()
dog1.Walk()
dog1.Bark() 
cat1=Cat()
cat1.Walk()
cat1.Meow()