import random
import time


def welcome_screen():

    hangmanLogo = """

| |  | |                                         | |
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __   | |
|  __  |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\  | |
| |  | | (_| | | | | (_| | | | | | | (_| | | | | |_|
|_|  |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_| (_)
                     __/ |
                    |___/
 """
    print(hangmanLogo)


class HangmanGame:

    def __init__(self):
        """
        Initialise the game class.
        """
        self.restart()

    def restart(self):
        """
        Resets all game states.
        """
        self.hidden_player = self.chosen_player()
        self.guessed_letters = []
        self.incorrect_guesses = 0
        self.max_guesses = 6
        self.play_game()

    def chosen_player(self):
        """
        Chooses a random footballer from the list for the user to guess.
        """
        footballers = ['messi', 'ronaldo', 'kane', 'haaland', 'mbappe',
                       'lewandowski', 'bellingham', 'neymar', 'son', 'foden',
                       'kroos', 'benzema', 'modric', 'salah', 'rashford',
                       'neuer', 'rooney', 'gerrard', 'lampard', 'maradona']
        return random.choice(footballers)

    def display_player(self):
        """
        Checks what letters have been guessed and displays if correct.
        """
        display = ""
        for letter in self.hidden_player:
            if letter in self.guessed_letters:
                display += letter
            else:
                display += "_"
        return display

    def hangman_picture(self):
        """
        Hangman pictures as they progeess depending on answers.
        """
        if self.incorrect_guesses == 0:
            print("  ________      ")
            print("  |      |      ")
            print("  |             ")
            print("  |             ")
            print("  |             ")
            print("*_| _*          ")
        elif self.incorrect_guesses == 1:
            print("  ________      ")
            print("  |      |      ")
            print("  |      0      ")
            print("  |             ")
            print("  |             ")
            print("*_| _*          ")
        elif self.incorrect_guesses == 2:
            print("  ________      ")
            print("  |      |      ")
            print("  |      0      ")
            print("  |     /       ")
            print("  |             ")
            print("*_| _*          ")
        elif self.incorrect_guesses == 3:
            print("  ________      ")
            print("  |      |      ")
            print("  |      0      ")
            print("  |     /|      ")
            print("  |             ")
            print("*_| _*          ")
        elif self.incorrect_guesses == 4:
            print("  ________      ")
            print("  |      |      ")
            print("  |      0      ")
            print("  |     /|\\    ")
            print("  |             ")
            print("*_| _*          ")
        elif self.incorrect_guesses == 5:
            print("  ________      ")
            print("  |      |      ")
            print("  |      0      ")
            print("  |     /|\\    ")
            print("  |     /       ")
            print("*_| _*          ")
        else:
            print("  ________      ")
            print("  |      |      ")
            print("  |      0      ")
            print("  |     /|\\    ")
            print("  |     / \\    ")
            print("*_| _*          ")

    def play_game(self):
        """
        Start of Footballers Hangman and allows user to start guessing letters.
        """
        name = input("Hi there, whats your name?")
        welcome = (f"Welcome to Footballers Hangman {name}!"
                   " \nEnter a letter and try to guess the footballer "
                   "before you run out of guesses!"
                   " \nYou have 6 tries to guess the footballer, "
                   "do you think you can do it?")

        for char in welcome:
            print(char, end='', flush=True)
            time.sleep(.05)
        while self.incorrect_guesses < self.max_guesses:
            current_display = self.display_player()
            print(f"\nFootballer: {current_display}")
            self.hangman_picture()
            guess = input("Please guess a letter:").lower()
            if len(guess) != 1 or not guess.isalpha():
                print("Enter a valid letter (A single lowercase letter)")
                continue
            if guess in self.guessed_letters:
                print("You have already tried that letter, try another.")
                continue
            self.guessed_letters.append(guess)
            if guess not in self.hidden_player:
                self.incorrect_guesses += 1
                print(f"Unlucky thats not one of the letters! "
                      f"You have {self.max_guesses - self.incorrect_guesses}"
                      f" guesses left!")
            else:
                print("Thats correct!")

            if all(letter in self.guessed_letters
                    for letter in self.hidden_player):
                print(f"Well done! You guessed the player"
                      f" {self.hidden_player}. And what a player ay!")
                play_again()
                break

        if self.incorrect_guesses == self.max_guesses:
            self.hangman_picture()
            print(f"Ahh unlucky {name}, you have run out of guesses!"
                  f"The player I was thinking of was... {self.hidden_player}. "
                  f"Better luck next time!")
            play_again()


def play_again():
    answer = input(str("Do you want to play again? (y/n):"))
    if answer == 'y':
        main()
    elif answer == 'n':
        print(f"No worries, thanks for playing!")
        quit()
    else:
        print("Please enter Y or N")
        play_again()


def main():
    welcome_screen()
    play_the_game = HangmanGame()
    play_the_game.play_game()


main()
