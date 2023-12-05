def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def is_winner(board, current_symbol):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == current_symbol for j in range(3)) or all(board[j][i] == current_symbol for j in range(3)):
            return True
    if all(board[i][i] == current_symbol for i in range(3)) or all(board[i][2 - i] == current_symbol for i in range(3)):
        return True
    return False


def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)


def play_tic_tac_toe():
    game_board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player_symbol = 'X'

    while True:
        display_board(game_board)
        row = int(
            input(f"Player {current_player_symbol}, enter row (0, 1, or 2): "))
        col = int(
            input(f"Player {current_player_symbol}, enter column (0, 1, or 2): "))

        if game_board[row][col] == ' ':
            game_board[row][col] = current_player_symbol

            if is_winner(game_board, current_player_symbol):
                display_board(game_board)
                print(f"Player {current_player_symbol} wins!")
                break
            elif is_board_full(game_board):
                display_board(game_board)
                print("It's a draw!")
                break
            else:
                current_player_symbol = 'O' if current_player_symbol == 'X' else 'X'
        else:
            print("Cell already occupied. Try again.")


if __name__ == "__main__":
    play_tic_tac_toe()
