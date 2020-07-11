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

print("Welcome to Database Admin App")

log_on_information = {
    "mooman74": "alskes145",
    "meramo1986": "kehns010101",
    "nickyD": "world1star",
    "george2": "booo3oha",
    "admin00": "admin1234",
}

username = input("\nEnter your username : ")

# Check username exits in log_on_information or not
if username in log_on_information.keys():

    # if username exists then allow them to type their password
    password = input("Enter your password : ")
    if password == log_on_information[username]:

        # if the user is admin then allow him to access the entire datebase
        if username == "admin00" and password == log_on_information[username]:
            print(f"\nHello {username}! You are logged in!")
            print("\nHere is the current database:")

            # Details of the database
            print("-----------------------------------------------")
            for key, value in log_on_information.items():
                print(f"Username : {key}\t\tPassword : {value}")
            print("-----------------------------------------------")

        # if usen is not admin, then give him the options to change their passwords
        else:
            print(f"\nHello {username}! You are logged in.")
            choice = input("\nWould you like to change password (yes/no): ").lower()

            # Ask user whether they wish to change password are not.
            if choice.startswith("y"):
                new_password = input("\nSet your New Password : ")
                if len(new_password) >= 8:
                    confirm_password = input("Confirm your password : ")

                    # if new password and confirm password same set new password to user
                    if new_password == confirm_password:
                        log_on_information[username] = new_password
                        print(f"\nHello {username} your password is {new_password}")
                        print("Your password has been set successfully")

                    # if new password is not equal to typed password
                    else:
                        print("\nYour Typed password doesn't match")
                        print("Please Try Again")

                # if password is less than 8 characters
                else:
                    print("\nNote : Your password should contain minimum 8 characters")

            # if user doesn't want to change the passwords, greet them for login
            else:
                print(f"\nThanks {username} for logging in.")

    # if password is incorrect
    else:
        print("\nInvalid Password! Try Again")

# if user doesn't exists
else:
    print(f"\nUsername with {username} doesn't exists on the database.")
    print("You don't have access to log on information")
