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
        



