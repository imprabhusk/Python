""" Description:

You are responsible for writing a program that will display the solutions to
any number of quadratic equations. Your program will ask the user how many
quadratic equations they would like to solve, ask for the coefficients of the
equation in the standard form of ax2 + bx + c = 0 , solve for x, and then
display the solutions. Your program will allow for both real and complex
solutions.

Step By Step Guide:

● Print a welcome summary to the user.
    ○ This summary should describe a quadratic equation and complex numbers.
● Get user input for how many quadratic equations they would like to solve.
● Loop through the number of equations. Each iteration, you should:
    ○ Print a message header stating the equation number you are solving. 
    ○ Get user input for the values of the coefficients a, b, and c.
    ○ Solve for the roots of the quadratic x1 and x2.
        ■ In order to solve a quadratic equation, you may be required to take the
          square root of a negative value which would result in an imaginary number.
          The resulting solution is a complex number as it has both real and imaginary
          parts.
        ■ The previously introduced math library’s sqrt() function works well for real
          numbers but not for imaginary numbers. To work with imaginary values and complex
          numbers we will need to import a library of extra code.
        ■ Type import cmath as the first line of code in your program. 
    ○ Print a summary of the solutions to the equation.
● Once the loop is complete, print a message thanking the user for using the program.
● Use at least 2 comments to describe sections of your code.
● “Chunk” your code so that is readable.
● Use appropriate and informative variable names.
● Format your output.

"""