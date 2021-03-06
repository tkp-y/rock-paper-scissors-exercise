import os
import random
#from random import choice

from dotenv import load_dotenv

load_dotenv()

#get player's name from .env file
PLAYER_NAME = os.getenv("PLAYER_NAME", default="Player One")

#welcome message
print("Rock, Paper, Scissors, Shoot!")


print("-------------------")
print("Welcome " + PLAYER_NAME + " to my Rock-Paper-Scissors game...")
print("-------------------")

#ask user how many times they wish to play
rounds = input("How many rounds do you wish to play? ")

#variable to count how many times user has won
wincount = 0

print("-------------------")

#run the game as many times as the user has chosen
for x in range(0,int(rounds)):

        #asking user for an input
        #create a list of valid options
        options = ["rock", "paper", "scissors"]

        user_choice = input("Please choose either 'rock', 'paper', or 'scissors': ")

        #validate the user selection

        #stop the program (not try to determine the winner)
        #... if user choice is invalid

        #change user choise to all lower case
        user_choice = user_choice.lower()

        #if the user choise is a valid option, move one
        if user_choice in options:
                pass
        #if the user choice is not a valid option, exit the game
        else:
                print("Oops, please choose a valid option and try again.")
                exit()


        #print out user choice
        print("You chose: " + user_choice)

        #simulating a computer input

        #assign computer a random choise
        computer_choice = random.choice(options)

        #print computer choice
        print("The computer chose: " + computer_choice)


        #determining who won

        print("-------------------")

        #adapted from from solution shared by student William in slack

        if computer_choice == user_choice:
                print("You and the computer tied.")
        elif user_choice == "paper" and computer_choice == "rock":
                print("You win! Congrats")
                wincount = wincount + 1 #add a win to the win count
        elif user_choice == "paper" and computer_choice == "scissors":
                print("Oh! The computer won, that's ok!")
        elif user_choice == "rock" and computer_choice == "paper":
                print("Oh! The computer won, that's ok!")
        elif user_choice == "rock" and computer_choice == "scissors":
                print("You win! Congrats")
                wincount = wincount + 1
        elif user_choice == "scissors" and computer_choice == "paper":
                print("You win! Congrats")
                wincount = wincount + 1
        elif user_choice == "scissors" and computer_choice == "rock":
                print("Oh! The computer won, that's ok!")


#print out farewell to user
print("-------------------")
#tell user how many times user won 
print("You won " + str(wincount) + " out of " + rounds + " rounds.")
print("Thanks for playing. Please play again!")