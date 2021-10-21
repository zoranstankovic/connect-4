def main():
    print()
    print("Welcome to Connect 4 Game")
    print()

    # CREATE THE BOARD
    board = [
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
    ]

    # CHOOSE INITIAL PLAYER
    # TODO: here I can improve this with randomly choosing who is first player
    active_player_index = 0
    # TODO: Ask for player(s) name
    players = ["Zoran", "Computer"]
    symbols = ['B', 'R']
    symbol = None
    position = None
    player = players[active_player_index]

    # UNTIL SOMEONE WINS
    while not find_winner(board, symbol, position):
        player = players[active_player_index]
        symbol = symbols[active_player_index]

        announce_turn(player)
        show_board(board)

        position = choose_location(board, symbol)
        if not position:
            print("That isn't an option, try again!")
            continue

        # TOGGLE ACTIVE PLAYER
        active_player_index = (active_player_index + 1) % len(players)

    print()
    print(f"GAME OVER! {player} has won with the board: ")
    show_board(board)
    print()


def find_winner(board, symbol, position):
    if not symbol and not position:
        return False

    # find winner horizontally
    # check next 3 positions to the right
    left_symbols = check_horizontally(board, position, symbol, "left")
    right_symbols = check_horizontally(board, position, symbol, "right")
    total_horizontally = left_symbols + right_symbols
    if total_horizontally >= 3:
        return True

    # CHECK THE WINNER VERTICALLY
    # vertically is enough to check down
    # check down
    total_down = check_down(board, position, symbol)
    if total_down >= 3:
        return True

    # CHECK DIAGONALS
    left_diagonal = check_diagonal(board, position, symbol, 'left')
    if left_diagonal >= 3:
        return True

    right_diagonal = check_diagonal(board, position, symbol, 'right')
    if right_diagonal >= 3:
        return True

    return False


def check_horizontally(board, start_position, symbol, direction):
    num_of_symbols = 0
    row = start_position[0]
    next_column = start_position[1]
    can_move = True
    while can_move:
        next_column = next_column - 1 if direction == "left" else next_column + 1
        if next_column < 0 or next_column >= len(board[0]) or symbol != board[row][next_column]:
            can_move = False
            continue

        num_of_symbols += 1

    return num_of_symbols


def check_down(board, start_position, symbol):
    num_of_symbols = 0
    column = start_position[1]
    next_row = start_position[0]
    can_move = True
    while can_move:
        next_row = next_row + 1
        if next_row >= 0 or symbol != board[next_row][column]:
            can_move = False
            continue

        num_of_symbols += 1

    return num_of_symbols


def check_diagonal(board, position, symbol, side):
    num_of_symbols = 0
    can_move_up = True
    can_move_down = True
    next_row = position[0]
    next_column = position[1]

    # check up
    while can_move_up:
        next_row, next_column = get_next_diagonal_position(
            side, 'up', [next_row, next_column])
        if next_column < 0 or next_column >= len(board[0]) or symbol != board[next_row][next_column]:
            can_move_up = False
            continue

        num_of_symbols += 1

    # we need to reset position
    next_row = position[0]
    next_column = position[1]

    # check down
    while can_move_down:
        next_row, next_column = get_next_diagonal_position(
            side, 'down', [next_row, next_column])

        if next_column < 0 or next_column >= len(board[0]) or symbol != board[next_row][next_column]:
            can_move_down = False
            continue

        num_of_symbols += 1

    return num_of_symbols


def get_next_diagonal_position(side, direction, current_position):
    next_row = current_position[0]
    next_column = current_position[1]
    if direction == 'up':
        next_row = current_position[0] + 1
        next_column = current_position[1] - \
            1 if side == 'left' else current_position[1] + 1
    elif direction == 'down':
        next_row = current_position[0] + 1
        next_column = current_position[1] + \
            1 if side == 'left' else current_position[1] + 1

    return next_row, next_column


def show_board(board):
    for row in board:
        print("| ", end='')
        for cell in row:
            symbol = cell if cell is not None else "_"
            print(symbol, end=" | ")
        print()


def announce_turn(player):
    print()
    print(f"It's {player}'s turn. Here's the board:")
    print()


def choose_location(board, symbol):
    """
    Ask player to choose location on the board
    where to put token/symbol
    :param list board: current board
    :param str symbol: players symbol
    :return: list with current token position
    :rtype: list
    """
    print()
    column = int(input("Choose which column: "))

    column -= 1

    if column < 0 or column >= len(board[0]):
        return False

    num_of_col_symbols = get_column_symbols_for_row(board, column)
    if num_of_col_symbols >= len(board):
        return False

    # we want to start from the last row
    start_row = -1
    # for every added symbol we will move row up
    row = start_row - num_of_col_symbols
    board[row][column] = symbol

    return [row, column]


def get_column_symbols_for_row(board, column):
    num_of_symbols = 0
    for row in board:
        if row[column]:
            num_of_symbols += 1

    return num_of_symbols


if __name__ == '__main__':
    main()
