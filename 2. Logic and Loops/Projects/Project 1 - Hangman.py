"""
This project may be a bit more challenging. There is a lot which I haven't included. However, I do provide
some to-do chunks to guide you on what you should do. These chunks are at the correct tab location. It's important
that you keep it at the same tabbed location.

Hangman:

This game will choose a random word and the user will be prompted to guess a letter. If the letter is correct, then it
will display it at the correct location in word.

If the user guesses a letter wrong, they'll get a strike. On the sixth incorrect guess, the user loses.

If the user has guessed all of the correct letters. break of out the loop (use the keyword break)

I've provided a way to display the word with the correct letters and underscores for the missing letters
ex) if the word was test, and the user has guessed t. generate_remaining_word() will return "T _ _ T"


Your challenge is to practice if statements and do the necessary code in that as outlined with the to do statements.

(I believe) I've included everything you need to complete this.
"""


import random

wordbank = ["abruptly", "absurd", "abyss", "affix", "askew", "avenue", "awkward", "axiom", "azure", "bagpipes", "bandwagon", "banjo", "bayou", "beekeeper", "bikini", "blitz", "blizzard", "boggle", "bookworm", "boxcar", "boxful", "buckaroo", "buffalo", "buffoon", "buxom", "buzzard", "buzzing", "buzzwords", "caliph", "cobweb", "cockiness", "croquet", "crypt", "curacao", "cycle", "daiquiri", "dirndl", "disavow", "dizzying", "duplex", "dwarves", "embezzle", "equip", "espionage", "euouae", "exodus", "faking", "fishhook", "fixable", "fjord", "flapjack", "flopping", "fluffiness", "flyby", "foxglove", "frazzled", "frizzled", "fuchsia", "funny", "gabby", 'happy', 'pencil', "stronghold", "stronghold", "stymied", "subway", "swivel", "syndrome", "thriftless", "thumbscrew", "topaz", "transcript", "transgress", "transplant", "triphthong", "twelfth", "twelfths", "unknown", "unworthy", "unzip", "uptown", "vaporize", "vixen", "vodka", "voodoo", "vortex", "voyeurism", "walkway", "waltz", "wave", "wavy", "waxy", "wellspring", "wheezy", "whiskey", "whizzing", "whomever", "wimpy", "witchcraft", "wizard", "woozy", "wristwatch", "wyvern", "xylophone", "yachtsman", "yippee", "yoked", "youthful", "yummy", "zephyr", "zigzag"]
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
used_letters = []


# Pick a random word
random_num = random.randint(0, len(wordbank))
word_of_the_game = wordbank[random_num]

# NOTE TO SELF: MAYBE LET PEOPLE MAKE THIS FUNCTION?
def generate_remaining_word():
    blank_word = ""
    for letter in word_of_the_game:
        if letter in used_letters:
            blank_word = letter + " "
        else:
            blank_word = "_ "

# While game isn't complete, number of incorrect guesses are less than 7,
while ():
    print(generate_remaining_word())
    usr_input = input("Guess: ")

    # Skips over invalid input
    if (usr_input not in letters):
        print("please enter a correct value")
        continue

    # TODO: If letter is in the word_of_the_game, add it to used letter and continue

    # TODO: If the letter is not in the the word_of_the_game, increase the incorrect guesses counter.

    # TODO: Check if the game has been won. If so, break out of the while loop.

    # TODO: Check if the game has been lost, if so, break

# TODO: Display whether the user won or lost.

