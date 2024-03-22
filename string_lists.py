# Ask the user for a string and print out whether this string is a
# palindrome or not. (A palindrome is a string that reads the same
# forwards and backwards.)

word = input("Enter a word: ").lower()
word = str(word)
reverse = word[::-1]
print(reverse)
print(word)
if word == reverse:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")