""" Description:

You are responsible for writing a program that simulates a thesaurus. Your
program will present a user with a list of words that your thesaurus contains.
Based on the users choice, you will randomly present them with a synonym for
their chosen word. Lastly, your program will display all of the potential
synonyms for each word in the thesaurus.

Step by Step Guide:

● Create a dictionary called "thesaurus".
    ○ You must have a minimum of four keys in the dictionary.
    ○ Each key should be a ​string​ of a word of your choice.
    ○ The associated values for each key should be a ​list ​containing five synonyms for
      the key.
● For example, my dictionary includes:
    "hot":['balmy', 'summery', 'tropical', 'boiling', 'scorching'], "cold":['chilly',
    'cool','freezing', 'frigid', 'polar'], "happy":['content', 'cheery', 'merry',
    'jovial', 'jocular'], "sad":['unhappy', 'downcast', 'miserable', 'glum',
    'melancholy'],
● Print a welcome message.
● Print what words are in your thesaurus.
    ○ This is represented by the keys of your dictionary
● Ask the user what word they would like to get a synonym for.
● If the users choice is in the thesaurus:
    ○ Chose a random synonym from the list containing the synonyms for the word.
        ■ Type import random as the first line of your program.
    ○ Display the information.
● Else, the word is not in the dictionary:
    ○ Inform the user.
● Ask the user if they would like to see the whole thesaurus.
    ○ This is represented by both the keys and values.
● If yes:
    ○ Display the whole dictionary following the format below.
● Else:
    ○ Print a goodbye message
● Use at least 2 comments to describe sections of your code.
● “Chunk” your code so that is readable.
● Use appropriate and informative variable names.
● Format your output.

"""

import random

thesaurus = {
    "hot": ["balmy", "summery", "tropical", "boiling", "scorching"],
    "cold": ["chilly", "cool", "freezing", "frigid", "polar"],
    "happy": ["content", "cheery", "merry", "jovial", "jocular"],
    "sad": ["unhappy", "downcast", "miserable", "glum", "melancholy"],
}

print("Welcome to the Thesaurus App")
print("\nChoose the word from the thesaurus and i will give you the synonym")
print("\nHere are the words in thesaurus")

# list all keys in thesaurus
for key in thesaurus.keys():
    print("\t", key)

word = input("\nWhat word would you like to get the synonym for : ")

# provide some random synonym
if word in thesaurus.keys():
    index = random.randint(0, 4)
    print(f"The synonym for the word {word} is : {thesaurus[word][index]}")
else:
    print(
        f"I'm sorry, Synonym for the word {word} currently doesn't exists on thesaurus."
    )

# Ask the user whether they want to see the whole thesaurus
choice = input("\nWould you like to see the whole thesaurus (yes/no) : ").lower()

# show all the values in thesaurus
if choice.startswith("y"):
    for key, values in thesaurus.items():
        print(f"\nSynonym for {key} are : ")
        for value in values:
            print("\t", value)


else:
    print("Thanks for using Thesaurus App. Hope You have enjoyed the program. GoodBye!")
