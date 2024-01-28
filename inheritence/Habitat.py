"""
create inheritance using animal Dog relation.
for example, 
    Animal and Dog both has same habitat so create a method for habitat 
"""

class Animal:
    def __init__(self, Habitat) -> None:
        self.habitat = Habitat
    def in_general(self):
        print(f"I am in general Habitat {self.habitat}")
    def sound(self, sound):
        print(f"some animal specific sound as {sound}")

class Dog(Animal):
    def __init__(self, Habitat) -> None:
        super().__init__(Habitat)
    def sound(self):
        return super().sound("Woff Woff")
    
dog = Dog("Domestic")
dog.in_general()
dog.sound()