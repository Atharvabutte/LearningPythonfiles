import random

class NumberGuessingGame:
    def __init__(self):
        self.print_welcome_message()

    def print_welcome_message(self):
        print("Welcome to the Number Guessing Game!")
        print("Please enter a range to generate the random number.")

    def get_user_range(self):
        while True:
            try:
                start = int(input("Enter the lower limit: "))
                end = int(input("Enter the upper limit: "))
                if start < end:
                    return start, end
                else:
                    print("The lower limit should be smaller than the upper limit.")
            except ValueError:
                print("Please enter valid numbers.")

    def get_user_guess(self):
        while True:
            try:
                guess = int(input("Enter your guess: "))
                if guess < self.start or guess > self.end:
                    print(f"Please enter a number between {self.start} and {self.end}.")
                else:
                    return guess
            except ValueError:
                print("Please enter a valid number.")

    def play(self):
        self.start, self.end = self.get_user_range()
        secret_number = random.randint(self.start, self.end)
        attempts = 0

        while True:
            user_guess = self.get_user_guess()
            attempts += 1

            if user_guess == secret_number:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
            elif user_guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")

if __name__ == "__main__":
    game = NumberGuessingGame()
    game.play()
