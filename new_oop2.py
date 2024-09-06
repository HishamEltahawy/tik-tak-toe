class Player():
    def __init__(self, name, symbol) -> None:
        self.name = ''
        self.symbol = ''
    def choose_name(self):
        while True:
            choice = input('Type Your Name:')
            if choice.isalpha():
                self.name = choice
                break
            else:
                print("Invalid Entry Try Again")
    def choose_symbol(self):
        while True:
            choice = input('Typer Your Symbol:').upper()
            if len(choice) == 1 and choice.isdigit():
                self.symbol = choice
                break
            else:
                print("Invalid Choice Just Single Letter")
        
class Board():  
    def __init__(self) -> None:
        self.board = [str(i) for i in range (1, 10)]

    def show_board(self):
        for i in range(0, 9, 3):
            print("|".join(self.board[i:i+3]))

    def update_board(self, symbol, choice):
        if self.is_valid_choice(choice):
            self.board[choice-1] = symbol
            return True
        else:
            print("<< You can't play here >>")
            return False        

    def is_valid_choice(self, choice):
        return self.board[choice-1].isdigit()
    
    def reset_game(self):
        self.board = [str(i) for i in range (1, 10)]

class Menu():
    def displayer_main_menu(self):
        while True:
            choice = input('''
>>>>> Welcome in tek-tak-toe Game >>>>>
              1- Start Game
              2- Quit Game
''')
            if choice.isdegit() and len(choice) == 1 :
                break
            else:
                print("Invalid choice...")
        return choice
    def displayer_end_menu(self):
        while True:
            choice = input('''
>>>>> Game Over >>>>>
    1- Restart Game
    2- Quit Game
''')           
            if choice.isdegit() and len(choice) == 1 :
                break
            else:
                print("Invalid choice...")
        return choice

class Game():
    def __init__(self) -> None:
        self.player = [Player(), Player()]
        self.board = Board()
        self.menu = Menu()
        self.player_round = 0
    def start_game(self):
        pass
    def setup_players(self):
        pass
    def play_game(self):
        pass
    def play_turn(self):
        pass
    def switch_player(self):
        pass
    def check_win(self):
        pass
    def check_draw(self):
        pass
    def restart_game(self):
        pass
    def quit_game(self):
        pass



