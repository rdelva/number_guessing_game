"""
Python Development Techdegree
Project 1 - The Number Guessing Game
--------------------------------
"""

# Import the random module.
import random

def generate_number():
        #generates a random number
        return random.randint(1,10)



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
    answer = input("Are you ready to play? (yes/no) " )
    
    score = [] #create a scorebox to keep a record of all the scores

    while answer.lower() == 'yes': 

        counter = 0       
        max_number = 10
        min_number = 1   
        random_number = generate_number()  # generates a random number and assigns it to random_number      
        game_over = False  # A flag that allows the guessing loop to continue 
        
        #Only prints out the highest score if the array is filled and selects the highest score
        if len(score):
            print("Highest score for the Guessing Game is: {}".format( min(score)))             


        while game_over == False: #continue to run the game until the user guesses the random number
            
            try:
                guess = input("Please guess a number between 1 to 10. ")           
                guess = int(guess)
              
                #Raise a ValueError if the guess is higher than the max_number
                if guess > max_number:
                    raise ValueError("Please enter a value that is less than 10")
                elif guess < min_number: 
                    raise ValueError("Please enter a value that is more than 1")
            except ValueError as err:
                print("Please enter a numerical value. {}".format(err))             
            else: 
                #keep guessing until guess == random_number
                
                        if guess < random_number:
                            print("Guess again. The number is higher")
                            counter += 1
                            game_over = False                      
                        elif guess > random_number:
                            print("Guess again. The number is lower")
                            counter += 1
                            game_over = False
                        else:
                            print("That's correct. The number is {}. It tooks you {} tries. ".format(random_number, counter))                       
                            score.append(counter)
                            answer = input("Do you want to play again? ")
                            game_over = True
                            

    
    print("Thank you for playing,{}! Good Bye :) ".format(name))
           
  

# Kick off the program by calling the start_game function.
start_game()