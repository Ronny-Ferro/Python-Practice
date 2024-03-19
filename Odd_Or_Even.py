# https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
# The exercise comes first (with a few extras if you want the extra challenge or want to spend more time), followed by a discussion. Enjoy!

# Ask the user for a number. Depending on whether the number is even or
# odd, print out an appropriate message to the user.
# Hint: how does an even / odd number react differently when
# divided by 2?

# Extras:

# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one
# number to divide by (check). If check divides evenly into num, tell
# that to the user. If not, print a different appropriate message.

number = int(input("Enter a number: "))


def oddoreven():
    if number % 2 == 0 and number % 4 == 0:
        print(f"The number {number} is even and divisible by 4.")
    elif number % 2 == 0 and number % 4 != 0:
        print(f"The number {number} is even.")
    else:
        print(f"The number {number} is odd.")


oddoreven()
