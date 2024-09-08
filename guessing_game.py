"""
Python Development Techdegree
Project 1 - The Number Guessing Game
--------------------------------
"""

# Import the random module.
import random

# Create the start_game function.
def start_game():
#   When the program starts, we want to:
#   ------------------------------------
#   1. Display an intro/welcome message to the player.
#   2. Store a random number as the answer/solution.
#   3. Continuously prompt the player for a guess.
#     a. If the guess is greater than the solution, display to the player "It's lower".
#     b. If the guess is less than the solution, display to the player "It's higher".

#   4. Once the guess is correct, stop looping, inform the user they "Got it"
#      and show how many attempts it took them to get the correct number.
#   5. Let the player know the game is ending, or something that indicates the game is over.

# ( You can add more features/enhancements if you'd like to. )
    #Display intro/welcome message
    name = input("What is your name? ")
    print("Hello {},  and welcome to The Number Guessing Game. I'm your host Rose!! \n Today you will guess a number between 1 to 10."
          .format(name))
    answer = input("Are you ready to play? " )
    number = random.randint(1,10)
   
    print("RANDOM NUMBER: ", number)
    counter = 0
    score = []


    while answer.lower() == 'yes': 
        max_number = 10      
       
        #Only prints out the highest score if the array is filled and selects the highest score
        if len(score):
            print("Highest score for the Guessing Game is: {}".format( min(score)))
        print("RANDOM NUMBER: ", number)
        guess = int(input("Please guess a number between 1 to 10. "))
        if guess < max_number + 1:
            if guess < number:
                print("Guess again!. It's higher.")
                counter += 1 
            elif guess > number:
                print("Guess again!. It's lower")
                counter += 1
            elif guess > max_number:
                print("THATS WAAAAY TO HIGH!!!! Try again.")
                counter += 1
            else:
                print("That's correct. The number is {}. It took you {} tries".format(number, counter))
                score.append(counter)
                answer = input("Do you want to play again? ")
        else:
            print("You are out of bounds. Try again!!!")
           
            
            

       
        


# Kick off the program by calling the start_game function.

start_game()