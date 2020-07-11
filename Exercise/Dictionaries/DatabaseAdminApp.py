""" Description:

You are responsible for writing a program that will simulate logging into a
database and prompting a user to change their password. All usernames and
passwords to the database will be stored in a dictionary. Upon entering the
correct credentials, your program will prompt the user to enter a new password
that is a minimum of eight characters long. If the new password meets the
criteria, it will be accepted, otherwise the new password will be rejected. If
the user who logged in is the admin, a list of all usernames and passwords
will be displayed.


Step by Step Guide:

● Print a welcome message.
● Create a dictionary called "log_on_information".
    ○ The key-value pairs in this dictionary will be username:password.
    ○ Store 5 keys.
        ■ Each key should be a string representing a username.
        ■ One username must be "admin00".
○ Store 5 values.
    ■ Each value should be a string representing a password at least 8 characters long.
● Get user input for their username.
● Follow the following conditional logic to control user interaction.
● If the username is in the database, get user input for their password.
    ○ If they enter the password correct, greet them with a message.
        ■ If the user that logged in is the admin00, display the whole dictionary.
        ■ Else, if the user who logged in is not the admin, ask the user if they would
          like to change their password.
● If the user wants to change their password, ask them for their newpassword and inform
  them that the password must be 8 characters long.
    ○ If the password is not 8 characters long, do not accept.
    ○ Else, If the password is 8 characters long or more, accept and display the username
      and new password.
● Else, if the user does not want to change their password, print a goodbye message.
    ○ Else, if the user enters their password incorrectly, inform the user.
● Else, If the username is not in the database, inform the user.
● Use at least 2 comments to describe sections of your code.
● “Chunk” your code so that is readable.
● Use appropriate and informative variable names.
● Format your output.

"""
