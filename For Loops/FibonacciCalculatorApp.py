""" Description:

You are responsible for writing a program that will compute the first n terms
of the Fibonacci Sequence. Your program will then display these terms. Next,
your program will calculate the ratios of consecutive Fibonacci numbers to
prove that these ratios approach the irrational mathematical constant of Phi;
1.618....

Step By Step Guide:

● Print a welcome message.
● Get user input for how many digits of the Fibonacci Sequence they would like to
compute.
● Define a list which holds two integers, 1 and 1.
    ○ This is the start of your Fibonacci Sequence.
● Using a for loop, write an algorithm that will compute the next term of the Fibonacci
  Sequence and append it to your list.
    ○ The nth term of the Fibonacci Sequence can be found by adding the n-1 and n-2 terms
      together.
    ○ You essentially take the previous two terms in the sequence and add them together to
      get the current term.
● Iterate over this loop until you reach the desired number of terms.
● Display the results of your algorithm.
● Define an empty list that will hold the ratios of consecutive terms from your Fibonacci
  Sequence.
    ○ These ratios will approach a value of Phi; 1.618....
● Using a for loop, write an algorithm that will compute these ratios.
    ○ To compute this ratio, you will divide the 2nd term in your list by the first.
    ○ The next iteration, you will divide the 3rd term by the 2nd.
    ○ The next iteration, the 4th term by the 3rd, and so forth.
● Each time you compute this ratio, append it to your list.
● Display the results of your algorithm.
● Print a statement about the Golden Ratio and Fibonacci.
● Use at least 2 comments to describe sections of your code.
● “Chunk” your code so that is readable.
● Use appropriate and informative variable names.
● Format your output.

"""