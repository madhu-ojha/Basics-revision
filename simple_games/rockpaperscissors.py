import random
choice = ""
comp_choice = ""


def home():
    print("     *** Rock, Paper and Scissors ***")
    print("--> Only for two players Either ")
    print("Select a choice:")
    print(" 1. Rock \n 2. Paper \n 3. Scissors")


def my_func():

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

    c_choice = random.randint(1, 3)
    if comp_choice == "1":
        print("Computer choose rock.")
    elif comp_choice == "2":
        print("Computer choose paper")
    elif comp_choice == "3":
        print("Computer choose scissors")
        exit()

    a = choice
    b = comp_choice
    if a == b:
        print("It's a draw.")
    if (a == 1 and b == 2) or (a == 2 and b == 3) or (a == 3 and b == 1):
        print('Sorry! You Lost. Try again.')
    if (a == 2 and b == 1) or (a == 3 and b == 2) or (a == 1 and b == 3):
        print('Congratulations! You Win.')


home()
while True:

    my_func()

    # cont = input("Press 'y' if you want to play again: ")
    # if cont.upper() != 'Y':
    #     break
