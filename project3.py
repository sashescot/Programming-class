#Game title: Escape!
#Setting: Mystery House
#Game summary:
#The ultimate goal is to go through all the rooms trying to find the exit
#Remember the house isn't your house, so you don't know you're way around 
#Once you reach the exit, the score updates to 1 point within python
#Global variables: The one variable used was a score variable which updates at the very end once you reach the exit
########
#import modules
#######

########
#define functions
#######
def start():
    print("You wake up in a dark house and need to find the exit. The game\nends once you've found the exit.")
    bedroom()

def bedroom():
    global score
    score = 0
    print("Your current score is" + str(score))
    print("You are currently in the bedroom, hint the hallway leads to almost every room")
    move = input("\nWhere would you like to go? Say one of these choices:\n\tbathroom\n\thallway\n")
    if move.lower() == "bathroom":
        bathroom()
    elif move.lower() == "hallway":
        hallway()
    else:
        print("That was not an option")
        bedroom()
        pass

def bathroom():
    global score
    score = 0
    print("Your current score is" + str(score))
    print("You are currently in the bathroom")
    move = input("\nWhere would you like to go? Say one of these choices:\n\thallway\n\tbedroom\n")
    if move.lower() == "hallway":
        hallway()
    elif move.lower() == "bedroom":
        bedroom()
    else:
        print("That was not an option")
        bathroom()
        pass

def hallway():
    global score
    score = 0
    print("Your current score is" + str(score))
    print("You are currently in the hallway")
    move = input("\nWhere would you like to go? Say one of these choices:\n\tdining area\n\tbedroom\n")
    if move.lower() == "dining area":
        dining_area()
    elif move.lower() == "bedroom":
        bedroom()
    else:
        print("That was not an option")
        hallway()
        pass
        
def dining_area():
    global score
    score = 0
    print("Your current score is" + str(score))
    print("Dining area: you notice a light so you decide to go towards it")
    move = input("\nWhere would you like to go? Say one of these choices:\n\tleft\n\tright\n")
    if move.lower() == "left":
        hallway()
    elif move.lower() == "right":
        living_room()
    else:
        print("That was not an option")
        dining_area()
        pass

def living_room():
    global score
    score = 0
    print("Your current score is" + str(score))
    print("Living room: almost there!")
    move = input("\nWhere would you like to go? Say one of these choices:\n\thallway\n\texit\n")
    if move.lower() == "hallway":
        hallway()
    elif move.lower() == "exit":
        exit()
    else:
        print("That was not an option")
        living_room()
        pass

def exit():
    global score
    score = score + 1
    print("Your current score is" + str(score))
    print("You now have a point")
    print("Yay! You found the exit and are now free!")
    print("*___*")

########
#main
#######
#TODO: Add some global variables
score = 0
start()