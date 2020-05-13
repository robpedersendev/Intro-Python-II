from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons"),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

HEADINGS = {
    'n': 'n_to',
    's': 's_to',
    'e': 'e_to',
    'w': 'w_to'
}
# Functions for the loop

# userInput

def userInput():
    user_input = input("Where doest thou desirest to wander: ")
    return user_input.lower()


# Handle userInput

def handle_userInput(player, user_input):
    if user_input == 'q':
        return f"I wish you would continue playing", False
    elif user_input in ('n', 'e', 's', 'w'):
        heading = HEADINGS[user_input]
        room = getattr(player.room, heading)
        print(room, "Located in the handle_userInput function")
        if room is not None:
            player.room = room
        elif user_input == 'n':
            print('There is no room to the North, try again')
        elif user_input == 'e':
            print('There is no room to the East, try again')
        elif user_input == 's':
            print('There is no room to the South, try again')
        elif user_input == 'w':
            print('There is no room to the Waffles, try again')
        else:
            print("Try typing \"N\" \"S\" \"W\" or \"E\" instead")
    return True



# Make a new player object that is currently in the 'outside' room.
player1 = Player("Bob", room['outside'])  # Prints out Player Name: Bob -- Players Location: Outside Cave Entrance --
# Description: North of you, the cave mount beckons

print(player1)
movement = True
while movement:





# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
