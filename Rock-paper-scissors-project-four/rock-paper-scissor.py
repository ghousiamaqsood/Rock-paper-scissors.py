import random

def play_rock_paper_scissors():
    """Plays a game of Rock-Paper-Scissors with the user."""

    choices = ["rock", "paper", "scissors"]
    user_choice = input("Choose rock, paper, or scissors: ").lower()

    # Strange mode: Randomly change the user's choice
    if random.randint(0, 2) == 0:
        user_choice = random.choice(choices)
        print(f"Strange mode activated! Your choice has been changed to {user_choice}.")

    computer_choice = random.choice(choices)
    print(f"The computer chose {computer_choice}.")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")

# Play the game
play_rock_paper_scissors()