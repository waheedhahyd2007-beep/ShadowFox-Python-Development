
import random

# Words and hints for the game
word_bank = {
    "python": "A popular programming language",
    "computer": "An electronic device used for computing",
    "keyboard": "Used to type on a computer",
    "developer": "A person who creates software",
    "algorithm": "A step-by-step method to solve a problem",
    "database": "An organized collection of data",
    "internet": "A worldwide network of computers",
    "variable": "Stores a value in programming",
    "function": "A reusable block of code",
    "programming": "The process of writing computer instructions"
}

# Hangman drawings for incorrect guesses
stages = [
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """
]


def play_hangman():
    word, hint = random.choice(list(word_bank.items()))

    guessed_letters = set()
    wrong_guesses = 0
    max_wrong_guesses = 6

    print("\n===== WELCOME TO HANGMAN =====")
    print("Hint:", hint)
    print("Guess the word one letter at a time!")

    while wrong_guesses < max_wrong_guesses:
        display_word = ""

        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("\nWord:", display_word)
        print("Incorrect guesses:",
              wrong_guesses, "/", max_wrong_guesses)
        print(stages[wrong_guesses])

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the word!")
            print("The word was:", word)
            return

        guess = input("Enter one letter: ").lower().strip()

        # Validate user input
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Enter only one letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Correct guess!")
        else:
            wrong_guesses += 1
            print("Wrong guess! Try again.")

    print(stages[wrong_guesses])
    print("\nGame over! You ran out of guesses.")
    print("The correct word was:", word)


# Start the game
while True:
    play_hangman()

    again = input("\nWould you like to play again? (yes/no): ")
    if again.lower().strip() != "yes":
        print("Thank you for playing Hangman!")
        break
