# hangman.py
# This is our main program file for the Hangman activity
import random
from hang_words import wordList
from hang_utils import createWordStruct, displayInfo, getUserGuess, analyzeGuess, isWordFound 

# Initial Setup
num_guesses = 8
word = ""
incorrect = []
correct = []
wordGuessed = False

# Choose our word
wordSet = set(wordList)
word = wordSet.pop()
print(word)

wordStruct = createWordStruct(word)
print(wordStruct)

print("Welcome - Let's Play Hangman!")
print("Take your first turn:")

while num_guesses > 0 and not wordGuessed:
    displayInfo(num_guesses, wordStruct, incorrect)
    g = getUserGuess(incorrect, correct)
    num_letters = analyzeGuess(g, wordStruct)
    if num_letters == 0:
        # Guessed Letter NOT found in the word
        incorrect.append(g)
        num_guesses = num_guesses - 1
        print(f"Sorry {g} is not in the word. Try again.")
    else:
        # Guessed Letter is found at least once in the word
        correct.append(g)
        print(f"{num_letters} {g} in the word!")
        
        if isWordFound(wordStruct):
            wordGuessed = True
            print("That’s Correct – You WIN!")
            print(f"You had {num_guesses-1} incorrect guesses remaining")

    print()

if not wordGuessed:
    print(f"Sorry, you lose. The word was {word}. Please play again! ")
    
