import random

def play_game():
    number = random.randint(1, 100)
    attempts = 10
    
    while attempts > 0:
        try:
            guess = int(input("Enter your guess (1-100): "))
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if guess > number:
            print("Too high!")
        elif guess < number:
            print("Too low!")
        else:
            print("You guessed it right!")
            return
        
        attempts -= 1
        print(f"Attempts left: {attempts}")
    
    print("You lost. Want to play again?")
    restart = input("(Y/YES/y/yes/ok to restart): ").strip().lower()
    if restart in ['y', 'yes', 'ok']:
        play_game()

def main():
    print("Welcome to the Number Guessing Game!")
    play_game()

if __name__ == "__main__":
    main()