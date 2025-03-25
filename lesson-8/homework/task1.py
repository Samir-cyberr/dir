class Animal:
    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound
        self.energy = 100
    
    def make_sound(self):
        print(f"{self.name} the {self.species} says {self.sound}!")
        self.energy -= 5
    
    def eat(self, food):
        print(f"{self.name} is eating {food}.")
        self.energy += 20
        if self.energy > 100:
            self.energy = 100
    
    def sleep(self):
        print(f"{self.name} is sleeping.")
        self.energy = 100
    
    def __str__(self):
        return f"{self.name} the {self.species} (Energy: {self.energy})"


class Cow(Animal):
    def __init__(self, name):
        super().__init__(name, "Cow", "Moo")
        self.milk_production = 0
    
    def produce_milk(self):
        if self.energy >= 30:
            self.milk_production += 1
            self.energy -= 30
            print(f"{self.name} produced milk! Total milk: {self.milk_production} liters")
        else:
            print(f"{self.name} is too tired to produce milk.")


class Chicken(Animal):
    def __init__(self, name):
        super().__init__(name, "Chicken", "Cluck")
        self.eggs_laid = 0
    
    def lay_egg(self):
        if self.energy >= 20:
            self.eggs_laid += 1
            self.energy -= 20
            print(f"{self.name} laid an egg! Total eggs: {self.eggs_laid}")
        else:
            print(f"{self.name} is too tired to lay eggs.")


class Pig(Animal):
    def __init__(self, name):
        super().__init__(name, "Pig", "Oink")
        self.mud_level = 0
    
    def roll_in_mud(self):
        print(f"{self.name} is rolling in the mud!")
        self.mud_level += 10
        self.energy -= 15
        if self.mud_level > 100:
            self.mud_level = 100


# Example usage
def run_farm_example():
    print("Welcome to the farm!")
    
    cow = Cow("Bessie")
    chicken = Chicken("Henrietta")
    pig = Pig("Porky")
    
    animals = [cow, chicken, pig]
    
    for animal in animals:
        print(animal)
        animal.make_sound()
        animal.eat("some food")
    
    cow.produce_milk()
    chicken.lay_egg()
    pig.roll_in_mud()
    
    print("\nFarm status:")
    for animal in animals:
        print(animal)


if __name__ == "__main__":
    run_farm_example()