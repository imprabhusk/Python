""" Description:

You are responsible for writing a program that will convert any given
speed in miles per hour to a more metric friendly unit of meters per
second. All calculations should be rounded to a set decimal precision of 2
decimal places.

Step by Step Guide:

● Print a welcome message.
● Get user input for their speed in miles per hour.
    ○ Allow for a decimal speed.
● Convert the speed in miles per hour to meters per second.
    ○ Use a conversion ratio of 1 mph = 0.4474 mps.
    ○ Use the round() function to round this speed to 2 decimal places.
    ○ Check the python documentation for information on how to use the round()
      function.
● Print a message to the user that informs them of their speed in meters per
  second.
● Use at least 2 comments to describe sections of your code.
● “Chunk” your code so that is readable.
● Use appropriate and informative variable names.
● Format your output.

"""

print("Welcome to Miles per Hour to Meter per Second Conversion App")

# Gathering user input which accepts decimal number
miles_per_hour = float(input("\nWhat is your speed in miles per hour : "))

# miles per hour to meter per second conversion
meter_per_second = miles_per_hour * 0.4475

# Format the output
print(f"\nYour speed in meter per second is {round(meter_per_second, 2)}")
