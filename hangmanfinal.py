import string
def iswordguessed(secretword, lettersguessed):
    for i in secretword:
        if i not in lettersguessed:
            return False
    return True
def getguessedstring(secretword, lettersguessed):
    underscore=["_" for i in range(len(secretword))]
    for i in range(len(secretword)):
        if secretword[i] in lettersguessed:
            underscore[i]=secretword[i]
    string1=""
    for i in underscore:
        string1=string1+i+" "
    return string1
def availableletters(lettersguessed):
    availableletters1=string.ascii_lowercase
    for i in lettersguessed:
        availableletters1=availableletters1.replace(i, "")
    return availableletters1

import random
WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
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
    print("  ", len(wordlist), "words loaded.")
    return wordlist
def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)
wordlist=loadWords()
secretword=chooseWord(wordlist)
lettersguessed=[]
guesses=8
def hangman(secretword):
    print("Welcom to Hangman")
    print("I am thinking of a word that is", len(secretword), "letters long")
    print("----------")
    while True:
        global guesses
        print("You have", guesses, "guesses left")
        print("Available letters: ", availableletters(lettersguessed))
        guess=input("Please guess a letter: ")
        guesses=guesses-1
        if guess not in lettersguessed:
            lettersguessed.append(guess)
        else:
            print("You have already guessed this letter")
            guesses=guesses+1
            continue
        if guess in secretword:
            print("Good guess: ", getguessedstring(secretword, lettersguessed))
            print("----------")
            guesses=guesses+1
        else:
            print("Oops that letter is not in my word", getguessedstring(secretword, lettersguessed))
            print("----------")
        if iswordguessed(secretword, lettersguessed):
            print("Congratulations, the word indeed was", secretword )
            break
        if guesses==0:
            print("You ran out of guesses, the word was", secretword)
            break
hangman(secretword)
        
            
        
        
        
    
    