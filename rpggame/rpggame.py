import random

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
rooms = {
    "Hall": {
        "south" : "Kitchen",
        "east" : "Dining Room",
        "west" : "Billard Room",
        "item" : "key"
        },
    "Kitchen" : {
        "north" : "Hall",
        },
    "Dining Room" : {
        "west" : "Hall",
        "south" : "Garden",
        "item" : "potion"
        },
    "Garden" : {
        "north" : "dining room"
        },
    "Billard Room" : {
        "east" : "Hall",
        "north": "Library",
        "item" : "almanach"
        },
    "Library": {
        "south" : "Billard Room",
        "east" : "Laboratory",
        "item" : "book-of-life"
        },
    "Laboratory": {
        "west" : "Library",
        "item": "beam-o-mat"
        }
    
    }


def showInstructions():
    #multiline string acts as a docstring
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
        #check if item starts with a vowel and adapt output
        if rooms[currentRoom]["item"].startswith(("a" or "e" or "i" or "o" or "u")):
            print('You see an ' + rooms[currentRoom]["item"])
        else:
            print('You see a ' + rooms[currentRoom]["item"])

    print("---------------------------")

def placeMonsterRandom():
    '''pick a random room and place the monster in it'''
    monsterRoom = ""
    #eliminate hall from rooms to place monster in, so our hero doesn't die rightaway
    while (monsterRoom == "") or (monsterRoom == "Hall"):
        monsterRoom = random.choice(list(rooms))
    rooms[monsterRoom]["item"] = "monster"

#main program


#start the player in the Hall
currentRoom = 'Hall'

placeMonsterRandom()
    
showInstructions()

#main game loop
while True: #creates an infinite loop
    showStatus()
    #wait for user input
    move = ''
    while move == '':
        move = input('>')
    move = move.lower().split() #lower converts string to lowercase, split creates list of words
    #end game
    if move[0] == "exit":
        break
    #navigation
    if move[0] == "go":
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
        else:
            print("You can't go that way!")
    #pick up an item
    if move[0] == "get":
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]["item"]:
            inventory += [move[1]]
            print ("picked up " + move[1] + "!")
            del rooms[currentRoom]["item"]
        else:
            print("Can't get " + move[1] + "!")

    #finish game            
    #a: die
    if "item" in rooms[currentRoom] and "monster" in rooms[currentRoom]['item']:
        print("Seems like you found a monster. YOU LOSE.")
        break
            
    #b: win
    if (currentRoom == "Garden" and "key" in inventory and "potion" in inventory)\
       or (currentRoom == "Laboratory" and ("book of life" and "beam-o-mat") in inventory):
        print("Looks like we found us a final girl. YOU WIN!")
        break
    
#end of main game loop
#end of main program
