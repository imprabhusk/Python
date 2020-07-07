""" Description:

You are responsible for writing a program that will generate binary and
hexadecimal values from 1 up to a specified user value. Recall that decimal is
a base 10 number system, binary is a base 2 number system, and hexadecimal is
a base 16 number system. Your program will use list slicing to first only show
a portion of these values. Your program will then loop through the entire
lists of decimal, binary, and hexadecimal values to show the relationship
between numbers of different bases.

Step By Step Guide:
● Print a welcome message.
● Get user input for how many values they would like to convert to binary and
hexadecimal.
● Using the range function, generate a list of numbers holding the decimal values
  from 1 up to the users maximum value.
● Create a blank list for the binary values.
● Create a blank list for the hexadecimal values.
● Use a for loop to loop through the decimal values. During each iteration:
    ○ Determine the binary representation and hexadecimal representation of the
      decimal value and add each value to the appropriate list.
        ■ To accomplish this use the built in bin() and hex() functions.
        ■ Google or check the python documentation on how to use these functions.
● Print a message informing the user that the lists are complete.
● Rather than print the whole list initially, use slicing to only show a portion of each list.
    ○ Get user input for the decimal number to start and stop at.
    ○ Be careful and think as to how these numbers relate to the indices of a list slice
● Print a message for each list slice.
● Use a for loop to loop through the portion of the list specified and print each element.
● Prompt the user to press Enter to see the entire list generated.
    ○ To pause a program you can use an input statement.
● Print a table header.
● Using only one for loop, print the decimal, binary, and hexadecimal values for each
element in each list.
    ○ This can be accomplished using the zip() function or proper list indexing.
● Use at least 2 comments to describe sections of your code.
● “Chunk” your code so that is readable.
● Use appropriate and informative variable names.
● Format your output.

"""

print('Welcome to Binary to Hexadecimal Conversion App')

# Get user input and generate list.
max_value = int(input('\nCompute binary and hexadecimal values up to the following decimal number : '))

decimal = list(range(1, max_value + 1))

binary = []
hexadecimal = []

for num in decimal:
    binary.append(bin(num))
    hexadecimal.append(hex(num))

print("\nGenerating Lists... Complete!")

# Get slicing index from user.
print("\nUsing slices you will now show a portion of each list")
lower_range = int(input('\nWhat decimal number would you like to start at : '))
upper_range = int(input('What decimal number would you like to stop at : '))

# Slice through each list individually.
print(f"\nDecimal values from {lower_range} and {upper_range} : ")
for num in binary[lower_range - 1 : upper_range]:
    print(num)

print(f"\nHexadecimal values from {lower_range} and {upper_range} : ")
for num in hexadecimal[lower_range - 1 : upper_range]:
    print(num)

# Format the output
input(f"\nPress Enter to see all values from 1 to {max_value}.")
print("\nDecimal\t\tBinary\t\tHexadecimal")
print('-------------------------------------------')
for d, b, h in zip(decimal, binary, hexadecimal):
    print(f"{d}\t\t{b}\t\t{h}")