#tictactoe game

board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

game_still_going=True
current_player="X"

winner=None
def display_board():
    print(board[0]+" | "+board[1]+" | "+board[2])
    print(board[3]+" | "+board[4]+" | "+board[5])
    print(board[6]+" | "+board[7]+" | "+board[8])

def play_game():
    display_board()
    
    while game_still_going:
        handle_turn(current_player)
        check_game_is_over()
        flip_player()
       
    if winner=="X" or winner=="O":
        print(winner+" won.")
    if winner==None:
        print("Tie. Nobody won.")

def handle_turn(player):
    print("Player "+current_player+" turn")
    position=int(input("Enter number b/w 1-9: "))
    print()
    if position>0 and position<10:
        position=position-1
        if board[position]=="-":
            board[position]=player
            display_board()
        else:
            print("That place is already taken Dumbo! GO Again.")
            handle_turn(player)
    else:
        handle_turn(current_player)
        
    
    
def check_game_is_over():
    check_for_winner()
    check_if_tie()
    return


def check_for_winner():
    row_winner()
    column_winner()
    diagonal_winner()
    return

def row_winner():
    global game_still_going
    global winner
    row1=board[0]==board[1]==board[2]!="-"
    row2=board[3]==board[4]==board[5]!="-"
    row3=board[6]==board[7]==board[8]!="-"
    if row1 or row2 or row3:
        game_still_going=False
    if row1:
        winner=board[0]
    if row2:
        winner=board[3]
    if row3:
        winner=board[6]
    return

def column_winner():
    global game_still_going
    global winner
    column1=board[0]==board[3]==board[6]!="-"
    column2=board[1]==board[4]==board[7]!="-"
    column3=board[2]==board[5]==board[8]!="-"
    if column1 or column2 or column3:
        game_still_going=False
    if column1:
        winner=board[0]
    if column2:
        winner=board[1]
    if column3:
        winner=board[2]
    return

def diagonal_winner():
    global game_still_going
    global winner
    diagonal1=board[0]==board[4]==board[8]!="-"
    diagonal2=board[2]==board[4]==board[6]!="-"
    if diagonal1 or diagonal2:
        game_still_going=False
    if diagonal1:
        winner=board[0]
    if diagonal2:
        winner=board[2]
    return



def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going=False
    return

    
def flip_player():
    global current_player
    if current_player=="X":
        current_player="O"
    else:
        current_player="X"
    return
play_game()



