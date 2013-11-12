#IVAN
# Rock-paper-scissors-lizard-Spock template
# try code here: http://www.codeskulptor.org/#user24_L58PGa0tBvnsNaL_5.py


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random

def number_to_name(number):
    # fill in your code below
    # convert number to a name using if/elif/else
    if number == 0:
        name = "rock"
        return name
    elif number == 1:
        name = "Spock"
        return name
    elif number == 2:
        name = "paper"
        return name
    elif number == 3:
        name = "lizard"
        return name
    elif number == 4:
        name = "scissors"
        return name
    else: print "you need to imput a number between 0-4"
# don't forget to return the result!


def name_to_number(name):
    # fill in your code below
    # convert name to number using if/elif/else
    if name == "rock":
        number = 0
        return number
    elif name == "Spock":
        number = 1
        return number
    elif name == "paper":
        number = 2
        return number
    elif name == "lizard":
        number = 3
        return number
    elif name == "scissors":
        number = 4
        return number
    else: print "you need to imput a correct string"

# don't forget to return the result!


def rpsls(name):
    # fill in your code below
    # convert name to player_number using name_to_number
    print "Player chooses", name
    number = name_to_number(name)
    
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5,1)
    print "Computer chooses", number_to_name(comp_number)
    
    # compute difference of player_number and comp_number modulo five
    # use if/elif/else to determine winner
    if number == comp_number:
        print "Player and computer tie!"
    elif (number - comp_number)%5<=2:
        print "PLAYER WINS!!"
    else: print "COMPUTER WINS!!"

    # convert comp_number to name using number_to_name
    # print results
    print ""



# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric

