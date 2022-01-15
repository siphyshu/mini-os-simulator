import time
import random
from os import system

def start():
    global started 
    started = True
    counter = 0

    for _ in range(5):

        system('cls')
        print("[WELCOME TO SHITTY CAR SIMULATOR]")
        print("[ENTER COMMANDS TO OPERATE YOUR CAR]")
        print("[start, stop or leave]")
        print("\n[CAR STARTED]")
        car = [r"          ______", r"    _-_- /|_||_\`.__", r"_-_-__  (   _    _ _\ ", r"-_ _-_- =`-(_)--(_)-'"]
        space = "       "
        print(space*counter + car[0])
        print(space*counter + car[1])
        print(space*counter + car[2])
        print(space*counter + car[3])
        counter += 1
        time.sleep(0.5)


def stop():
    global started 
    started = False
    counter = 4
    for _ in range(5):

        system('cls')
        print("[WELCOME TO SHITTY CAR SIMULATOR]")
        print("[ENTER COMMANDS TO OPERATE YOUR CAR]")
        print("[start, stop or leave]")
        print("\n[CAR STOPPING]")
        car = [r"          ______", r"    _-_- /|_||_\`.__", r"_-_-__  (   _    _ _\ ", r"-_ _-_- =`-(_)--(_)-'"]
        space = "       "
        print(space*counter + car[0])
        print(space*counter + car[1])
        print(space*counter + car[2])
        print(space*counter + car[3])
        counter -= 1
        time.sleep(0.3)

    else:
        system('cls')
        print("[WELCOME TO SHITTY CAR SIMULATOR]")
        print("[ENTER COMMANDS TO OPERATE YOUR CAR]")
        print("[start, stop or leave]")
        print("\n[CAR STOPPED]")
        print(r'''  ______
 /|_||_\`.__
(   _    _ _\
=`-(_)--(_)-' ''')


def main():
    started = None
    while True:
        system('cls')
        print("[WELCOME TO SHITTY CAR SIMULATOR]")
        print("[ENTER COMMANDS TO OPERATE YOUR CAR]")
        print("[start, stop or leave]")

        if started == True:
            start()

        elif started == False:
            stop()

        else:
            print(r'''
  ______
 /|_||_\`.__
(   _    _ _\
=`-(_)--(_)-' ''')
            

        command = input("\nENTER: ")
        if command.upper() == 'START':
            if started == False or started == None:
                started = True 

            else:
                print("\n[CAR ALREADY STARTED]")
                time.sleep(2)

        elif command.upper() == 'STOP':
            if started == False or started == None:
                print("\n[CAR ALREADY STOPPED]")
                started = None
                time.sleep(2)

            else:
                started = False

        else:
            pass


if __name__ == "__main__":
    main()