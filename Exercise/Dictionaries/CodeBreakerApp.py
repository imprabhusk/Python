""" Description:

You are responsible for writing a program that will encode or decode a message
based off the letter distribution of a predetermined key text. Your program
will determine a frequency analysis for two texts and use these letter
distributions to create a cipher to either encode or decode a message based
off user input. This program is an extension of the Frequency Analysis App.

Step by Step Guide:

● Begin by copying your code from the Frequency Analysis App
● Print a new welcome message.
● Comment out the user input for getting key_phrase_1 (key_phase_1 value given below)
● Hard code a predetermined phrase between you and the person you are communicating
  with for key_phase_1. I am using excerpts from Sherlock Holmes, but anything will do.
● Comment out the user input for getting key_phrase_2
● Hard code a predetermined phrase between you and the person you are communicating
  with for key_phase_2. (key_phase_2 value given below)
  I am using excerpts from Sherlock Holmes, but anything will do.
● You should be able to encode or decode a message regardless of the key phrases chosen.
● To In order to accomplish this, you must look at the frequency analysis of the two key
  phrases.
● Given a character in the secret message that is to be encoded, you must find its index
  in the frequency analysis of the first message.
● Then find the letter that appears at the same index in the frequency analysis of the
  second message.
● This is your encoding rule to encode one character as another.
● For example, the letter "o" appears at index 1 in the first frequency analysis. The
  letter "t" appears at index 1 in the second frequency analysis. Therefore the letter
  “o” would be encoded to the letter “t”.
● The letter “h” appears at index 7 in the first frequency analysis. The letter “r”
  appears at index 7 in the second frequency analysis. Therefore the letter “h” would be
  encoded to the letter “r”.
● Similarly, the word “oh” would be encoded to “tr” using the given key phrases.

NEW CODE TO ADD:

● Ask the user if they would like to encode or decode a message.
● Ask the user for the message.
    ○ You should take proper precautions to make the message all lower case.
    ○ You should take proper precautions to remove all non-letters from their message.
● If the user chose to encode the message, run an algorithm to encode and print the
  message.
    ○ Create a blank list called encoded_phrase.
    ○ For each letter that is in the phrase:
        ■ Create a variable called index and set it equal to the index of the current
          letter in key_phrase_1_ordered_letters.
● To accomplish this you can use the .index() method.
● Google or check Python documentation on the .index() method.
        ■ Create a variable called letter and set it equal to the letter that appears in
          key_phrase_2_ordered_letters at the specified index.
        ■ Append letter to the list encoded_phrase.
    ○ Print the encoded message.
        ■ There are multiple ways to do this. You may use the end= argument of the print
          function or the .join() method for strings.
● Elif the user chose to decode the message, run an algorithm to decode and print the
  message.
    ○ Create a blank list called decoded_phrase.
    ○ For each letter that is in the phrase:
        ■ Create a variable called index and set it equal to the index of the current
          letter in key_phrase_2_ordered_letters.
● To accomplish this you can use the .index() method.
● Google or check Python documentation on the .index() method.
        ■ Create a variable called letter and set it equal to the letter that appears
          in key_phrase_1_ordered_letters at the specified index.
        ■ Append letter to the list encoded_phrase.
    ○ Print the decoded message.
        ■ There are multiple ways to do this. You may use the end= argument of the print
          function or the .join() method for strings.
● Else, the user chose an invalid option and inform them.
● Use at least 2 comments to describe sections of your code.
● “Chunk” your code so that is readable.
● Use appropriate and informative variable names.
● Format your output.

"""

# key_phrase_1 = """
# To Sherlock Holmes she is always the woman. I have seldom heard him mention
# her under any other name. In his eyes she eclipses and predominates the whole
# of her sex. It was not that he felt any emotion akin to love for Irene Adler.
# All emotions, and that one particularly, were abhorrent to his cold, precise
# but admirably balanced mind. He was, I take it, the most perfect reasoning and
# observing machine that the world has seen, but as a lover he would have placed
# himself in a false position. He never spoke of the softer passions, save with
# a gibe and a sneer. They were admirable things for the observer excellent for
# drawing the veil from men's motives and actions. But for the trained reasoner
# to admit such intrusions into his own delicate and finely adjusted temperament
# was to introduce a distracting factor which might throw a doubt upon all his
# mental results. Grit in a sensitive instrument, or a crack in one of his own
# highpower lenses, would not be more disturbing than a strong emotion in a
# nature such as his. And yet there was but one woman to him, and that woman was
# the late Irene Adler, of dubious and questionable memory. I had seen little of
# Holmes lately. My marriage had drifted us away from each other. My own
# complete happiness, and the homecentred interests which rise up around the man
# who first finds himself master of his own establishment, were sufficient to
# absorb all my attention, while Holmes, who loathed every form of society with
# his whole Bohemian soul, remained in our lodgings in Baker Street, buried
# among his old books, and alternating from week to week between cocaine and
# ambition, the drowsiness of the drug, and the fierce energy of his own keen
# nature. He was still, as ever, deeply attracted by the study of crime, and
# occupied his immense faculties and extraordinary powers of observation in
# following out those clues, and clearing up those mysteries which had been
# abandoned as hopeless by the official police. From time to time I heard some
# vague account of his doings: of his summons to Odessa in the case of the
# Trepoff murder, of his clearing up of the singular tragedy of the Atkinson
# brothers at Trincomalee, and finally of the mission which he had accomplished
# so delicately and successfully for the reigning family of Holland. Beyond
# these signs of his activity, however, which I merely shared with all the
# readers of the daily press, I knew little of my former friend and companion.
# """
# key_phrase_2 = """
# Quite so! You have not observed. And yet you have seen. That is just my point.
# Now, I know that there are seventeen steps, because I have both seen and
# observed. By the way, since you are interested in these little problems, and
# since you are good enough to chronicle one or two of my trifling experiences,
# you may be interested in this. He threw over a sheet of thick, pink tinted
# notepaper which had been lying open upon the table. It came by the last post,
# said he. Read it aloud. The note was undated, and without either signature or
# address. There will call upon you tonight, at a quarter to eight o'clock, it
# said, "a gentleman who desires to consult you upon a matter of the very
# deepest moment. Your recent services to one of the royal houses of Europe have
# shown that you are one who may safely be trusted with matters which are of an
# importance which can hardly be exaggerated. This account of you we have from
# all quarters received. Be in your chamber then at that hour, and do not take
# it amiss if your visitor wear a mask. This is indeed a mystery, I remarked.
# What do you imagine that it means? I have no data yet. It is a capital mistake
# to theorise before one has data. Insensibly one begins to twist facts to suit
# theories, instead of theories to suit facts. But the note itself. What do you
# deduce from it? I carefully examined the writing, and the paper upon which it
# was written. The man who wrote it was presumably well to do, I remarked,
# endeavouring to imitate my companion's processes. Such paper could not be
# bought under half a crown a packet. It is peculiarly strong and stiff.
# """
