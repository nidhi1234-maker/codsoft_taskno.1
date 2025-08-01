import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def get_user_choice():
    while True:
        choice = input("\nChoose Rock, Paper, or Scissors: ").strip().lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        print("❌ Invalid input. Please enter rock, paper, or scissors.")

def determine_winner(user, computer):
    if user == computer:
        return 'tie'
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return 'user'
    else:
        return 'computer'

def play_game():
    print("🎮 Welcome to Rock, Paper, Scissors!")
    user_score = 0
    computer_score = 0
    round_num = 1

    while True:
        print(f"\n--- Round {round_num} ---")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose: {user_choice.capitalize()}")
        print(f"Computer chose: {computer_choice.capitalize()}")

        winner = determine_winner(user_choice, computer_choice)

        if winner == 'tie':
            print("🤝 It's a tie!")
        elif winner == 'user':
            print("✅ You win this round!")
            user_score += 1
        else:
            print("❌ Computer wins this round.")
            computer_score += 1

        print(f"🏆 Score -> You: {user_score} | Computer: {computer_score}")

        play_again = input("\nDo you want to play another round? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("\n🎉 Final Score:")
            print(f"You: {user_score} | Computer: {computer_score}")
            print("👋 Thanks for playing!")
            break

        round_num += 1

# Run the game
play_game()
