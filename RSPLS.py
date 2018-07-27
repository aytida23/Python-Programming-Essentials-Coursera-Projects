"""
Implementing Rock-Paper-Scissors-Lizard-Spock hand game
"""

import random

#making a name to number function
def name_to_number(name):
    """
    Takes a string name and then return into a number between 0 and 4
    """
    #conditions for taking string name and returning number
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return "An error occured, please fix the error and try again."


#making another function that converts number to name
def number_to_name(number):
    """
    A function that converts a number in the range of 0 to 4 into its
    corresponding name as a string.
    """
    #conditions for converting number in range of 0 to 4 into corresponding string
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return "An error occured, please fix the error and try again."


#making the main function rpsls
def rpsls(player_choice):
    """
    Given string player_choice it plays the RPSLS game,
    and return results in the console
    """
    #prints out a blank line
    print("")
    #message describing the players choice
    print("Player chooses ",player_choice)
    
    #computing player_number using name_to_number function
    player_number = name_to_number(player_choice)
    
    #computing comp_number using random.randrange() function
    comp_number = random.randrange(5)
    
    #computing comp_choice corresponding to the comp_number using number_to_name()
    comp_choice = number_to_name(comp_number)
    
    #message describing computers choice
    print("Computer chooses ",comp_choice)
    
    #computing the difference between comp_number and player_number taken modulo five
    difference = (comp_number - player_number) % 5

    #if-else conditions concerning the winner
    if (difference == 0):
        print("Palyer and computer tie!")
    elif (difference == 1) or (difference == 2):
        print("Computer wins!")
    else:
        print("Player wins!")
    


rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
