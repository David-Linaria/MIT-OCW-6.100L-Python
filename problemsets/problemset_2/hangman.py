# Problem Set 2, hangman.py
# Name: David Linaria
# Collaborators: \
# Time spent: 1h 30mins

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

def get_help(secret_word, avail_letters):
    choose_from = ''
    for char in secret_word:
        if (char in avail_letters) and (char not in choose_from):
            choose_from += char
    new = random.randint(0, len(choose_from) - 1)
    revealed_letter = choose_from[new]
    return revealed_letter

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for char in secret_word:
        if char not in letters_guessed:
            return False
    return True
    #pass


def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessed_word = ''
    for i in range(len(secret_word)):
        if secret_word[i] in letters_guessed:
            guessed_word += secret_word[i]
        else:
            guessed_word += '*'
    return guessed_word
    #pass


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    avail_letters = ''
    for char in string.ascii_lowercase:
        if char not in letters_guessed:
            avail_letters += char
    return avail_letters
    #pass



def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    surplus_guess_count = 10
    letters_guessed = []
    print('Welcome to Hangman!')
    print(f'I am thinking of a word that is {len(secret_word)} letters long.')
    while not with_help:
        print(f'--------------')
        if surplus_guess_count <= 0:
            print(f'Sorry, you ran out of guesses. The word was {secret_word}.')
            return None

        elif has_player_won(secret_word, letters_guessed):
            unique_letters_in_secretword = ''
            for char in secret_word:
                if char not in unique_letters_in_secretword:
                    unique_letters_in_secretword += char
            total_score = surplus_guess_count + 4 * len(unique_letters_in_secretword) + 3 * len(secret_word)
            print(f'Congratulations, you won!')
            print(f'Your total score for this game is: {total_score}')
            return None

        else:
            print(f'You have {surplus_guess_count} guesses left.')
            print(f'Available letters: {get_available_letters(letters_guessed)}')
            char = input('Please guess a letter: ')
            char = char.lower()

            # case 1: char is invalid: count -0
            if (not char.isalpha()) or (char.isalpha() and len(char) != 1):
                print(f'Oops! That is not a valid letter. Please input a letter from the alphabet: {get_word_progress(secret_word, letters_guessed)}')
                continue

            # case 2: char have already been guessed: count -0
            elif char in letters_guessed:
                print(f'Oops! You\'ve already guessed that letter: {get_word_progress(secret_word, letters_guessed)}')
                continue

            # case 3: char not in word and char is vowel: count -2, add the guess to letters_guessed
            elif (char not in secret_word) and (char in 'aeiou'):
                letters_guessed.append(char)
                surplus_guess_count -= 2
                print(f'Oops! That letter is not in my word: {get_word_progress(secret_word, letters_guessed)}')
                continue

            # case 4: char not in word and char is consonant: count -1, add the guess to letters_guessed
            elif (char not in secret_word) and (char not in 'aeiou'):
                letters_guessed.append(char)
                surplus_guess_count -= 1
                print(f'Oops! That letter is not in my word: {get_word_progress(secret_word, letters_guessed)}')
                continue

            # case 5: char in word, count -0, add the guess to letters_guessed
            else:
                letters_guessed.append(char)
                print(f'Good guess: {get_word_progress(secret_word, letters_guessed)}')
                continue

    while with_help:
        print(f'--------------')
        if surplus_guess_count <= 0:
            print(f'Sorry, you ran out of guesses. The word was {secret_word}.')
            return None

        elif has_player_won(secret_word, letters_guessed):
            unique_letters_in_secretword = ''
            for char in secret_word:
                if char not in unique_letters_in_secretword:
                    unique_letters_in_secretword += char
            total_score = surplus_guess_count + 4 * len(unique_letters_in_secretword) + 3 * len(secret_word)
            print(f'Congratulations, you won!')
            print(f'Your total score for this game is: {total_score}')
            return None

        else:
            print(f'You have {surplus_guess_count} guesses left.')
            print(f'Available letters: {get_available_letters(letters_guessed)}')
            char = input('Please guess a letter: ')
            char = char.lower()

            # case 0: char is !: check if surplus count >= 3, get_help, count -3, add the guess to letters_guessed
            if char == '!':
                if surplus_guess_count < 3:
                    print(f'Oops! Not enough guesses left: {get_word_progress(secret_word, letters_guessed)}')
                    continue
                else:
                    surplus_guess_count -= 3
                    help_char = get_help(secret_word, get_available_letters(letters_guessed))
                    letters_guessed.append(help_char)
                    print(f'Letter revealed: {help_char}')
                    print(f'{get_word_progress(secret_word, letters_guessed)}')
                    continue

            # case 1: char is invalid: count -0
            elif (not char.isalpha()) or (char.isalpha() and len(char) != 1):
                print(f'Oops! That is not a valid letter. Please input a letter from the alphabet: {get_word_progress(secret_word, letters_guessed)}')
                continue

            # case 2: char have already been guessed: count -0
            elif char in letters_guessed:
                print(f'Oops! You\'ve already guessed that letter: {get_word_progress(secret_word, letters_guessed)}')
                continue

            # case 3: char not in word and char is vowel: count -2, add the guess to letters_guessed
            elif (char not in secret_word) and (char in 'aeiou'):
                letters_guessed.append(char)
                surplus_guess_count -= 2
                print(f'Oops! That letter is not in my word: {get_word_progress(secret_word, letters_guessed)}')
                continue

            # case 4: char not in word and char is consonant: count -1, add the guess to letters_guessed
            elif (char not in secret_word) and (char not in 'aeiou'):
                letters_guessed.append(char)
                surplus_guess_count -= 1
                print(f'Oops! That letter is not in my word: {get_word_progress(secret_word, letters_guessed)}')
                continue

            # case 5: char in word, count -0, add the guess to letters_guessed
            else:
                letters_guessed.append(char)
                print(f'Good guess: {get_word_progress(secret_word, letters_guessed)}')
                continue

    #pass



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    secret_word = choose_word(wordlist)
    with_help = False
    hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
    pass

