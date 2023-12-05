import random

difficulty = (0.9, 0.5, 0.1)
options = ("rock", "paper", "scissors")
running = True



while running:
    player = None
    computer = random.random()

    player_difficulty = None
    while player_difficulty not in difficulty:
        choice = input("Chooses a difficulty: (easy, normal, hard): ").lower()
        if choice == "easy":
            player_difficulty = .9
        elif choice == "normal":
            player_difficulty = .5
        elif choice == "hard":
            player_difficulty = .1

    while player not in options:
        player = input("Choose a choice! (rock, paper, scissors): ").lower()

    print(computer)

    player_wins = True if player_difficulty > computer else False
    computer_answer = None
    if player == "rock":
        computer_answer = "scissors" if player_wins else "paper"
    elif player == "paper":
        computer_answer = "rock" if player_wins else "scissors"
    else:
        computer_answer = "paper" if player_wins else "rock"

    print()
    print(f"Player: {player}")
    print(f"Computer: {computer_answer}")
    print()
    if player_wins:
        print("You win!")
    else:
        print("You lost!")

    if not input("Want to play again? (y/n): ").lower() == "y":
        running = False

print("Thanks for playing!")