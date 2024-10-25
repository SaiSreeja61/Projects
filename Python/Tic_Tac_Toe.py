board=[" " for _ in range(9)]
def display_board(board):
    print(board[0]+"|"+board[1]+"|"+board[2])
    print("-+-+-")
    print(board[3]+"|"+board[4]+"|"+board[5])
    print("-+-+-")
    print(board[6]+"|"+board[7]+"|"+board[8])
def check_win(board,Player):
    win_combinations=[
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for combo in win_combinations:
        if all(board[i]==Player for i in combo):
            return True
    return False
current_player="X"
while True:
    display_board(board)
    position=int(input(f"Player {current_player} choose a position(0-8) : "))
    if board[position]==" ":
        board[position]=current_player
        if check_win(board,current_player):
            display_board(board)
            print(f"Player {current_player} Wins!")
            break
        if " " not in board:
            display_board(board)
            print("It's a Draw")
            break
        current_player="O" if current_player=="X" else "X"
    else:
        print("That position is already taken.Try again")