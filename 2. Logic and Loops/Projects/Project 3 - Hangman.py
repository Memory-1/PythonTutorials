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

