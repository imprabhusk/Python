""" Description

You are responsible for writing a program that simulates the Power Ball
Lottery. The traditional power ball is played by randomly choosing 5 white
balls numbered 1 through 69 then randomly choosing 1 red ball numbered 1
through 26. The traditional power ball has astronomically low odds of
winning. Therefore, your program will allow users to adjust the odds by
setting how many balls the lottery will choose from. Your program will
then calculate the odds the user has of winning. The user will purchase
tickets in a set interval, without purchasing repeated losing tickets,
until they either win the lottery or choose to give up.

Step By Step Guide:

● Print a welcome message as formatted below.
● The normal Power Ball Lottery chooses 5 random white balls numbered 1
  through 69.
● Once a ball is chosen, it cannot be chosen again.
● Using all 69 balls will make winning the lottery nearly impossible.
  Therefore, we want to give the user the option to set how many white balls
  they will pick from.
● Get user input for the number of white balls to use.
    ○ Store this user input in a variable called white_balls.
● If the user entered a number less than 5, set the value of white_balls to
  five.
    ○ This ensures that we have enough numbers to choose from.
● Similarly, the red Power Ball is normally chosen from red balls numbered 1
  through 26.
● We want to give the user the option to set how many red balls they will pick
  from.
● Get user input for the number of red balls to use.
    ○ Store this input in a variable called red_balls.
● If the user entered a number less than 1, set the value of red_balls to one.
    ○ This ensures we have at least one power ball.
● Generate the odds the user will win this specific lottery.
● Create a variable called odds and set it equal to 1.
    ○ You will use this variable to perform repeated multiplication.
● Use a for loop to loop an appropriate number of times to perform the correct
  multiplication. Your for loop should be a numerical for loop such as for i in
  range(5):
    ○ For example, if the user wanted 69 white balls and 26 red balls the odds
      would be calculated as follows: (69*68*67*66*65)*26/120.
    ○ For example, if the user wanted 20 white balls and 4 red balls the odds
      would be calculated as follows: (20*19*18*17*16)*4/120.
    ○ Try to determine the relationship between the number of white balls used,
      the value of i in the for loop, and the terms being multiplied together
      to get the odds.
● Determine the odds for any specific lottery given and print the odds to the
  user.
● We will allow users to purchase tickets in a set interval.
● Get user input for how many tickets they would like to purchase in each
  interval.
    ○ Store this input in a variable called ticket_interval.
● Next, we need to simulate creating the winning lotto numbers.
● Each lottery ball will be represented by a random integer.
    ○ Type import random as the first line of code in your program.
● Create a blank list called winning_numbers.
● Generate the numbers to represent the white balls.
    ○ While there are less than 5 values in winning_numbers:
        ■ Generate a random integer from 1 up to the users value of
          white_balls.
        ■ If the integer does not already appear in the list winning_numbers:
            ● Append the integer to the list winning_numbers. We cannot have
              repeated values.
● Permanently sort the list winning_numbers.
● Generate the number to represent the red power ball.
    ○ Generate a random integer from 1 up to the users value of red_balls.
    ○ Append this to the end of the list winning_numbers.
    ○ Do not sort the list as the red power ball is always at the end of the
      winning numbers.
● You now have a list of numbers, winning_numbers that represent the winning
  Power Ball numbers; 5 numbers that are ordered and then one final Power Ball
  number added at the end.
    ○ For example [10, 22, 24, 54, 67, 3]
● Now, simulate the actual Power Ball drawing.
● Print a welcome message as formatted below.
● Display the winning power ball numbers all on one line as formatted below.
    ○ Use the end= argument.
● Prompt the user to press enter to being purchasing tickets.
● Create a variable called tickets_purchased and set it equal to 0.
    ○ This will keep track of how many tickets have been created.
    ○ Every time your while loop runs you should increment this by 1.
● Create a flag variable called active and set it to True.
    ○ This variable will stay True as long as the user wants to continue to
      purchase tickets. After, the number of tickets stored in ticket_interval
      have been created, ask the user if they want to purchase more. If they do
      not, set this variable to False.
● Create a blank list called tickets_sold.
    ○ This will keep track of every ticket that has been sold.
    ○ We will use this list to make sure that we don't purchase a losing ticket
      more than once.
● Use a while loop that will continue to run until a winning ticket is picked
  or user wants to stop wasting their money. This loop needs to check two
  conditions: The winning ticket has not been sold and the user still wants to
  play.
    ○ Create a blank list called lottery_numbers which will hold the current
      lottery numbers of a ticket that is being purchased.
        ■ Once the ticket is created and determined to be a loser, you can use
          this same variable for the next ticket.
    ○ Simulate picking a lottery ticket.
        ■ You should do this in a similar manner to picking the actual power
          ball numbers. Pick 5 numbers, sort them, and then add a 6th.
    ○ If the current ticket is not in your list of tickets sold:
        ■ Increase the number of purchased tickets by 1.
        ■ Add it to the list of tickets sold,
        ■ Print the ticket as a list.
    ○ Else:  
        ■ Print a message that a losing ticket was generated that has already
          been purchased and that the ticket is being disregarded.
    ○ After picking the number of tickets in ticket_interval, which can be
      checked using modulo division:
        ■ Print the total number of tickets purchased.
        ■ Get user input for if they would like to continue purchasing tickets.
        ■ If the user does not want to continue:
            ● Set your flag variable to False
● The while loop will end either by purchasing the winning ticket or by giving
  up.
● If the current lottery ticket is equal to the winning ticket:
    ○ You won the lottery!
    ○ Print the winning ticket numbers.
    ○ Print the total number of tickets purchased.
● Else
    ○ You didn’t win the lottery.
    ○ Print how many tickets were purchased.
● Use at least 2 comments to describe sections of your code.
● “Chunk” your code so that is readable.
● Use appropriate and informative variable names.
● Format your output.

"""
