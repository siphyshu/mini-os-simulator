#Implementation of Two Player Tic-Tac-Toe game in Python.

''' We will make the board using dictionary 
    in which keys will be the location(i.e : top-left,mid-right,etc.)
    and initialliy it's values will be empty space and then after every move 
    we will change the value according to player's choice of move. '''

from os import system
import time

theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []

for key in theBoard:
    board_keys.append(key)

''' We will have to print the updated board after every move in the game and 
    thus we will make a function in which we'll define the printBoard function
    so that we can easily print the board everytime by calling this function. '''

def printBoard(board):
    system('cls')

    print(f" {board['7']} | {board['8']} | {board['9']} ")
    print('___|___|___')
    print(f" {board['4']} | {board['5']} | {board['6']} ")
    print('___|___|___')
    print(f" {board['1']} | {board['2']} | {board['3']} ")
    print("   |   |   ")

# Now we'll write the main function which has all the gameplay functionality.
def game():

    turn = 'X'
    count = 0


    for _ in range(9):
        printBoard(theBoard)
        print(f"\nIt's {turn}'s turn.\nMove to which place? " , end="")

        move = input()        

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("\nThat place is already filled.", end="")
            time.sleep(2)
            continue

        # Now we will check if player X or O has won,for every move after 5 moves. 
        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # across the top
                printBoard(theBoard)
                print("\n[Game Over.]\n")                
                print("+=+=+| {" + turn + "} WON. |+=+=+=+")                
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # across the middle
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print("+=+=+| {" + turn + "} WON. |+=+=+=+")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the bottom
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print("+=+=+| {" + turn + "} WON. |+=+=+=+")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print("+=+=+| {" + turn + "} WON. |+=+=+=+")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the middle
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print("+=+=+| {" + turn + "} WON. |+=+=+=+")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # down the right side
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print("+=+=+| {" + turn + "} WON. |+=+=+=+")
                break 
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print("+=+=+| {" + turn + "} WON. |+=+=+=+")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print("+=+=+| {" + turn + "} WON. |+=+=+=+")
                break 

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            printBoard(theBoard)
            print("\nGame Over.\n")                
            print("+=+=+| It's a Tie!! |+=+=+")

        # Now we have to change the player after every move.
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    # Now we will ask if player wants to restart the game or not.
    restart = input("\nDo want to play Again? (Y/N) ")
    if restart == "y" or restart == "Y":  
        for key in board_keys:
            theBoard[key] = " "

        time.sleep(2)
        system('cls')
        game()

    else:
        print("\n[EXITING]")
        time.sleep(2)

if __name__ == "__main__":
    game()