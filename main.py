import csv
import random
import time
import sys
import base64
import os
import subprocess
from getpass import getpass


def main():
    while True:
        welcome()
        ask_user = input(
            "\nLogin(L) or Create Account(C) [Q to quit]: ").upper()

        if ask_user == 'C':
            time.sleep(0.2)
            clear()
            print("\n[CREATING NEW ACCOUNT]")
            create_account()

        elif ask_user == 'L':
            time.sleep(0.1)
            clear()
            print("\n[LOGGING IN]")
            login()

        elif ask_user == 'Q':
            print("\nExiting...")
            loading()
            clear()
            time.sleep(0.2)
            exit()

        else:

            print('\n[Enter L, C, Q.]')

    input()



def welcome():
    print(r'''
             ,----------------,              ,---------,
        ,-----------------------,          ,"        ,"|
      ,"                      ,"|        ,"        ,"  |
     +-----------------------+  |      ,"        ,"    |
     |  .-----------------.  |  |     +---------+      |
     |  |                 |  |  |     | -==----'|      |
     |  |  OS Simulator   |  |  |     |         |      |
     |  |  Bad command or |  |  |/----|`---=    |      |
     |  |  C:\>passwd()   |  |  |   ,/|==== ooo |      ;
     |  |                 |  |  |  // |(((( [33]|    ,"
     |  `-----------------'  |," .;'| |((((     |  ,"
     +-----------------------+  ;;  | |         |,"
        /_)______________(_/  //'   | +---------+
   ___________________________/___  `,
  /  oooooooooooooooo  .o.  oooo /,   \,"-----------
 / ==ooooooooooooooo==.o.  ooo= //   ,`\--{)B     ,"
/_==__==========__==_ooo__ooo=_/'   /___________,"
`-----------------------------'
''', end="")


def create_account():
    while True:
        newusername = input("\nEnter a Username: ")
        if username_not_available(newusername) == True:
            print('[ALERT: Username Already Exists]')

        else:
            break

    while True:
        newpassword = input("\nEnter a New Password: ")
        # print(password_strength(newpassword))
        confm_password = input("Confirm Password: ")

        # if confm_password == "":
        #     continue

        if newpassword == confm_password:
            newpassword = pwd_encrypt(newpassword)
            break

        elif newpassword != confm_password:
            print("[ALERT: Passwords do not match!]")

    first_name = input("\nFirst Name: ")
    last_name = input("Last Name: ")
    age = input('Age (in num): ')

    email_address = input("Email Address: ")
    phone_no = input("Phone Number: ")

    backup_key = input(
        "\nWhat is the name of your first friend?\n[ALERT: This will be used as a backup key incase you forget your password] ").upper()
    backup_key = pwd_encrypt(backup_key)

    with open('database.csv', 'a+', newline='') as newuseradd:
        fieldnames = ['username', 'password', 'firstname',
                      'lastname', 'age', 'email', 'phone', 'backupkey']
        new_user_writer = csv.DictWriter(newuseradd, fieldnames=fieldnames)
        new_user_writer.writerow({'username': newusername, 'password': newpassword, 'firstname': first_name,
                                  'lastname': last_name, 'age': age, 'email': email_address, 'phone': phone_no, 'backupkey': backup_key})
        print("\nCongrats new account created!")
        time.sleep(1)
        clear()
        newuseradd.close()


def account_details(account):

    with open('database.csv', 'r') as accountreader:
        reader = csv.DictReader(accountreader)

        for x in list(reader):
            if x['username'] == account:
                name = x['firstname'] + ' ' + x['lastname']
                age = x['age']
                email = x['email']
                phone = x['phone']
                # password = x['password']
                break

    print(f"\n[MY PROFILE]")

    print(f'\nUsername: {account}')
    print(f'Password: ********')

    print(f"\nName: {name}")
    print(f"Age: {age}")
    print(f"Email Account: {email}")
    print(f"Phone Number: {phone}")

    print("\nPress Enter to go back to menu.")

    input()
    clear()


def login():

    with open('database.csv', 'r') as userlogin:
        login_reader = csv.DictReader(userlogin)
        username1 = input("\nUsername: ")

        for row in list(login_reader):
            if row['username'] == username1:
                print("[User Found]")

            else:
                continue

            attempts = 0

            while attempts <= 2:
                password1 = getpass("\nPassword: ********** ")
                password1 = pwd_encrypt(password1)

                if row['password'] == password1:
                    print("[Access Granted]")
                    loading()
                    clear()
                    print(f'\nWelcome to your account!')
                    login_session(username1)
                    break

                else:
                    if attempts == 2:
                        print("[Incorrect Password]")
                        attempts += 1
                        loading()

                    else:
                        print("[Try Again]")
                        attempts += 1
                        # print(f"Attempt {attempts}")

            else:
                clear()
                ask = input(
                    "\nForgot Password?(F) or Create New Account?(C): ").upper()

                if ask == 'F':
                    print("\n[Forgot Password]")
                    if forgotpassword(username1):
                        print("[Access Granted]")
                        loading()
                        clear()
                        print(f'\nWelcome to your account!')
                        login_session(username1)

                    else:
                        print("\nSorry, Try again after some time.")

                elif ask == 'C':
                    time.sleep(0.2)
                    clear()
                    print("\n[CREATING NEW ACCOUNT]")
                    create_account()

                else:
                    time.sleep(0.2)
                    print("[Exiting]")
                    clear()

        else:
            time.sleep(0.5)
            clear()



