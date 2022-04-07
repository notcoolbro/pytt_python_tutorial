#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
rooms = {
    'Hall': {
        'south' : 'Kitchen'
        },
    'Kitchen' : {
        'north' : 'Hall'
        }
    }

#start the player in the Hall
currentRoom = 'Hall'

def showInstructions():
    '''print a main menu and the commands'''
    print('''
    Welcome to your own RPG Game
    ============================

    Get to the Garden with a key and a potion.
    Avoid the monsters!

    Commands:
    go [direction]
      get [item]
    ''')

def showStatus():
    '''print the player's current status'''
    #print the current room
    print('---------------------------')
    print('You are in the ' + currentRoom)
    #print the current inventory
    print('Inventory : ' + str(inventory))
    #print an item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")


#main program
showInstructions()
#main game loop
while True:
    showStatus()
    #wait for user input
    move = ''
    while move == '':
        move = input('>')
    move = move.lower().split()
    #end game
    if move[0] == "exit":
        break
    #navigation
    if move[0] == "go":
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
        else:
            print("You can't go that way!")
