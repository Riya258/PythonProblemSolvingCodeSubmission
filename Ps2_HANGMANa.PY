# Problem Set 2
# Name: Riya
# Time Spent: 3:00hrs

import random
                       # library that we use in order to choose on random words from a list of words.
print("loading word list.......")

WORDLIST_FILENAME = "words.txt"


  #  print("Loading word list from file...")
    # inFile: file
inFile = open(WORDLIST_FILENAME,'r')
    # line: string
line = inFile.readline()
    # wordlist: list of strings
wordlist = line.split()
   # print("  ", len(wordlist), "words loaded.")
print("  ", len(wordlist),"loaded words.")
word=random.choice(wordlist)            # Function will choose one random word from this list of words.

# your code begins here!
name = input("Quel est ton nom? ") 
print("Bonjour ! ", name)                       # Here the user is asked to enter the name first.
print("Bonne chance....")                        #Good luck.
print("Bienvenue dans le jeu Pendu...")        #Welcome to the game Hangman.
print("Devinez les personnages")      #Guess the characters.
guesses = ''
print("I'm thinking of a word that",len(word),"character is long")
turns = len(word)*2              
while turns > 0:
     
                         # counts the number of times a user fails.
    failed = 0
     
                         # all characters from the input word taking one at a time.
    for char in word:
         
                                # comparing that character with the character in guesses
        if char in guesses:
            print(char)
             
        else:
            print("_")
             
                                 # for every failure 1 will be incremented in failure
            failed += 1
             
 
    if failed == 0:
                              # user will win the game if failure is 0 and 'You Win' will be given as output
        print("Vous Gagnez")
         
        # this print the correct word
        print("The word is: ", word)
        break
     
    # if user has input the wrong alphabet then it will ask user to enter another alphabet
    guess = input("Devinez les personnages:")
     
    # every input character will be stored in guesses
    guesses += guess
     
    # check input with the character in word
    if guess not in word:
         
        turns -= 1
         
        # if the character doesn’t match the word then “Wrong” will be given as output
        print("Tort")
         
        # this will print the number of turns left for the user
        print("You have", + turns, 'more guesses')
         
         
        if turns == 0:
            print("Vous perdez")