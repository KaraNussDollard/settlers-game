from random import randint

# this will be the main code for the game. Can eventually define functions
# in separate files and then import them here for cleaner code.

hand_resources = []

def roll(hand_resources):
    """rolls dice for player, identifies output, adds to hand"""
    # may want to add player name as argument?

    dice = randint(1, 6)
    print "You rolled a %d" % dice
    if dice == 1:
        print "You get a wheat."
        hand_resources.append("wheat")
    elif dice == 2:
        print "You get a wood."
        hand_resources.append("wood")
    elif dice == 3:
        print "You get an iron."
        hand_resources.append("iron")
    elif dice == 4:
        print "You get a sheep."
        hand_resources.append("sheep")
    elif dice == 5:
        print "You get a brick."
        hand_resources.append("brick")
    else:
        print "Something else happens."
        #figure this out later.
    print "In your hand you have", hand_resources

    print "Do you want to roll again?"
    global roll_again
    roll_again = raw_input("Y or N: ")

    return hand_resources
    return roll_again

def buy():
    print "To buy a road, you need 1 brick and 1 wood."
    print "To buy a settlement, you need 1 brick, 1 wood, 1 sheep, and 1 iron."
    print "To buy a city, you need 3 iron and 2 wheat."

    # need way to count items in list
    # could use pop to remove items from list?
    # may be better to have a count for each resource type
    # could resources be a class?
    # could use += and -=


roll(hand_resources)

while roll_again == "Y":
    print "Okay, here we go."
    roll(hand_resources)

print "Do you want to buy something?"
buy_choice = raw_input("Y or N: ")

if buy_choice == "N":
    print "Okay, it is the next player's turn."
else:
    buy()
