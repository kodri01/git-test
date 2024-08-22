from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def feed(self):
        pass

    def display_info(self):
        print(f'Name : {self.name}')
        print(f'Species : {self.species}')

class Lion(Animal):
    def make_sound(self):
        print('Roar')
    
    def feed(self):
        print('The lion is fed with meat.')
    
    def display_info(self):
        return super().display_info()

class Elephant(Animal):
    def make_sound(self):
        print('Trumpett')
    
    def feed(self):
        print('The Elephant is fed with vegetables.')
    
    def display_info(self):
        return super().display_info()

def manage_animal(animal):
    animal.make_sound()
    animal.display_info()
    animal.feed()

lion = Lion('Simba', 'Lion')
elephant = Elephant('Dumbo','Elephant')

print('Lion :')
manage_animal(lion)
print('')

print('Elephant :')
manage_animal(elephant)