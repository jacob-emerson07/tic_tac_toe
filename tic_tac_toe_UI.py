import tic_tac_toe as ttt
import ttt_AI

RUNNING = True


def get_game_type():
    # Allows the user to choose between playing against another human player or an
    # AI that randomly chooses an empty space.

    game_type = input('What game type ["Human" or "AI"] would you like to play? ')

    if not ttt.validate_type(game_type):
        print("Invalid Game Type, please try again.")
        get_game_type()

    if game_type == "AI":
        while game_type != "Easy" and game_type != "Medium":
            print(game_type)
            game_type = input('What difficulty ["Easy" or "Medium"]? ')
        

    return game_type

def print_board():
    # Prints the game board.
    
    print("+---+---+---+")
    for row in ttt.BOARD:
        print("|", end=" ")
        print(*row, sep=" | ", end=" |\r\n")
        print("+---+---+---+")

def take_input():
    # Requests the user to input the row and column that they would like to place
    # their game piece. The function then checks whether or not the move is valid
    # using the private validating function, _validate_turn().
    
    is_valid = False
    while not is_valid:
        row = input(f"What row would you like to place? ")
        column = input("What column? ")
        
        if ttt.validate_turn(row,column):
            is_valid = True
            break
        print(f"Invalid choice, try again.")
        
    return int(row)-1, int(column)-1

def start():
    global RUNNING
    
    game_type = get_game_type()

    print_board()
    
    while RUNNING:
        
        if game_type == "Easy" and ttt.TURN == 2:
            print()
            coords = ttt_AI.easy_input(ttt.BOARD)

        elif game_type == "Medium" and ttt.TURN == 2:
            print()
            coords = ttt_AI.medium_input(ttt.BOARD)
            
        else:
            coords = take_input()

        ttt.add_piece(coords)

        victor = ttt.winner()
        
        print_board()

        if victor != None and victor != "DRAW":
            RUNNING = False
            print(victor, " is the winner!")
                  
        elif victor == "DRAW":
            RUNNING = False
            print(victor)

if __name__ == "__main__":
    start()
                  
