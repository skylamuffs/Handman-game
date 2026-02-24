from random import randint

def letters_and_dashes(word,guesses):
    # Print the guessed letters and unguessed dashes in the word
    for letter in word:
        if letter=="\n":
            break
        if letter in guesses:
            print(letter," ",end="")
        else:
            print("_ ",end="")
    print("\n")

def hangman(lines):
    # Draw the hangman according to the number of incorrect guesses
    print("You have",10-lines,"guesses left.")
    if lines==1:
        print(r"""

                         |
                         |
                         |
                         |
                         |
                         |
                         |                  """)
    elif lines==2:
        print(r"""

                         |
                         |
                         |
                         |
                         |
                         |
                      ___|___               """)
    elif lines==3:
        print(r"""
                          _______
                         |/
                         |
                         |
                         |
                         |
                         |
                      ___|___               """)
    elif lines==4:
        print(r"""
                          _______
                         |/
                         |     _
                         |    (_)
                         |
                         |
                         |
                      ___|___               """)
    elif lines==5:
        print(r"""
                          _______
                         |/
                         |     _
                         |    (_)
                         |     |
                         |     |
                         |
                      ___|___               """)
    elif lines==6:
        print(r"""
                          _______
                         |/
                         |     _
                         |    (_)
                         |     |
                         |     |
                         |    /
                      ___|___               """)
    elif lines==7:
        print(r"""
                          _______
                         |/
                         |     _
                         |    (_)
                         |     |
                         |     |
                         |    / \
                      ___|___               """)
    elif lines==8:
        print(r"""
                          _______
                         |/
                         |     _
                         |    (_)
                         |   --+
                         |     |
                         |    / \
                      ___|___               """)
    elif lines==9:
        print(r"""
                          _______
                         |/
                         |     _
                         |    (_)
                         |   --+--
                         |     |
                         |    / \
                      ___|___               """)


def print_used_letters(wrong):
    # Print the list of incorrect letters
    print("\n")
    print("Letters used:  ", end='')
    for wrong_letter in wrong:
        print(wrong_letter," ", end='')
    print("\n")


def get_word():
    # Get a random word from the word list file
    word_list=open("longWords.txt",'r')
    words=word_list.readlines()
    new_word=words[randint(1,len(words)-1)]
    word_list.close()
    return(new_word)

def letter_yes(correct_letter,correct_letters):
    # If the letter is correct, append the letter to the correct letters list and print a message.
    correct_letters.append(correct_letter)
    print(correct_letter,"is in the word.")
    return(correct_letters)

def letter_no(incorrect_letter,incorrect_letters):
    # If the letter is incorrect, append the letter to the incorrect letters list.
    incorrect_letters.append(incorrect_letter)
    return(incorrect_letters)

def fail(correct_word):
    # Print the fail message and the correct word
    print(r"""
                          ________
                         |/    |
                         |     |
                         |    (_)
                         |   --+--
                         |     |
                         |    / \
                      ___|___               """)
    print("You failed!")
    print("The word was",correct_word)

def success(correct_word):
    # Print the success message and the correct word
    print(r"""
                -
               ( \\
                ) )
               ( (  .-""-.  A.-.A
                \ \/      \\/ , , \\
                 \   \    =;  t  /=
                  \   |"".  ' --'
                   / //  | ||
                  /_,))  |_,))
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!""")
    
    print("Congratulations, the word is",correct_word)



guesses_left=10
correct_letter_list=[]
wrong_letter_list=[]
letter=""

word=get_word()
letters_left=len(word)-1

print("==================")
print("Welcome to Hangman")
print("==================")
print("\n")
print("I am thinking of a",letters_left,"letter word.")
letters_and_dashes(word,[])

# Main loop
while guesses_left>0 and letters_left!=0:
    # Valid input check
    letter=(input("Guess a letter: ")).lower()
    while (letter in wrong_letter_list) or (letter in correct_letter_list):
        letter=(input("Letter is already used. Guess another letter:\n")).lower()
    while not letter.isalpha():
        letter=input(("This is not a letter. Guess a letter:\n")).lower()
    
    if letter in word:
         letters_left=letters_left-word.count(letter)
         if letters_left==0: # Check if all the letters in the word have been found
             success(word)
         else:
             correct_letter_list=letter_yes(letter,correct_letter_list)
             letters_and_dashes(word,correct_letter_list)
    else:
         guesses_left=guesses_left-1
         wrong_letter_list=letter_no(letter,wrong_letter_list)
         hangman(10-guesses_left)
         print_used_letters(wrong_letter_list)

if guesses_left==0:
    fail(word)

