import random

def get_user_choice():
    user_choice = input("Enter 'snake', 'water', or 'gun': ").lower()
    while user_choice not in ['snake', 'water', 'gun']:
        print("Invalid choice!. Please enter 'snake', 'water', or 'gun'.")
        user_choice = input("Enter 'snake', 'water', or 'gun': ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(['snake', 'water', 'gun'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == 'snake':
        return "You win!" if computer_choice == 'water' else "You lose!"
    elif user_choice == 'water':
        return "You win!" if computer_choice == 'gun' else "You lose!"
    elif user_choice == 'gun':
        return "You win!" if computer_choice == 'snake' else "You lose!"

def main():
    print("Welcome to Snake-Water-Gun Game!")
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYour choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        play_again = input("Do you want to play again? (Y/N): ").lower()
        if play_again != 'Y'.lower():
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    main()

    