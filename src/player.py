# Write a class to hold player information, e.g. what room they are in
# currently.
from items import Item


class Player(Item):
    def __init__(self, name, room, items=[]):
        self.name = name
        self.room = room
        self.items = items

    def lose_item:

    def add_item:

    def __str__(self):
        return f"Player Name: {self.name} \nPlayers {self.room}"
