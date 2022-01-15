import random 
import time

print("\nWelcome to Guess the nummber.")
print('''
Rules:
1. Guess a number between 1-100.
2. You get 7 chances
3. 'Hot' means you are within 5 of the number.
4. 'Warm' means you are within 10 of the number.
5. 'Cold' means you are within 20 of the number.''')
number = random.randint(1,100)

chances = 6

while chances > 0:
    guess = int(input("\nGuess: "))
    
    if guess == number:
        print("\nCORRECT GUESS!")
        print("YOU WIN!!")
        time.sleep(2)
        input("\n[PRESS ENTER TO QUIT] ")
        break
        
    elif guess != number:
        chances -= 1

        prox = abs(number-guess)

        if prox in range(0,6):
            print('[HOT]')

        elif prox in range(6,11):
            print('[WARM]')

        elif prox in range(11,21):
            print('[COLD]')

        print(f"{chances} Guesses left.")
        continue

        
if chances == 0:
    print("\nYOU LOOSE.")
    print(f"THE NUMBER WAS: {number}")
    time.sleep(2)
    input("\n[PRESS ENTER TO QUIT] ")
