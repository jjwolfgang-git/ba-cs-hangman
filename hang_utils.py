# We will keep all of our helper functions in this file

def createWordStruct(w):
    
    rv = []
    for l in w:
        td = { "letter": l, "found": False }
        rv.append(td)
    return rv
    
# Display the info at the beginning of each turn
def displayInfo(num_guesses, wordList, incorrect_guesses):
    
    print(f"You have {num_guesses} incorrect guesses remaining")
    print(formWordString(wordList))
    print(f"Incorrect letters guessed: {formIncorrectString(incorrect_guesses)}")
    
# Create the string of guessed and not guess letters
def formWordString(wl):
    rv = ""
    for ld in wl:
        if ld['found']:
            rv = rv + ld['letter'] + " "
        else:
            rv = rv + "_" + " "
    return rv
    

# Create a string of all the incorrect guesses
def formIncorrectString(incGuess):
    rv = ""
    # Loop through every letter in the list and form a single string
    for l in incGuess:
        rv = rv + l + " "
    return rv
  
# Ask the user for a guess and make sure it has not already been guessed    
def getUserGuess(incGuess, correctGuess):
    # Set a boolean to False
    valid = False
    
    # Loop until the boolean is no longer False
    while not valid:
        # Keep asking for a letter until we get a valid guess
        guess = input("Guess a letter: ")
        guess = guess.upper()[0]
        # Call isGuessValid() 
        valid = isGuessValid(guess, incGuess, correctGuess)
    return guess

# Validate that the letter guessed has not already been guessed
def isGuessValid(guess, incGuess, correctGuess):
    # Convert to upper case
    g = guess.upper()
    
    # Make sure the guess is a letter
    if g < "A" or g > "Z":
        return False
    
    # Make sure the letter is not in the incorrect letter list
    if g in incGuess or g in correctGuess:
        print("That letter has already been guessed")
        return False
    
    return True

# Determine if the letter is found in the word
# If so, update the dictionary(ies) of the word
# Return the number of times that letter is found in the word
def analyzeGuess(g, wl):
    # Keep track of how many matches we find
    count = 0
    # Loop through each letter in the wl dictionary and check if
    # the letter matches our guess
    for ld in wl:
        if g == ld['letter']:
            ld['found'] = True
            count += 1
    return count

def isWordFound(wl):
    # Determine if any letters are NOT found yet
    for ld in wl:
        if ld['found'] == False:
            return False
    
    # If we get through the loop, all letters were found
    return True


if __name__ == "__main__":
    
    ws = createWordStruct("TEST")
    print("All blanks")
    print(formWordString(ws))
    ws[0]['found'] = True
    ws[3]['found'] = True
    print(formWordString(ws))
    print("Incorrect Guesses of A, B, C")
    print(formIncorrectString(["A","B","C"]))
    print("Display Info: ")
    displayInfo(4, ws, ["A","B","C"])
    
    assert isGuessValid("g", ["A","B","C"], ["T"]) == True, "isGuessValid True Failed"
    assert isGuessValid("g", ["A","B","C"], ["G"]) == False, "isGuessValid False/Correct Failed"
    assert isGuessValid("g", ["A","B","G"], ["T"]) == False, "isGuessValid False/Incorrect Failed"

    print("User Guess: A, B, G, T are invalid guesses")
    ug = getUserGuess(["A","B","G"], ["T"])
    
    assert analyzeGuess("E", ws) == 1, "analyzeGuess E failed"
    assert analyzeGuess("T", ws) == 2, "analyzeGuess T failed"
    assert analyzeGuess("J", ws) == 0, "analyzeGuess J failed"
    
    print("==> Unit Test Suite Complete")
    
    
