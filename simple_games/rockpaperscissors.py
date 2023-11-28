import random


def home():
    print("     *** Rock, Paper and Scissors ***")
    print("--> Only for two players Either ")
    print("Select a choice:")
    print(" 1. Rock \n 2. Paper \n 3. Scissors")


def player_choice():
    global choice
    choice = input("Enter your choice in number: ")
    if choice == "1":
        print("You choose rock.")
    elif choice == "2":
        print("You choose paper")
    elif choice == "3":
        print("You choose scissors")
    else:
        print("Invalid Choice!!")
        exit()


def computer_choice():
    global comp_choice
    comp_choice = str(random.randint(1, 3))
    if comp_choice == "1":
        print("Computer choose rock.")
    elif comp_choice == "2":
        print("Computer choose paper")
    elif comp_choice == "3":
        print("Computer choose scissors")


def my_func():
    a = choice
    b = comp_choice
    if a == b:
        print("It's a draw.")
    if (a == "1" and b == "2") or (a == "2" and b == "3") or (a == "3" and b == "1"):
        print('Sorry! You Lost. Try again.')
    if (a == "2" and b == "1") or (a == "3" and b == "2") or (a == "1" and b == "3"):
        print('Congratulations! You Win.')


while True:
    home()
    print()
    player_choice()
    print()
    computer_choice()
    print()
    my_func()

    cont = input("Press 'y' if you want to play again: ")
    if cont.upper() != 'Y':
        break