def login_session(user):
    while True:
        print(f"\n[{user.upper()}'s account.]")
        ask = input('''
        Choose from menu and enter number.
        
        1. See Account Details
        2. Change Password
        3. Open your Notepad
        4. Open Calculator
        5. Play Games
        6. Watch Movies
        7. Play Songs
        0. Log out

        Enter:  ''')

        if ask == '1':
            print(f"\nFetching {user}'s account details.")
            loading()
            clear()
            account_details(user)

        elif ask == '2':
            loading()
            clear()
            print("\n")
            print("[Error 404: Page not found.] " * 3)
            print("\nSorry for the inconvenience.")

            input("\nPress enter to go back to menu.\n")
            clear()
            # change_password(user)

        elif ask == '3':
            print(f"\nOpening {user}'s notepad.")
            loading()
            clear()
            notepad(user)
            input("\nPress enter to go back to menu.\n")
            clear()

        elif ask == '4':
            print("\nOpening Calculator.")
            loading()
            clear()
            os.system('calculator.py')
            input("\nPress enter to go back to menu.\n")

        elif ask == '5':
            print("\nLoading Games Section.")
            loading()
            clear()
            games()
            clear()

        elif ask == '6':
            print("\nLoading Movie Centre.")
            loading()
            clear()
            movies()
            clear()

        elif ask == '7':
            print("\nLoading Song Space.")
            loading()
            clear()
            songs()
            clear()

        elif ask == '0':
            print("\nLogging Out.")
            loading()
            clear()
            break
        else:
            clear()


def pwd_encrypt(pwd):
    bytesstr = pwd.encode("UTF-8")
    encodedstr = base64.a85encode(bytesstr)
    a85str = encodedstr.decode("UTF-8")
    rvrsdstr = a85str[::-1]
    finalstr = ""

    i = 0
    for char in rvrsdstr:
        if (i % 2 == 0):
            i += 1
            pass

        else:
            finalstr += char
            i += 1

    return finalstr


def forgotpassword(username):
    with open("database.csv", 'r') as account:
        reader = csv.DictReader(account)

        for row in list(reader):
            if row['username'] == username:
                ask_backupkey = input(
                    "\nWhat is the name of your first friend? ").upper()
                ask_backupkey = pwd_encrypt(ask_backupkey)

                if row['backupkey'] == ask_backupkey:
                    return True

                else:
                    return False


def username_not_available(username):
    with open('database.csv', 'r') as users:
        user_reader = csv.DictReader(users)
        for row in list(user_reader):
            if row['username'] == username:
                return True

            else:
                return False


def notepad(account):
    padname = f"{account}'s_notepad.txt"
    with open(padname, 'a+') as pad:
        pad.close()

    os.system(padname)


def games():
    while True:
        clear()
        print("\nWelcome to Games Arcade.")
        gamelist = []
        basepath = os.getcwd() + "\\games\\"

        for entry in os.listdir(basepath):
            gamelist.append(entry)

        numofgames = len(gamelist)

        if numofgames == 0:
            print("\n[No Games Available]\n[Add to play]")
            input("\nPress Enter to go back to home.")
            break

        else:
            print("\n        Choose a game from menu and enter number.\n")

            for i in range(0, numofgames):
                print(f"        {i+1}. {gamelist[i]}")

            print("        0. Go Back to Home Page.")

            choice = input("\n      Enter: ")

            if int(choice) in range(1, numofgames+1):
                print(f"\nOpening {gamelist[int(choice)-1]}.")
                loading()
                clear()
                gamepath = basepath + gamelist[int(choice)-1]
                subprocess.Popen(['start', "", gamepath], shell=True)
                input("\nPress Enter to go back to game menu. ")

            elif choice == '0':
                clear()
                break

            else:
                clear()


def movies():
    while True:
        clear()
        print("\n        Choose a movie from menu and enter number.\n")
        movielist = []
        basepath = os.getcwd() + "\\movies\\"

        for entry in os.listdir(basepath):
            movielist.append(entry)

        numofmovies = len(movielist)

        if numofmovies == 0:
            print("\n[No Movies Available]\n[Add to watch]")
            input("\nPress Enter to go back to home.")
            break

        else:
            print("\nWelcome to Movie Centre.")
            for i in range(0, numofmovies):
                print(f"        {i+1}. {movielist[i]}")

            print("        0. Go Back to Home Page.")

            choice = input("\n      Enter: ")

            if int(choice) in range(1, numofmovies+1):
                print(f"\nPlaying {movielist[int(choice)-1]}.")
                loading()
                clear()
                moviepath = basepath + movielist[int(choice)-1]
                print(f"Currently Playing {movielist[int(choice)-1]}")
                subprocess.Popen(['start', "", moviepath], shell=True)
                input("\nPress Enter to go back to movie centre. ")

            elif choice == '0':
                clear()
                break

            else:
                clear()

