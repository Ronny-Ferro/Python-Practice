# https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
# Create a program that asks the user to enter their name
# and their age. Print out a message addressed to them that
# tells them the year that they will turn 100 years old.

# Extras:
# Add on to the previous program by asking the user for another number and
# printing out that many copies of the previous message.
# (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines.
# (Hint: the string "\n is the same as pressing the ENTER button)
name = input("Name: ")
age = int(input("Age: "))
year = 2023 - age + 100

print("Your name is "+ name + " and your age is " + str(age) + " you will turn 100 years old on " + str(year))