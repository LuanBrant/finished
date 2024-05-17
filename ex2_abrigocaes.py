import random

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclasses devem implementar este método")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return f"{self.name} diz: Woof!"

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def speak(self):
        return f"{self.name} diz: Meow!"

class Shelter:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def adopt_animal(self):
        if self.animals:
            animal = random.choice(self.animals)
            self.animals.remove(animal)
            return f"{animal.name} foi adotado!"
        else:
            return "Não há animais disponíveis para adoção."

# Criando alguns animais
dog1 = Dog("Rex", "Labrador")
cat1 = Cat("Whiskers", "Cinza")
dog2 = Dog("Buddy", "Golden Retriever")
cat2 = Cat("Mittens", "Branco")

# Criando um abrigo e adicionando animais
shelter = Shelter()
shelter.add_animal(dog1)
shelter.add_animal(cat1)
shelter.add_animal(dog2)
shelter.add_animal(cat2)

# Adotando um animal aleatório
print(shelter.adopt_animal())

# Verificando os animais restantes no abrigo
print("Animais no abrigo:")
for animal in shelter.animals:
    if isinstance(animal, Dog):
        print(f"{animal.name} - {animal.breed}")
    elif isinstance(animal, Cat):
        print(f"{animal.name} - {animal.color}")
