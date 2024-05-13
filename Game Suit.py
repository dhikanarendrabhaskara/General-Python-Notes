###################################### TRADITIONAL SUIT GAME ##################################
def Game():
    '''
    Pick a number:
    1 = BATU
    2 = GUNTING
    3 = KERTAS

    Rules of the game:
    BATU > GUNTING
    GUNTING > KERTAS
    KERTAS > BATU
    '''

    import random
    myPoints = 0
    computerPoints = 0 
    gamePoints = 3 # number of accumulated points to win
    play = True
    name = input("\nHello there, what's your name ? ").upper()
    print(f"Alright {name}, let's play the traditional suit game!")

    while play:

        # computer's random input
        list1 = [1,2,3]
        Computer = random.choices(list1)
        inputComputer = ""
        for i in Computer:
            inputComputer += str(i)
            inputComputer = int(inputComputer)
        inputGame = int(input("\nChoose your input number (1-BATU, 2-GUNTING, 3-KERTAS): "))
        
        # the rules of the game
        if inputGame == 1:
            print("Your move: BATU")
        elif inputGame == 2:
            print("Your move: GUNTING")
        elif inputGame == 3:
            print("Your move: KERTAS")
        if inputComputer == 1:
            print("Computer's move: BATU")
        elif inputComputer == 2:
            print("Computer's move: GUNTING")
        elif inputComputer == 3:
            print("Computer's move: KERTAS")

        if inputGame == 1 and inputComputer == 2:
            print("YOU WIN")
            myPoints += 1
        elif inputGame == 2 and inputComputer == 3:
            print("YOU WIN")
            myPoints += 1
        elif inputGame == 3 and inputComputer == 1:
            print("YOU WIN")
            myPoints += 1
        elif inputGame == inputComputer:
            print("IT'S A DRAW")
        else:
            print("YOU LOSE")
            computerPoints += 1

        # the score
        print(f"SCORE: You-{myPoints} and Computer-{computerPoints}")
        if myPoints == gamePoints:
            play = False
            print(f"\nCONGRATULATIONS, {name}! YOU'VE WON THE GAME")
        elif computerPoints == gamePoints:
            play = False
            print(f"\nI'M SORRY, {name}. YOU'VE LOST THE GAME")

Game()



