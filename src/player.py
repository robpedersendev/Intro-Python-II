# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, room, items=[]):
        self.name = name
        self.room = room
        self.items = items

    def printRoom(self):
        print("##################################################################")
        print(f"Current Room: {self.room.name}")
        print("##################################################################")
        print(f"{self.room.description}")
        print("##################################################################")
        print("Items in this room:")
        self.room.displayItems()
        print("##################################################################")

    def printInventory(self):
        print("##################################################################")
        print(f"{self.name}'s inventory:")
        for item in self.items:
            print(item)
        print("##################################################################")

    def add(self, item):
        exists = False
        for room in self.room.items:
            if item == room.name:
                self.items.append(room)
                room.onTake()
                self.room.removeItem(room)
                exists = True
                break
        if not exists:
            print(f"{item} does not exist in the room.")

    def drop(self, item):
        exists = False
        for inventory in self.items:
            if item == inventory.name:
                self.items.remove(inventory)
                inventory.onDrop()
                self.room.addItems(inventory)
                exists = True
                break
        if not exists:
            print(f"{self.name} does not hold {item}.")

    def __str__(self):
        return f"Player Name: {self.name} \nPlayers {self.room}"
