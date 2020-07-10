""" Description:

You are responsible for writing a program that will simulate logging into a
business’s shipping accounts software. Once logged in your program will
display the current costs of shipping x amount of items. Based on the number
of items shipped, the cost to ship each item will vary. Once the cost to ship
an item is set, your program will calculate the cost of shipping the entire
order. Upon confirmation of the order, your program will place the order and
prepare the shipment.

Step by Step Guide:

● Begin by creating a list that will hold 5 user names of your choice.
    ○ For example: users = ['Jack', 'Mike', 'Smith', 'Alan', 'Jenny']
● Print a welcome message to the user.
● Get user input for their specific username.
    ○ Usernames should not be case sensitive. For example, mike ==   Mike.
● If the username is in the list of usernames:
    ○ Welcome the user.
    ○ Print the shipping price summary as formatted below.
    ○ Get user input for how many items they would like to ship.
    ○ Use an if, elif, else chain to determine the cost of shipping each item.
    ○ Calculate the users bill based on the number of items to ship and the cost
      of shipping each item.
        ■ Round this bill to two decimal places.
    ○ Print the results as formatted below.
    ○ Ask the user if they would like to place their order.
    ○ If the users answer starts with y:
        ■ Print a message confirming that their order has been placed.
    ○ Else:
        ■ Inform the user that no order has been placed.
● Else, the user does not have an account:
    ○ Inform the user and say goodbye.
● Use at least 2 comments to describe sections of your code.
● “Chunk” your code so that is readable.
● Use appropriate and informative variable names.
● Format your output.

"""

print("Welcome to the Shipping Accounts App")

# list of users
users = ["jack", "mike", "smith", "alan", "jenny"]
username = input("\nHello, What is your name : ").title().lower()

# Users in the lists only are allowed to shop
if username in users:
    # Print a price summary
    print(f"\nHello {username}. Welcome back to your account.")
    print("\nCurrent Shipping prices are as follows:")
    print("Shipping orders 0 to 100\t\t : $5.10 each")
    print("Shipping orders 100 to 500\t\t : $5.00 each")
    print("Shipping orders 500 to 1000\t\t : $4.95 each")
    print("Shipping orders over 1000\t\t : $5.10 each")

    # Determine the price based on how many items are shipped
    quantity = int(input("\nHow many items would you like to ship : "))

    if quantity < 100:
        cost = 5.10
    elif quantity < 500:
        cost = 5.00
    elif quantity < 1000:
        cost = 4.95
    else:
        cost = 4.80

    # Display final cost
    bill = quantity * cost
    bill = round(bill, 2)

    print(f"To ship {quantity} items it will cost you {bill}$ at {cost} per item.")

    choice = input("\nWould you like to place this order : ").lower()

    # place order if you desire
    if choice.startswith("y"):
        print(f"Okay, Your Order has been placed. Shipping your {quantity} items.")
    else:
        print("Okay, no order is being placed at this time.")

# If users not in users list are not allowed to shop. Add your name to users list to shop
# with us.
else:
    print(
        "\nSorry, You do not have an account with us. kindly create an account to shop\
with us. See you later. Goodbye."
    )
