from room import Room
from player import Player
from items import Item, Food, Weapon

# Declare all the rooms

# Initialize items

# Generic items
stick = Item("Stick",
             "An old, reliable piece of a tree                                                                      ")

# Food
rice = Food("Rice", "Grain that you can eat", 310)
bagel = Food("Bagel", "This turns into carbohydrates", 700)

# Weapon
knife = Weapon("Knife", "Close to a shank, but not a shank", 35)
prison_shank = Item("Shank", "A sharp knife used in ye olde prisons")

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

# Add room items
room['outside'].addItems(stick, stick, bagel)
room['foyer'].addItems(knife, bagel)
room['overlook'].addItems(rice, prison_shank)
room['narrow'].addItems(knife, bagel, knife, rice, rice, stick)
room['treasure'].addItems(knife, knife, knife, bagel, bagel, bagel, bagel, bagel, bagel, bagel)

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
    user_input = input(f"What would you like to do? Move :[n] "
                       f"North\t[s] South\t[e] East\t[w] West\n[i] Access Inventory\
                        n[take <item_name>]\t[drop <item_name>]\n[q] Quit: ")
    return user_input.lower()


# Handle userInput

def handle_userInput(player, user_input):
    cli_input = user_input.split()
    if len(cli_input) == 1:
        if user_input == 'q':
            print(f"\n\n\n\t\t\t\tI wish you would not say such things!\n\n\n")
            return False
        elif user_input in ('n', 'e', 's', 'w'):
            heading = HEADINGS[user_input]
            room = getattr(player.room, heading)
            # print(room, "Located in the handle_userInput function")
            if room is not None:
                player.room = room
            else:
                print("There is no rooms to the %s, you dope." % user_input)
        elif user_input == 'i':
            player.printInventory()
        else:
            print("\n\n\n\t\t\t\tTry typing \"N\" \"S\" \"W\" \"E\" \"I\" \"Get/Take\" \"Drop\" instead\n\n\n")
        return True
    elif len(cli_input) == 2:
        if cli_input[0] == "get" or cli_input[0] == "take":
            player.add(cli_input[1])
        elif user_input[0] == "drop":
            player.drop(cli_input[1])
        return True
    else:
        print("\n\n\n\t\t\t\tTry typing \"N\" \"S\" \"W\" \"E\" \"I\" \"Get/Take\" \"Drop\" instead\n\n\n")
    return True


# Main function that is ran and called

def main():
    # Have user provide a username
    username = input("What is your name? ")
    # Make a new player object that is currently in the 'outside' room.
    player = Player(username,
                    room['outside'])  # Prints out Player Name: Bob -- Players Location: Outside Cave Entrance --
    # Description: North of you, the cave mount beckons

    movement = True

    while movement:
        player.printRoom()

        user_input = userInput()
        movement = handle_userInput(player, user_input)

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


if __name__ == "__main__":
    main()
