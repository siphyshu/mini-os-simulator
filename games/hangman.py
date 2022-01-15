import time
import random
import math
from os import system

def restart():
    restart = input('''
        Do you wanna play again?
        (YES / NO): ''').lower()

    if restart == 'yes':
        
        time.sleep(2)
        system('cls')
        main()

    else:
        print('\n[EXITING]')
        time.sleep(2)
        exit()


def main():

    words = ['sit', 'stand', 'chair', 'table', 'school', 'hangman', 'home', 'paper', 'box', 'jump', 'run', 'pencil', 'playing', 'phone', 'friends', 'car', 'cheese']
    secret_word = random.choice(words)

    if len(secret_word) == 4:
        turns = 9

    elif len(secret_word) == 5:
        turns = 10    
    
    elif len(secret_word) == 6:
        turns = 12

    elif len(secret_word) == 7:
        turns = 13
    
    player = input("Player's name: ")

    print(f"Greetings {player},\nIts time to play Hangman!")
    print(f"\nYou have {turns} Guesses.")

    time.sleep(1)

    check = ''

    while turns > 0:
        
        failed = 0

        for char in secret_word:
            
            if char in check:
                print(char, end="")

            else:
                print('_', end="")
                failed += 1

        if failed == 0:
            print("\n[YOU WON]")
            
            time.sleep(2)

            restart()
            

        guess = input('''\n[Start Guessing]: ''')

        if len(guess) == 1:
            
            check += guess
            
            if guess not in secret_word:         
                print('''[Wrong]''')
                turns -= 1
                print(f"\n[{turns} Guesses left]")

                if turns == 0:
                    
                    print('''\n[GAME OVER]\n[YOU LOOSE]''')

                    print(f"\nThe secret word was {secret_word}.")

                    time.sleep(2)
                    
                    restart()

        else:
            
            print('''\n[NO CHEATING!]''')

            if turns == 0:
                
                print('''\n[GAME OVER]\n[YOU LOOSE]''')

                print(f"\nThe secret word was {secret_word}.")

                time.sleep(2)
                
                restart()

main()