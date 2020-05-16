# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, room, items=[]):
        self.name = name
        self.room = room
        self.items = items

    def printRoom(self):
        print("\n\n\n\t\t\t\t")
        print(f"Current Room: {self.room.name}")
        print("\n\n\n\t\t\t\t")
        print(f"{self.room.description}")
        print("\n\n\n\t\t\t\t")
        print("Items in this room:")
        self.room.displayItems()
        print("\n\n\n")

    def printInventory(self):
        print("\n\n\n\t\t\t\t")
        print(f"{self.name}'s inventory:")
        for item in self.items:
            print(item)
        print("\n\n\n")

    def add(self, item):
        exists = False
        for room in self.room.items:
            if item == room.name:
                self.items.append(room)
                room.take()
                self.room.remove(room)
                exists = True
                break
        if not exists:
            print(f"{item} does not exist in the room.")

    def drop(self, item):
        exists = False
        for inventory in self.items:
            if item == inventory.name:
                self.items.remove(inventory)
                inventory.drop()
                self.room.add(inventory)
                exists = True
                break
        if not exists:
            print(f"{self.name} does not hold {item}.")

    def __str__(self):
        return f"Player Name: {self.name} \nPlayers {self.room}"
