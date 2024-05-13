################################## HANGMAN GAME ##################################

import random
guessWord = []
letterStorage = []
alphabet = "abcdefghijklmnopqrstu"
wordList = ['toothbrush','refrigerator','television','thermometer','trashbin','treadmill',
            'smartphone','hairdryer','calculator','sofabed','toothpaste']
secretWord = random.choice(wordList)
lengthWord = len(secretWord)
name = input("What's your name? ")
print("Hello " + name + ", time to play hangman!\n")

def opening():
    for i in secretWord:
        guessWord.append("-")
    print(f"Ok, the word you need has {lengthWord} characters & it can be found in your house")
    print(guessWord)

def game():
    opening()
    guessCount = 5 # number of guessing chances
    while guessCount > 0:
        guess = input("Pick a letter: ").lower()
        if guess in letterStorage:
            guessCount -= 1 
            print("\nYou've already guessed that letter!") 
            print(f"You have {guessCount} chance(s) left")
            if guessCount == 0:
                print("TOUGH LUCK, YOU'RE DEAD!")
                break 
        else:
            letterStorage.append(guess)
            if guess in secretWord:
                print("\nYou guessed correctly!")
                for x in range(0,lengthWord):
                    if secretWord[x] == guess:
                        guessWord[x] = guess
                        print(guessWord)
                if '-' not in guessWord:
                    print("CONGRATULATIONS, YOU WON!")
                    break       
            else:
                guessCount -= 1
                print("\nThe letter is not in the word")
                print(f"You have {guessCount} chance(s) left")
                if guessCount == 0:
                    print("TOUGH LUCK, YOU'RE DEAD!")
                    break

game()