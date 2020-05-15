# Implement a class to hold room information. This should have name and
# description attributes.
from items import Item


class Room(Item):
    def __init__(self, name, description, item, item_description):
        self.name = name
        self.description = description
        super().__init__(item, item_description)

        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        return f"Location: {self.name} \nDescription: {self.description}"
