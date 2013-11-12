# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random

# initialize global variables used in your code

secret_number = 0
attempts = 0

# helper function to start and restart the game
def new_game():
    print ""
    print "try to guess the secret number[0,100)"
    print ""
    global secret_number
    global attempts
    attempts = 7
    secret_number = random.randrange(0, 100)
    return secret_number

# define event handlers for control panel

def range100():
    # button that changes range to range [0,100) and restarts
    new_game()

def range1000():
    # button that changes range to range [0,1000) and restarts
    print ""
    print "range changed up to 1000"
    print ""
    global secret_number
    global attempts
    attempts = 10
    secret_number = random.randrange(0, 1000)
    return secret_number
    
def input_guess(guess):
    # main game logic goes here
    
    global attempts
    print "Your guess was", guess
    attempts = attempts-1
    print "Number of remaining guesses:", attempts

    if attempts > 0:
        if int(guess) > secret_number:
            print "LOWER!!"
            print ""
        elif int(guess) < secret_number:
            print "HIGHER"
            print ""
        elif int(guess) == secret_number:
            print "CORRECT!!"
            print ""
            attempts = 7
            new_game()
    else:
        print ""
        print "Game over. The name was:", secret_number
        print "New game starts!"
        attempts = 7
        new_game()
            
# create frame

f = simplegui.create_frame("Guess The Number",300,300)

# register event handlers for control elements

f.add_input("Enter a Guess", input_guess, 200)
f.add_button("Range [0,100)", range100, 200)
f.add_button("Range [0,1000)", range1000, 200)


# call new_game and start frame
new_game()
f.start()