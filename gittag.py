class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f'Hai, Nama saya {self.name}, saya berumur {self.age} tahun')
    
Person1 = Person("Kodri", 24)
Person1.introduce()