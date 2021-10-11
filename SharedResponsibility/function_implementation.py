import random

OPTIONS = ['rock', 'paper', 'scissors']


def print_options():
    print('(1) Rock, (2) Paper, (3) Scissors')


def get_human_choice():
    return OPTIONS[int(input('Input a number: ')) - 1]


def get_computer_choice():
    return random.choice(OPTIONS)


def print_choices(human_choice: str, computer_choice: str):
    print(f'Your choice {human_choice}')
    print(f'Computer choice is {computer_choice}')


def print_result(human_choice: str, computer_choice: str):
    if human_choice == computer_choice:
        print('Draw!')
        return

    match human_choice:
        case 'rock':
            win_lose(human_choice, computer_choice, 'scissors', 'paper')
        case 'paper':
            win_lose(human_choice, computer_choice, 'rock', 'scissors')
        case 'scissors':
            win_lose(human_choice, computer_choice, 'paper', 'rock')


def win_lose(human_choice: str, computer_choice: str, win_to: str, lose_to: str):
    match computer_choice:
        case str(win_to):
            print(f'Yes, {human_choice} beat {computer_choice}!')
        case str(lose_to):
            print(f'Sorry, {computer_choice} beat {human_choice}')


def run_rsp_game():
    print_options()
    human_choice = get_human_choice()
    computer_choice = get_computer_choice()
    print_choices(human_choice, computer_choice)
    print_result(human_choice, computer_choice)


run_rsp_game()
