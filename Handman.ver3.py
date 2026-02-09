import random

#import files into the game
with open('Wordlist.txt', 'r') as file:
    wordlist = [line.strip() for line in file]
    
#asking player's details
name = input("What is your name? ")
print("Hello,", name, "nice to meet you! Welcome to Hangman!!!!!!!!!!")

print("\n" + "="*50)
print("Here are the game rules:")
print("1. I'll choose a random word for you to guess")
print("2. You'll guess one letter at a time")
print("3. Each incorrect guess brings you closer to losing")
print("4. Guess the word before you run out of attempts!")
print("="*50)

# Select a random word from the wordlist
secret_word = random.choice(wordlist).upper()
word_length = len(secret_word)


# Game variables
guessed_letters = []
incorrect_guesses = 0
max_attempts = 6
correctly_guessed = ['_'] * word_length


print(f"\nAlright {name}, I've chosen a word!")
print(f"The word has {word_length} letters.")
print(f"You have {max_attempts} attempts to guess the word.\n")


# Hangman stages (visual representation)
hangman_stages = [
    """
       ------
    """,
    """
       ------
            |
            |
            |
            |
            |
    """,
    """
       ------
            |
            |
            |
            |
            |
    ==========
    """,
    """
       ------
       |    |
            |
            |
            |
            |
    ==========
    """,
    """
       ------
       |    |
       O    |
            |
            |
            |
    ==========
    """,
    """
       ------
       |    |
       O    |
       |    |
            |
            |
    ==========
    """,
    """
       ------
       |    |
       O    |
      /|    |
            |
            |
    ==========
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
            |
            |
    ==========
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
      /     |
            |
    ==========
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
      / \\   |
            |
    ==========
    """
]
