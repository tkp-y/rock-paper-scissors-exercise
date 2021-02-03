
import random
#from random import choice


print("Rock, Paper, Scissors, Shoot!")


print("-------------------")
print("Welcome 'Player One' to my Rock-Paper-Scissors game...")
print("-------------------")

#asking user for an input

options = ["rock", "paper", "scissors"]

user_choice = input("Please choose either 'rock', 'paper', or 'scissors': ")

#validate the user selection

#stop the program (not try to determine the winnter)
#... if user choice is invalid

user_choice = user_choice.lower()

if user_choice in options:
    pass
else:
    print("Oops, please choose a valid option and try again.")
    exit()


#string interpolation / format string usage
#print(f"You chose: {x}")


print("You chose: " + user_choice)

#simulating a computer input



computer_choice = random.choice(options)
#computer_choice = choice(options)

print("The computer chose: " + computer_choice)





#determining who won

print("-------------------")

if computer_choice == user_choice:
    print("You and the computer tied.")
elif user_choice == "paper" and computer_choice == "rock":
        print("You win! Congrats")
elif user_choice == "paper" and computer_choice == "scissors":
        print("Oh! The computer won, that's ok!")
elif user_choice == "rock" and computer_choice == "paper":
        print("Oh! The computer won, that's ok!")
elif user_choice == "rock" and computer_choice == "scissors":
        print("You win! Congrats")
elif user_choice == "scissors" and computer_choice == "paper":
        print("You win! Congrats")
elif user_choice == "scissors" and computer_choice == "rock":
        print("Oh! The computer won, that's ok!")



print("-------------------")
print("Thanks for playing. Please play again!")