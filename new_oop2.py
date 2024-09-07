import os

def clearScreen():
    os.system("cls")

class Player():
    def __init__(self) -> None:
        self.name = ''
        self.symbol = ''
    def choose_name(self):
        while True:
            choice = input('Type Your Name:').title()
            if choice.isalpha():
                self.name = choice
                break
            else:
                print("Invalid Entry Try Again")
    def choose_symbol(self):
        while True:
            choice = input('Typer Your Symbol:').upper()
            if len(choice) == 1 and choice.isdigit() == False:
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
            if choice.isdecimal() == True and len(choice) == 1 :
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
            if choice.isdigit() and len(choice) == 1 :
                break
            else:
                print("Invalid choice...")
        return choice

class Game():
    def __init__(self) :
        self.player = [Player(), Player()]
        self.board = Board()
        self.menu = Menu()
        self.player_round = 1
        self.winner = "No One Wins"
    def start_game(self):
        choice = self.menu.displayer_main_menu()
        if choice == "1":
            self.setup_players()
            self.play_game()
        else:
            print("Quiting Game.....")
    def setup_players(self):
        for counter, players in enumerate(self.player, start=1):
            print(f"Player {counter} Enter your details >>>")
            players.choose_name()
            players.choose_symbol()
            clearScreen()
    def play_game(self):
            while True:
                clearScreen()
                self.play_turn()
                if self.check_win() or self.check_draw():
                    if self.check_win() == True:
                        self.board.show_board()
                        if  self.winner == self.player[0].symbol:
                            print(f"The Winner Is >>>>> {self.player[0].name} <<<<<") 
                        else:
                            print(f"The Winner Is >>>>> {self.player[1].name} <<<<<")  
                        choice = self.menu.displayer_end_menu()
                        if choice == "1":
                            self.restart_game()
                        else:
                            self.quit_game()
                            break
                    elif self.check_draw() == True:
                        self.board.show_board()
                        print(f">>>>> {self.winner} <<<<<")
                        choice = self.menu.displayer_end_menu()
                        if choice == "1":
                            self.restart_game()
                        else:
                            self.quit_game()
                            break                       
    def play_turn(self):
        self.switch_player()
        player = self.player[self.player_round]
        self.board.show_board()
        print(f"{player.name}'s turn ({player.symbol})")
        while True:
            try:
                cell_choice = int(input("choose a cell (1-9)"))
                if  1 <= cell_choice <= 9 and self.board.update_board(choice=cell_choice, symbol=player.symbol):
                    break
                else:
                    print("invalid choice try again")
            except ValueError:
                print("please enter a number between (1-9)")

    def switch_player(self):
        self.player_round = 1- self.player_round
    def check_win(self):      
        win_combination = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8]
        ,[0, 3, 6], [1, 4, 7], [2, 5, 8]
        ,[0, 4, 8], [2, 4, 6]  ]
        for combo in win_combination:
            if self.board.board[combo[0]]  == self.board.board[combo[1]] == self.board.board[combo[2]]:
                self.winner = self.board.board[combo[0]]
                return True

    def check_draw(self):
        for cell in self.board.board:
            if cell.isdigit():
                return False
    def restart_game(self):
        self.board.reset_game()
        self.player_round = 1
        self.winner = "No One Wins"
        self.play_game()
    def quit_game(self):
        print("Quiting Game.....")


root = Game().start_game()
