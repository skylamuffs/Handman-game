import random

# Import files into the game
with open('Wordlist.txt', 'r') as file:
    wordlist = [line.strip() for line in file]

# Function to validate player name
def get_player_name():
    while True:
        name = input("What is your name? ").strip()
        
        # Check if name contains only alphabetic characters and spaces
        if not name:
            print("Name cannot be empty! Please enter your name.")
            continue
        
        # Check if name contains any digits
        if any(char.isdigit() for char in name):
            print("Please enter a valid name without numbers! Try again.")
            continue
        
        # Check if name contains only letters and spaces
        if all(char.isalpha() or char.isspace() for char in name):
            return name
        else:
            print("Please enter a valid name using only letters and spaces! Try again.")

# Get player's name with validation
name = get_player_name()
print(f"Hello, {name}, nice to meet you! Welcome to Hangman!!!!!!!!!!")

# Game Rules
print("\n" + "="*50)
print("Here are the game rules:")
print("1. There will be 10 guesses")
print("2. You'll guess one letter at a time")
print("3. Each incorrect guess brings you closer to losing")
print("4. Guess the word before you run out of attempts!")
print("="*50)

# Select a random word from the wordlist
secret_word = random.choice(wordlist).upper()
length = len(secret_word)

# Guesses
letters = []
wrong_guesses = 0
max_attempts = 10
correctly_guessed = ['_'] * length

print(f"\nAlright {name}, I've chosen a word!")
print(f"The word has {length} letters.")


# Hangman stages (drawing the handman)
hangman_stages = [
   r"""

   """,
    r"""
       ------
    """,
    r"""
       ------
            |
            |
            |
            |
            |
    """,
    r"""
       ------
            |
            |
            |
            |
            |
    ==========
    """,
    r"""
       ------
       |    |
            |
            |
            |
            |
    ==========
    """,
    r"""
       ------
       |    |
       O    |
            |
            |
            |
    ==========
    """,
    r"""
       ------
       |    |
       O    |
       |    |
            |
            |
    ==========
    """,
    r"""
       ------
       |    |
       O    |
      /|    |
            |
            |
    ==========
    """,
    r"""
       ------
       |    |
       O    |
      /|\   |
            |
            |
    ==========
    """,
    r"""
       ------
       |    |
       O    |
      /|\   |
      /     |
            |
    ==========
    """,
    r"""
       ------
       |    |
       O    |
      /|\   |
      / \   |
            |
    ==========
    """
]

# Main game loop
while wrong_guesses < max_attempts and '_' in correctly_guessed:
    # Display current hangman stage
    print(hangman_stages[wrong_guesses])
    
    # Display current word progress
    print("Word:", " ".join(correctly_guessed))
    
    # Show guessed letters
    if letters:
        print(f"Guessed letters: {', '.join(sorted(letters))}")
    
    # Get player's guess
    while True:
        guess = input("\nGuess a letter: ").upper().strip()
        
        # Input validation
        if len(guess) != 1:
            print("Please enter only one letter!")
            continue
        if not guess.isalpha():
            print("Please enter a valid letter (A-Z)!")
            continue
        if guess in letters:
            print(f"You've already guessed '{guess}'! Try a different letter.")
            continue
        break
    
    # Add to guessed letters
    letters.append(guess)
    
    # Check if the letter is in the secret word
    if guess in secret_word:
        print(f"Good guess! '{guess}' is in the word!")
        
        # Update the correctly guessed letters
        for i in range(length):
            if secret_word[i] == guess:
                correctly_guessed[i] = guess
    else:
        print(f"Sorry, '{guess}' is not in the word.")
        incorrect_guesses += 1
        print(f"Incorrect guesses remaining: {max_attempts - wrong_guesses}")
    
    print("-" * 50)

