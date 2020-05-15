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
        for roomItem in self.room.items:
            if item == roomItem.name:
                self.items.append(roomItem)
                roomItem.onTake()
                self.room.removeItem(roomItem)
                exists = True
                break
        if not exists:
            print(f"{item} does not exist in the room.")

    def __str__(self):
        return f"Player Name: {self.name} \nPlayers {self.room}"
