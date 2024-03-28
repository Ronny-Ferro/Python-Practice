# https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using
# input), compare them, print out a message of congratulations to the winner,
# and ask if the players want to start a new game)
import sys

player1 = input("What's your name: ")
player2 = input("What's your name: ")

player1_choice = input("Enter rock, paper, or scissors: ").lower()
player2_choice = input("Enter rock, paper, or scissors: ").lower()


def compare(u1, u2):
    if u1 == u2:
        return "It's a tie!"
    elif u1 == 'rock':
        if u2 == 'scissors':
            return "Rock wins!"
        else:
            return "Paper wins!"
    elif u1 == 'scissors':
        if u2 == 'paper':
            return "Scissors win!"
        else:
            return "Rock wins!"
    elif u1 == 'paper':
        if u2 == 'rock':
            return "Paper wins!"
        else:
            return "Scissors win!"
    else:
        return "Invalid input! You have not entered rock, paper or scissors, try again."
        sys.exit()

print(compare(player1_choice, player2_choice))
