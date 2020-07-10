""" Description:

You are responsible for writing a program that will convert a given
temperature in degrees Fahrenheit to degrees Celsius and degrees Kelvin. Your
program will round all conversions to a precision of four decimal places.
Lastly, your program will display the results in a convenient table style
format.

Step by Step Guide:

● Print a welcome message.
● Get user input for their given temperature in degrees Fahrenheit.
    ○ Allow for a decimal temperature.
● Convert the temperature into both Celsius and Kelvin.
    ○ If you are unsure of the conversion ratios, google is your friend.
    ○ Round all values to 4 decimal places.
● Display all three temperatures such that the temperature values are
  aligned when printing.
● Use at least 2 comments to describe sections of your code.
● “Chunk” your code so that is readable.
● Use appropriate and informative variable names.
● Format your output as below.

"""

print("Welcome to Temprature Conversion App")

temperature_in_fahrenheit = float(
    input("\nWhat is the given temperature in degree fahrenheit : ")
)

# temperature conversion to celsius
temperature_in_celsius = (5 / 9) * (temperature_in_fahrenheit - 32)

# temperature conversion to kelvin
temperature_in_kelvin = temperature_in_celsius + 273.15

# Format output
print(f"\nDegrees in Fahrenheit is {round(temperature_in_fahrenheit, 4)}")
print(f"\nDegrees in Celsius is {round(temperature_in_celsius, 4)}")
print(f"\nDegrees in Kelvin is {round(temperature_in_kelvin, 4)}")
