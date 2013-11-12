# Rock-paper-scissors-lizard-Spock template


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
    # don't forget to return the result!
    
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
    

    
def name_to_number(name):
    # fill in your code below
    # convert name to number using if/elif/else
    # don't forget to return the result!
    
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
    


def rpsls(name): 
    # fill in your code below
    # convert name to player_number using name_to_number
    
    print "Player chooses", name
    number = name_to_number(name)

    # compute random guess for comp_number using random.randrange()
    # convert comp_number to name using number_to_name
    comp_number = random.randrange(0,5,1)
    print "Computer chooses", number_to_name(comp_number)
    
    # compute difference of player_number and comp_number modulo five
    # use if/elif/else to determine winner
    if number == comp_number:
        print "Player and computer TIE!"
    elif (number - comp_number) %5 <= 2:
        print "PLAYER WINS!!"   
    else: print "COMPUTER WINS!!"

    # print results
    print ""
    
         
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


