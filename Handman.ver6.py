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

# Main game function
def play_game(name):
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
                print("Please enter a valid letter!")
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
            wrong_guesses += 1
            print(f"Incorrect guesses remaining: {max_attempts - wrong_guesses}")
        
        print("-" * 50)
    
    # Game over - check result
    print(hangman_stages[wrong_guesses])
    
    if '_' not in correctly_guessed:
        # Player won
        print(f"CONGRATULATIONS {name.upper()}!!! ")
        print(f"You guessed the word: {secret_word}")
        print(f"With {wrong_guesses} wrong guesses and {max_attempts - wrong_guesses} guesses remaining!")
    else:
        # Player lost
        print(f"SORRY {name}, YOU LOST! ")
        print(f"The word was: {secret_word}")
        print(f"You guessed: {' '.join(correctly_guessed)}")
        print("Better luck next time!")

# Main program
print("=" * 60)
print("WELCOME TO HANGMAN GAME!")
print("=" * 60)

# Get player name once at the beginning
name = get_player_name()
print(f"\nHello, {name}, nice to meet you! Welcome to Hangman!!!!!!!!!!")

# Game Rules (show only once)
print("\n" + "="*50)
print("Here are the game rules:")
print("1. There will be 10 guesses")
print("2. You'll guess one letter at a time")
print("3. Each incorrect guess brings you closer to losing")
print("4. Guess the word before you run out of attempts!")
print("="*50)

# Main game loop
play_more = True
while play_more:
    play_game(name)
    
    # Ask if player wants to play again
    while True:
        play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()
        if play_again in ['yes', 'y', 'no', 'n']:
            play_more = play_again in ['yes', 'y']
            break
        else:
            print("Please enter 'yes' or 'no'.")
    
    if play_more:
        print("\n" + "=" * 60)
        print(f"GREAT! GET READY FOR THE NEXT ROUND, {name.upper()}!")
        print("=" * 60)

print("\n" + "=" * 60)
print(f"THANKS FOR PLAYING HANGMAN, {name.upper()}! GOODBYE!")
print("=" * 60)