import random


def choose_word():
    words = ["elephant", "pythonic", "hangman", "developer", "challenge"]
    return random.choice(words)


def display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)


def hangman():
    secret_word = choose_word()
    guessed_letters = set()
    incorrect_attempts = 0
    max_attempts = 6

    print("Welcome to Hangman!")

    while incorrect_attempts < max_attempts:
        current_display = display_word(secret_word, guessed_letters)
        print(f"\nWord: {current_display}")
        print(f"Incorrect attempts left: {max_attempts - incorrect_attempts}")
        print()

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.add(guess)

        if guess not in secret_word:
            incorrect_attempts += 1
            print("Incorrect guess. Try again.")
        else:
            print("Good guess!")

        if all(letter in guessed_letters for letter in secret_word):
            print(f"\nCongratulations! You guessed the word: {secret_word}")
            break

    if incorrect_attempts == max_attempts:
        print(f"\nSorry, you ran out of attempts. The word was: {secret_word}")


if __name__ == "__main__":
    hangman()
