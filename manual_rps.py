import random


options=["Rock", "Paper", "Scissors"]

def get_computer_choice():
    return random.choice(options)

def get_user_choice():
    return input('pick your choice ').lower()


def  get_winner(computer_choice, user_choice):

    if get_user_choice == computer_choice:
        winner= print(f"Both players selected {user_choice}. It's a tie!")
    elif user_choice == "rock":
        if computer_choice == "scissors":
            winner= print("Rock smashes scissors! You win!")
        else:
            winner= print("Paper covers rock! You lose computer won.")
    elif user_choice == "paper":
        if computer_choice == "rock":
            winner= print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose computer won.")
    elif user_choice == "scissors":
        if computer_choice == "paper":
            winner=print("Scissors cuts paper! You win!")
        else:
            winner=print("Rock smashes scissors! You lose computer won.")
    return winner



def play():
    human_choice=get_user_choice()
    computer_choice=get_computer_choice()
    return get_winner(computer_choice, human_choice )


play()