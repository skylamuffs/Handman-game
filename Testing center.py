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

# Game Rules function
def display_rules(name):
    print(f"\nHello, {name}, nice to meet you! Welcome to Hangman!!!!!!!!!!")
    
    print("\n" + "="*50)
    print("Here are the game rules:")
    print("1. There will be 10 guesses")
    print("2. You'll guess one letter at a time")
    print("3. Each incorrect guess brings you closer to losing")
    print("4. Guess the word before you run out of attempts!")
    print("="*50)

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

def play_game(name):
    # Select a random word from the wordlist
    secret_word = random.choice(wordlist).upper()
    word_length = len(secret_word)
    
    # Guesses
    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = 10
    correctly_guessed = ['_'] * word_length
    
    print(f"\nAlright {name}, I've chosen a word!")
    print(f"The word has {word_length} letters.")
    
    # Main game loop
    while incorrect_guesses < max_attempts and '_' in correctly_guessed:
        # Display current hangman stage
        print(hangman_stages[incorrect_guesses])
        
        # Display current word progress
        print("Word:", " ".join(correctly_guessed))
        
        # Show guessed letters
        if guessed_letters:
            print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        
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
            if guess in guessed_letters:
                print(f"You've already guessed '{guess}'! Try a different letter.")
                continue
            break
        
        # Add to guessed letters
        guessed_letters.append(guess)
        
        # Check if the letter is in the secret word
        if guess in secret_word:
            print(f"Good guess! '{guess}' is in the word!")
            
            # Update the correctly guessed letters
            for i in range(word_length):
                if secret_word[i] == guess:
                    correctly_guessed[i] = guess
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            incorrect_guesses += 1
            print(f"Incorrect guesses remaining: {max_attempts - incorrect_guesses}")
        
        print("-" * 50)
    
    # Game over - check result
    if '_' not in correctly_guessed:
        print("\n" + "="*50)
        print(f"CONGRATULATIONS {name}! 🎉🎉🎉")
        print(f"You guessed the word: {secret_word}")
        print(f"With {max_attempts - incorrect_guesses} guesses remaining!")
        print("="*50)
    else:
        print(hangman_stages[incorrect_guesses])
        print("\n" + "="*50)
        print(f"GAME OVER {name}! 💀")
        print(f"The word was: {secret_word}")
        print("Better luck next time!")
        print("="*50)
    
    # Ask if player wants to play again
    while True:
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again in ['yes', 'y']:
            return True
        elif play_again in ['no', 'n']:
            return False
        else:
            print("Please enter 'yes' or 'no'.")

# Main program
def main():
    name = get_player_name()
    display_rules(name)
    
    keep_playing = True
    while keep_playing:
        keep_playing = play_game(name)
    
    print(f"\nThanks for playing Hangman, {name}! Goodbye! 👋")

# Run the game
if __name__ == "__main__":
    main()