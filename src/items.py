class Item:
    def __init__(self, item_description, name):
        self.name = name
        self.item_description = item_description

    def take(self):
        print(f"You have picked up {self.name}.")

    def drop(self):
        print(f"You have dropped {self.name}.")

    def __str__(self):
        return f"{self.name}--{self.item_description}"


class Food(Item):
    def __init__(self, name, description, calorie):
        super().__init__(name, description)
        self.calorie = calorie


class Weapon(Item):
    def __init__(self, name, description, damage):
        super().__init__(name, description)
        self.damage = damage
