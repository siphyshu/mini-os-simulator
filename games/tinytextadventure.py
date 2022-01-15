import time
import random

# game function
def game():

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Welcome to the cavern of secrets!")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    time.sleep(3)

    print("You enter a dark cavern out of curiosity. It is dark and you can only make out a small stick on the floor.")
    ch1 = str(input("Do you take it? [y/n]: "))

    # STICK TAKEN
    if ch1 in ['y', 'Y', 'Yes', 'YES', 'yes']:
        print("You have taken the stick!")
        time.sleep(2)
        stick = 1

    # STICK NOT TAKEN
    else:
        print("You did not take the stick")
        stick = 0

    print("As you proceed further into the cave, you see a small glowing object")
    ch2 = str(input("Do you approach the object? [y/n]"))

    # APPROACH SPIDER
    if ch2 in ['y', 'Y', 'Yes', 'YES', 'yes']:
        print("You approach the object...")
        time.sleep(2)
        print("As you draw closer, you begin to make out the object as an eye!")
        time.sleep(1)
        print("The eye belongs to a giant spider!")
        ch3 = str(input("Do you try to fight it? [Y/N]"))

        # FIGHT SPIDER
        if ch3 in ['y', 'Y', 'Yes', 'YES', 'yes']:

            # WITH STICK
            if stick == 1:
                print("You only have a stick to fight with!")
                print("You quickly jab the spider in it's eye and gain an advantage")
                time.sleep(2)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("                  Fighting...                   ")
                print("   YOU MUST HIT ABOVE A 5 TO KILL THE SPIDER    ")
                print("IF THE SPIDER HITS HIGHER THAN YOU, YOU WILL DIE")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                time.sleep(2)
                fdmg1 = int(random.randint(3, 10))
                edmg1 = int(random.randint(1, 5))
                print("you hit a", fdmg1)
                print("the spider hits a", edmg1)
                time.sleep(2)

                if edmg1 > fdmg1:
                    print("The spider has dealt more damage than you!")
                    complete = 0
                    return complete

                elif fdmg1 < 5:
                    print("You didn't do enough damage to kill the spider, but you manage to escape")
                    complete = 1
                    return complete

                else:
                    print("You killed the spider!")
                    complete = 1
                    return complete

            # WITHOUT STICK
            else:
                print("You don't have anything to fight with!")
                time.sleep(2)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("                  Fighting...                   ")
                print("   YOU MUST HIT ABOVE A 5 TO KILL THE SPIDER    ")
                print("IF THE SPIDER HITS HIGHER THAN YOU, YOU WILL DIE")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                time.sleep(2)
                fdmg1 = int(random.randint(1, 8))
                edmg1 = int(random.randint(1, 5))
                print("you hit a", fdmg1)
                print("the spider hits a", edmg1)
                time.sleep(2)

                if edmg1 > fdmg1:
                    print("The spider has dealt more damage than you!")
                    complete = 0
                    return complete

                elif fdmg1 < 5:
                    print("You didn't do enough damage to kill the spider, but you manage to escape")
                    complete = 1
                    return complete

                else:
                    print("You killed the spider!")
                    complete = 1
                    return complete
        
        #DON'T FIGHT SPIDER
        else:
            print("You choose not to fight the spider.")
            time.sleep(1)
            print("As you turn away, it ambushes you and impales you with it's fangs!!!")
            complete = 0
            return complete

    # DON'T APPROACH SPIDER
    else:
            print("You turn away from the glowing object, and attempt to leave the cave...")
            time.sleep(1)
            print("But something won't let you....")
            time.sleep(2)
            complete = 0
            return complete

# Game Loop
alive = True
while alive:

    complete = game()
    if complete == 1:
        alive = input('You managed to escape the cavern alive! Would you like to play again? [y/n]: ')
        if alive in ['y', 'Y', 'YES', 'yes', 'Yes']:
            alive

        else:
            break

    else:
        alive = input('You have died! Would you like to play again? [y/n]: ')
        if alive in ['y', 'Y', 'YES', 'yes', 'Yes']:
            alive

        else:
            break