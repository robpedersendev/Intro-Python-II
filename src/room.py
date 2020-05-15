# Implement a class to hold room information. This should have name and
# description attributes.
from items import Items


class Room(Items):
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        super().__init__(items)

        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        return f"Location: {self.name} \nDescription: {self.description}"
