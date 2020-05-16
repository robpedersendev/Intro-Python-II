class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def take(self):
        print(f"You have picked up {self.name}.")

    def drop(self):
        print(f"You have dropped {self.name}.")

    def __str__(self):
        return f"{self.name}--{self.description}"


class Food(Item):
    def __init__(self, name, description, calorie):
        super().__init__(name, description)
        self.calorie = calorie


class Weapon(Item):
    def __init__(self, name, description, damage):
        super().__init__(name, description)
        self.damage = damage
