class Item:
    def __init__(self, item_description, name):
        self.name = name
        self.item_description = item_description

    def take(self):
        print(f"You have picked up {self.name}.")

    def __str__(self):
        return f"{self.name}--{self.item_description}"
