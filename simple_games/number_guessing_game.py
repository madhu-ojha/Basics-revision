import random


def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    secret_number = random.randint(1, 100)

    while True:
        guess = int(input("Guess the number (between 1 and 100): "))

        if guess == secret_number:
            print("Congratulations! You guessed the correct number.")
            break
        elif guess < secret_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")


if __name__ == "__main__":
    number_guessing_game()
