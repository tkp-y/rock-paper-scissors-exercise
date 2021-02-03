
import random


print("Rock, Paper, Scissors, Shoot!")


print("-------------------")
print("Welcome 'Player One' to my Rock-Paper-Scissors game...")
print("-------------------")

#asking user for an input


user_choice = input("Please choose either 'rock', 'paper', or 'scissors': ")




#string interpolation / format string usage
#print(f"You chose: {x}")


print("You chose: " + user_choice)

#simulating a computer input


options = ["rock", "paper", "scissors"]

computer_choice = random.choice(options)

print("The computer chose: " + computer_choice)

exit()

#determining who won

print("-------------------")
print("Oh, the computer won. It's ok.")
print("-------------------")
print("Thanks for playing. Please play again!")