import random

OPTIONS = ['rock', 'paper', 'scissors']


class RPSGame:
    def __init__(self):
        self.human_choice = None
        self.computer_choice = None

    def print_options(self):
        print('(1) Rock, (2) Paper, (3) Scissors')

    def get_human_choice(self):
        self.human_choice = OPTIONS[int(input('Input a number: ')) - 1]

    def get_computer_choice(self):
        self.computer_choice = random.choice(OPTIONS)

    def print_choices(self):
        print(f'Your choice {self.human_choice}')
        print(f'Computer choice is {self.computer_choice}')

    def print_result(self):
        if self.human_choice == self.computer_choice:
            print('Draw!')
            return

        match self.human_choice:
            case 'rock':
                self.win_lose('scissors', 'paper')
            case 'paper':
                self.win_lose('rock', 'scissors')
            case 'scissors':
                self.win_lose('paper', 'rock')

    def win_lose(self, win_to: str, lose_to: str):
        match self.computer_choice:
            case str(win_to):
                print(f'Yes, {self.human_choice} beat {self.computer_choice}!')
            case str(lose_to):
                print(f'Sorry, {self.computer_choice} beat {self.human_choice}')

    def run_rsp_game(self):
        self.print_options()
        self.get_human_choice()
        self.get_computer_choice()
        self.print_choices()
        self.print_result()


game = RPSGame()
game.run_rsp_game()
