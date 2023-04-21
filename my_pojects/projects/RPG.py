#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""

def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
    RPG Game
    ========
    Commands:
      go [direction]
      get [item]
      touch [object]
      use [item] with [structure]
    ''')

def showStatus():
    """determine the current status of the player"""
    # print the player's current location
    print('---------------------------')
    print('You are in the ' + currentRoom)
    print(rooms[currentRoom]['description'])
    # print what the player is carrying
    print('Inventory:', inventory)
    # check if there's an item in the room, if so print it
    if "item" in rooms[currentRoom]:
      print('You see a ' + rooms[currentRoom]['item'])
    if "object" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['object'])
    if "structure" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['structure'])
    print("---------------------------")


# an inventory, which is initially empty
inventory = []

# total user moves
total_moves = 0

# a dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'description' : 'An imposing chamber with vaulted ceilings, towering pillars, and a grand entrance.'
                                  ' The walls are adorned with macabre tapestries and flickering torches.'
                                  ' There are ominous doors leading to the north, south, and east.',
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room'
                },
            'Locked room' : {
                  'description' : 'A foreboding chamber with a heavy oak door, bolted shut with rusted chains.'
                                  ' The air is thick with the smell of incense and decay.'
                                  ' You can barely make out the shadowy figure of a dark altar in the center of the room.',
                  'south' : 'Hall',
                  'structure'  : 'dark alter'
                },
            'Kitchen' : {
                  'description' : 'A shadowy room with blackened walls and a rusty stove.'
                                  ' The cupboards are filled with twisted implements and jars of unspeakable things.'
                                  ' A grotesque monster with jagged teeth lurks in the shadows.',
                  'north' : 'Hall',
                  'npc'  : 'monster'
                },
            'Dining Room' : {
                  'description' : 'A grandiose chamber with a long, black table and a crystal chandelier dripping with cobwebs.'
                                  ' The walls are adorned with portraits of long-dead ancestors and flickering candelabras.'
                                  ' There are ominous doors leading to the west and south.',
                  'west' : 'Hall',
                  'south': 'Garden',
                  'item' : 'potion'
               },
            'Garden' : {
                  'description' : 'A haunting outdoor space with twisted trees, thorny vines, and twisted statues.'
                                  ' The air is thick with the scent of decay and the sound of wailing winds.'
                                  ' There is a door leading to the north and a gaping, dark tunnel leading down.',
                  'north' : 'Dining Room',
                  'down' : 'Tunnel'
               },
            'Tunnel' : {
                  'description' : 'A chilling and claustrophobic tunnel with low, arched ceilings and slimy walls.'
                                  ' The only light comes from flickering torches on the walls, casting eerie shadows on the ground.'
                                  ' There is a faint glimmer of an amulet and an odd stone on the ground, but you sense an ominous presence lurking in the darkness.',
                  'up' : 'Garden',
                  'item'  : 'amulet',
                  'object' : 'odd stone'
            }
         }




# start the player in the Hall
currentRoom = 'Hall'

showInstructions()

# breaking this while loop means the game is over
while True:
    showStatus()

    # the player MUST type something in
    # otherwise input will keep asking
    move = ''
    while move == '':
        move = input('>')

     # normalizing input:
     # .lower() makes it lower case, .split() turns it to a list
     # therefore, "get golden key" becomes ["get", "golden key"]
    move = move.lower().split(" ", 1)

    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
          if move[1] in rooms[currentRoom]:
             #set the current room to the new room
             currentRoom = rooms[currentRoom][move[1]]
             #adds to moves count
             total_moves += 1

            # if they aren't allowed to go that way:
          else:
            print('You can\'t go that way!')

    #if they type 'get' first
    if move[0] == 'get' :
        # make two checks:
        # 1. if the current room contains an item
         # 2. if the item in the room matches the item the player wishes to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory.append(move[1])
            #display a helpful message
            print(move[1] + ' got!')
            #delete the item key:value pair from the room's dictionary
            del rooms[currentRoom]['item']

    #if player picks up key
    if 'key' in inventory:
        rooms['Hall'].update({'north' :'Locked room'})

     #if they type 'touch'
    if move[0] == 'touch':
        if move[1] == 'odd stone' and rooms[currentRoom] == rooms['Tunnel'] :
            print('The odd stone sinks into the wall...')
            del rooms['Tunnel']['object']
            rooms['Hall'].update({'item': 'key'})
        else:
            print('That didn\'t do anything.')

     #if player types 'use' [item] 'with' [structure]
    if move[0] == 'use':
        if move[1] == 'amulet with dark alter':
            inventory.remove('amulet')
            inventory.append('dark amulet')
            print('A shadowy substance creeps from the alter and blackens the amulet')

## If a player enters a room with a monster while holding dark amulet
    if 'npc' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['npc'] and 'dark amulet' in inventory :
        del rooms[currentRoom]['npc']
        inventory.remove('dark amulet')
        inventory.append('unholy amulet')
        print("As you enter the room a monster lunges at you, the shadows concealed in the dark amulet tears through the air and impales the creature. \n"
                "The shadow tendrils slam the creature to the floor and starts to consumes it.")


    ## If an unprepared player enters a room with a monster
    if 'npc' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['npc']:
        print('A monster has got you... GAME OVER!')
        print(f" Your total moves through the game: {total_moves}")
        break

    ## Define how a player can win
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        print(f" Your total moves through the game: {total_moves}")
        break

    if 'unholy amulet' in inventory and currentRoom == 'Locked room':
        print('A voice echos in your head... "We have much to do, and nothing to stop us now."')
        print(f" Your total moves through the game: {total_moves}")
        break
