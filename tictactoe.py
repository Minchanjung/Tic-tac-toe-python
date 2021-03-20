game_board = {
    1: " ", 2: " ", 3: " ", 
    4: " ", 5: " ", 6: " ", 
    7: " ", 8: " ", 9: " "
}

def print_board(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])

#print(print_board(game_board))

def game():
    marker = "X"
    count = 0

    for i in range(10):
        print_board(game_board)
        print("its your turn, " + marker + " choose a position")

        move = input()
        if game_board[move] == " ":
            game_board[move] == marker
            count += 1
        
        else:
            print("that place is already filled")

        if count >= 5:
            if game_board[1] == game_board[2] == game_board[3] != " ": #top row win
                print_board(game_board)
                print("\nGame Over\n")
                print(marker + " has won")
                break

            elif game_board[4] == game_board[5] == game_board[6] != " ": #middle row win
                print_board(game_board)
                print("\nGame Over\n")
                print(marker + " has won")
                break

             elif game_board[7] == game_board[8] == game_board[9] != " ": #bottom row win
                print_board(game_board)
                print("\nGame Over\n")
                print(marker + " has won")
                break

            elif game_board[1] == game_board[4] == game_board[7] != " ": #first colunm win
                print_board(game_board)
                print("\nGame Over\n")
                print(marker + " has won")
                break

            elif game_board[2] == game_board[5] == game_board[8] != " ": #second colunm win
                print_board(game_board)
                print("\nGame Over\n")
                print(marker + " has won")
                break

            elif game_board[3] == game_board[6] == game_board[9] != " ": #third colunm win
                print_board(game_board)
                print("\nGame Over\n")
                print(marker + " has won")
                break

             elif game_board[1] == game_board[5] == game_board[9] != " ": #first diagonal win
                print_board(game_board)
                print("\nGame Over\n")
                print(marker + " has won")
                break

            elif game_board[7] == game_board[5] == game_board[3] != " ": #second diagonal win
                print_board(game_board)
                print("\nGame Over\n")
                print(marker + " has won")
                break

            