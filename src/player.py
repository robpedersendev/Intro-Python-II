# Write a class to hold player information, e.g. what room they are in
# currently.
from items import Items


class Player(Items):
    def __init__(self, name, room, items, item_description):
        self.name = name
        self.room = room
        super().__init__(items, item_description)

    def __str__(self):
        return f"Player Name: {self.name} \nPlayers {self.room}"
