# ## https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html
# write a program that prints out all the elements of the list
# that are less than 5.
# Instead of printing the elements one by one, make a new list that
# has all the elements less than 5 from this list in it and print
# out this new list.
# Write this in one line of Python.
# Ask the user for a number and return a list that contains only
# elements from the original list a that are smaller than that
# number given by the user.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print([element for element in a if element<=5])

numbers = [7,3,13,6,8,5,1,2,4,15,9,10,12,14,11]
lessFnums = []
lessNnums = []

for num in numbers:
    if num < 5:
        lessFnums.append(num)
        lessNnums.sort()
print(lessFnums)
print()

num = int(input("Enter a number: "))
for n in numbers:
    if n < num:
        lessNnums.append(n)
        lessNnums.sort()
print(lessNnums)