def songs():
    while True:
        clear()
        print("\n        Choose a Song from menu and enter number.\n")
        songlist = []
        basepath = os.getcwd() + "\\songs\\"

        for entry in os.listdir(basepath):
            songlist.append(entry)

        numofsongs = len(songlist)

        if numofsongs == 0:
            print("\n[No Songs Available]\n[Add to listen]")
            input("\nPress Enter to go back to home.")
            break

        else:
            print("\nWelcome to Song Space.")

            for i in range(0, numofsongs):
                print(f"        {i+1}. {songlist[i]}")

            print("        0. Go Back to Home Page.")

            choice = input("\n      Enter: ")

            if int(choice) in range(1, numofsongs+1):
                clear()
                songpath = basepath + songlist[int(choice)-1]
                print(f"Currently Playing {songlist[int(choice)-1]}")
                subprocess.Popen(['start', "", songpath], shell=True)

            elif choice == '0':
                clear()
                break

            else:
                clear()



def clear():
    _ = os.system('cls')


def loading():
    print("\n[", end="")

    for _ in range(0, 25):
        x = random.choice([0.05, 0.07, 0.1, 0.2, ])
        time.sleep(x)
        print("█", end="", flush=True)

    print("]")



if __name__ == "__main__":
    main()



# def password_strength(pwd):
#     alpha = 0
#     num = 0
#     spc_char = 0
#     upper = False
#     lower = False

#     for char in pwd:
#         if char in 'abcdefghijklmnopqrstuvwxyz':
#             alpha += 1
#             if char.isupper():
#                 upper = True

#             elif char.islower():
#                 lower = True

#         elif char in '123456789':
#             num += 1

#         else:
#             spc_char += 1

#     if alpha >= 8 and num >= 4 and spc_char >= 1 and (upper == True or lower == True):
#         return '[STRONG PASSWORD] [Confirm Password or Press Enter to choose new password]'

#     elif (8 > alpha >= 5) and (1 < num <= 4) and (spc_char == 0):
#         return '[GOOD PASSWORD] [Confirm Password or Press Enter to choose new password]'

#     else:
#         return '[WEAK PASSWORD] [Confirm Password or Press Enter to choose new password]'


# def games():
    # while True:
    #     clear()

    #     print("\nWelcome to Games Bar.")
    #     game = input('''
    #     Choose a game from menu and enter number.

    #     1. Guess the Number
    #     2. Hangman
    #     3. Tic-Tac-Toe
    #     4. Dungeon Adventure
    #     5. Car Simulator
    #     0. Go Back to Home Page

    #     Enter: ''')

    #     if game == '1':
    #         print("\nOpening Guess the Number Game.")
    #         loading()
    #         clear()
    #         os.system('guessthenumber.py')
    #         input("Press enter to go back to game menu. ")

    #     elif game == '2':
    #         print("\nOpening Hangman.")
    #         loading()
    #         clear()
    #         os.system('hangman.py')

    #     elif game == '3':
    #         print("\nOpening Tic Tac Toe.")
    #         loading()
    #         clear()
    #         os.system('tictactoe.py')

    #     elif game == '4':
    #         print("\nOpening Dungeon Adventure.")
    #         loading()
    #         clear()
    #         os.system('tinytextadventure.py')

    #     elif game == '5':
    #         print("\nOpening Car Simulator.")
    #         loading()
    #         clear()
    #         os.system('carsimulator.py')

    #     elif game == '0':
    #         clear()
    #         break

    #     else:
    #         clear()


# def change_password(username):

#     with open('database.csv', 'a+') as change_pwd:
#         fieldnames = ['username', 'password','firstname','lastname','age','email']
#         change_pwd_reader = csv.DictReader(change_pwd)
#         change_pwd_writer = csv.DictWriter(change_pwd, fieldnames=fieldnames)

#         for row in list(change_pwd_reader):
#             if row['username'] == username:

#             #     while True:
#             #         print("Enter details below correctly.")
#             #         oldpassword = input("\nEnter Old Password: ")

#             #         if row['password'] == oldpassword:

#             #             while True:
#             #                 newpassword = input("\nEnter New Password: ")
#             #                 pwd_confm = input("Confirm Password: ")

#             #                 if newpassword == pwd_confm:
#             #                     replaced = row['password'].replace(oldpassword, newpassword)
#             #                     row['password'] = replaced
#             #                     change_pwd_writer.writerow(row)
#             #                     break

#             #                 else:
#             #                     print("\n[Passwords don't match]")
#             #                     time.sleep(0.5)

#             #             break


#             #         else:
#             #             print("\n[Paswword Incorrect]")
#             #             time.sleep(0.5)

#             # else:
#             #     print("FAIL")

#                 oldpassword = input("\nEnter Old Password: ")

#                 newpassword = input("\nEnter New Password: ")
#                 pwd_confm = input("Confirm Password: ")

#                 if newpassword == pwd_confm:
#                     replaced = row['password'].replace(row['password'], newpassword)
#                     row['password'] = replaced
#                     change_pwd_writer.writerow(row)
