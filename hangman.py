# Hangman game
import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    parameter: list of words (strings)
    ---------------------------------------------------------------------------
    Returns: a word from wordlist at random
    
    """
    
    return random.choice(wordlist)

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    parameter: secretWord: string, the word the user is guessing
               lettersGuessed: list, what letters have been guessed so far
    ---------------------------------------------------------------------------
    returns: True if all the letters of secretWord are in lettersGuessed;
             False otherwise
    '''
  
    for i in secretWord:
        if i not in lettersGuessed:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    parameter: secretWord: string, the word the user is guessing
               lettersGuessed: list, what letters have been guessed so far
    ---------------------------------------------------------------------------
    returns: string, comprised of letters and underscores that represents
             what letters in secretWord have been guessed so far.
    '''
   
    s=''
    for i in secretWord:
        if i in lettersGuessed:
            s+=i
        else:
            s+='_'
    return s


def getAvailableLetters(lettersGuessed):
    '''
    parameter: lettersGuessed: list, what letters have been guessed so far
    ---------------------------------------------------------------------------
    returns: string, comprised of letters that represents what letters have not
             yet been guessed.
    '''
   
    s='abcdefghijklmnopqrstuvwxyz'
    ans=''
    for i in s:
        if i not in lettersGuessed:
            ans+=i
    return ans
    

def hangman(secretWord):
    '''
    parameter: secretWord: string, the secret word to guess.
    ---------------------------------------------------------------------------
    prints: number of guesses, wheter or not it's a right guess, and if the word has been found

    '''
    
    print ("Welcome to the game, Hangman!")
    print ("I'm thinking of a word that is " + str(len(secretWord)) + " letters long.")
    lettersGuessed = ''
    guessesLeft = 8
    print ("------------")
    
    while True:
        print ("You have " + str(guessesLeft) + " guesses left.")
        print ("Available letters: " + getAvailableLetters(lettersGuessed))
        guess = input("Please guess a letter: ")
        if guess in secretWord and guess not in lettersGuessed:
            lettersGuessed += guess
            print ("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
        elif guess in lettersGuessed:
            print ("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed += guess
            print ("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
            guessesLeft -= 1
        print ("------------")
        if guessesLeft <= 0:
            print ("Sorry, You've ran out of guesses. The word was " + secretWord + ".")
            break
        if isWordGuessed(secretWord, lettersGuessed):
            print ("Congratulations! You've won!")
            break



secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
