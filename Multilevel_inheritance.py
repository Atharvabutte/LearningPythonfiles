class animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def show(self):
        print(f"Name :{self.name}")
        print(f"Species :{self.species}")

class Category(animal):
    def __init__(self,name,breed):
        animal.__init__(self,name,species="Dog")
        self.breed = breed
        
    def show(self):
        animal.show(self)
        print(f"Breed: {self.breed}")

class Which_animal(Category):
    def __init__(self,name,color):
        Category.__init__(self,name,breed="Husky")
        self.color = color
        
    def show(self):
        Category.show(self)
        print(f"Color: {self.color}")
        


A= Which_animal("Boxer","Brown")
A.show()