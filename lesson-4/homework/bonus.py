import random

def get_winner(player, computer):
    if player == computer:
        return "Tie"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "Player"
    else:
        return "Computer"

def main():
    choices = ["rock", "paper", "scissors"]
    player_score = 0
    computer_score = 0
    
    while player_score < 5 and computer_score < 5:
        player_choice = input("Enter rock, paper, or scissors: ").lower()
        if player_choice not in choices:
            print("Invalid choice. Try again.")
            continue
        
        computer_choice = random.choice(choices)
        print(f"Computer chose {computer_choice}")
        
        winner = get_winner(player_choice, computer_choice)
        if winner == "Player":
            player_score += 1
            print("You win this round!")
        elif winner == "Computer":
            computer_score += 1
            print("Computer wins this round!")
        else:
            print("It's a tie!")
        
        print(f"Score -> Player: {player_score}, Computer: {computer_score}\n")
    
    if player_score == 5:
        print("Congratulations! You win the match!")
    else:
        print("Computer wins the match. Better luck next time!")

if __name__ == "__main__":
    main()