# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items

        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def add(self, *new):
        for item in new:
            self.items.append(item)

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print(f"{item} does not exist in this room.")

    def __str__(self):
        return f"Location: {self.name} \nDescription: {self.description}"
