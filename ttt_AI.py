import tic_tac_toe as ttt

from random      import randint
from collections import defaultdict


def easy_input(board):
    # Takes the game board and finds how many empty spaces there are. The function
    # randomly chooses an empty spot to place their piece on and selects that
    # position.
    
    empty_spaces = sum(x.count(" ") for x in board)
    choice = randint(1, empty_spaces)
    count = 0
    for i in range(len(board)):
        for j in range(3):
            if board[i][j] == " ":
                count += 1
                if count == choice:
                    return i,j

def medium_input(board):
    # Takes the game board and finds out if there is a way for the opponent to win on
    # the next turn. If such a move exists, the function will choose the spot that
    # would prevent the loss. It will also check if there is a way for it to win, taking
    # priority over preventing a loss. If no condition exists, then the function will
    # choose a random spot with the easy_input function.

    # The point_of_interest variable stores the point that would block a losing condition,
    # starting with an initial condition of being an empty tuple.
    point_of_interest = tuple()

    # Checking each row.
    for row in range(len(board)):
        counts = defaultdict(int)

        for i in range(3):
            counts[board[row][i]] += 1

        for column in counts:
            if counts[column] == 2 and column != " ":
                if column == ttt.PLAYERS[ttt.TURN]:
                    if " " in counts.keys():
                        return row, board[row].index(" ")
                        
                elif column != ttt.PLAYERS[ttt.TURN] and column != " ":
                    if " " in counts.keys():
                        point_of_interest = (row, board[row].index(" "))

    # Checking each column.
    for i in range(3):
        counts = defaultdict(int)

        for row in range(len(board)):
            counts[board[row][i]] += 1

        for row in counts.keys():
            if counts[row] == 2 and row != " ":
                if row == ttt.PLAYERS[ttt.TURN]:
                    if " " in counts.keys():
                        return [board[0][i], board[1][i], board[2][i]].index(" "), i

                elif row != ttt.PLAYERS[ttt.TURN] and row != " ":
                    if " " in counts.keys():
                        point_of_interest = ([board[0][i], board[1][i], board[2][i]].index(" "), i)

    # Checking the first diagonal (going from left to right).
    counts = defaultdict(int)
    for i in range(3):
        counts[board[i][i]] += 1

    for point in counts:
        if counts[point] == 2 and point != " ":
            if point == ttt.PLAYERS[ttt.TURN]:
                if " " in counts.keys():
                    return [board[0][0], board[1][1], board[2][2]].index(" "), [board[0][0], board[1][1], board[2][2]].index(" ")

            elif point != ttt.PLAYERS[ttt.TURN] and point != " ":
                if " " in counts.keys():
                    point_of_interest = ([board[0][0], board[1][1], board[2][2]].index(" "), [board[0][0], board[1][1], board[2][2]].index(" "))        

    # Checking the second diagonal (going from right to left).
    counts = defaultdict(int)
    for i in range(3):
        counts[board[2-i][i]] += 1

    for point in counts:
        if counts[point] == 2 and point != " ":
            if point == ttt.PLAYERS[ttt.TURN]:
                if " " in counts.keys():
                    return 2-([board[2][0], board[1][1], board[0][2]].index(" ")), [board[2][0], board[1][1], board[0][2]].index(" ")

            elif point != ttt.PLAYERS[ttt.TURN] and point != " ":
                if " " in counts.keys():
                    point_of_interest = (2-[board[2][0], board[1][1], board[0][2]].index(" "), [board[2][0], board[1][1], board[0][2]].index(" "))
    
    # If there is a point that would prevent a loss, it would return here.
    if point_of_interest != tuple():
        return point_of_interest
    
    # Otherwise choose a random point using the easy_input function.  
    return easy_input(board)
