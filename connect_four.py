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
    players = get_players()
    tokens = ['B', 'R']
    token = None
    position = None
    player = players[active_player_index]

    # UNTIL SOMEONE WINS
    while not find_winner(board, token, position):
        player = players[active_player_index]
        token = tokens[active_player_index]

        announce_turn(player)
        show_board(board)

        position = choose_location(board, token)
        if not position:
            print("That isn't an option, try again!")
            continue

        # TOGGLE ACTIVE PLAYER
        active_player_index = (active_player_index + 1) % len(players)

    print()
    print(f"GAME OVER! {player} has won with the board: ")
    show_board(board)
    print()


def find_winner(board, token, position):
    if not token and not position:
        return False

    # find winner horizontally
    # check next 3 positions to the right
    left_tokens = check_horizontally(board, position, token, "left")
    right_toknes = check_horizontally(board, position, token, "right")
    total_horizontally = left_tokens + right_toknes
    if total_horizontally >= 3:
        return True

    # CHECK THE WINNER VERTICALLY
    # vertically is enough to check down
    # check down
    total_down = check_down(board, position, token)
    if total_down >= 3:
        return True

    # CHECK DIAGONALS
    left_diagonal = check_diagonal(board, position, token, 'left')
    if left_diagonal >= 3:
        return True

    right_diagonal = check_diagonal(board, position, token, 'right')
    if right_diagonal >= 3:
        return True

    return False


def check_horizontally(board, start_position, token, direction):
    num_of_tokens = 0
    row = start_position[0]
    next_column = start_position[1]
    can_move = True
    while can_move:
        next_column = next_column - 1 if direction == "left" else next_column + 1
        if next_column < 0 or next_column >= len(board[0]) or token != board[row][next_column]:
            can_move = False
            continue

        num_of_tokens += 1

    return num_of_tokens


def check_down(board, start_position, token):
    num_of_tokens = 0
    column = start_position[1]
    next_row = start_position[0]
    can_move = True
    while can_move:
        next_row = next_row + 1
        if next_row >= 0 or token != board[next_row][column]:
            can_move = False
            continue

        num_of_tokens += 1

    return num_of_tokens


def check_diagonal(board, position, token, side):
    num_of_tokens = 0
    can_move_up = True
    can_move_down = True
    next_row = position[0]
    next_column = position[1]

    # check up
    while can_move_up:
        next_row, next_column = get_next_diagonal_position(
            side, 'up', [next_row, next_column])
        if next_column < 0 or next_column >= len(board[0]) or token != board[next_row][next_column]:
            can_move_up = False
            continue

        num_of_tokens += 1

    # we need to reset position
    next_row = position[0]
    next_column = position[1]

    # check down
    while can_move_down:
        next_row, next_column = get_next_diagonal_position(
            side, 'down', [next_row, next_column])

        if next_column < 0 or next_column >= len(board[0]) or token != board[next_row][next_column]:
            can_move_down = False
            continue

        num_of_tokens += 1

    return num_of_tokens


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
            token = cell if cell is not None else "_"
            print(token, end=" | ")
        print()


def announce_turn(player):
    print()
    print(f"It's {player}'s turn. Here's the board:")
    print()


def choose_location(board, token):
    """
    Ask player to choose location on the board
    where to put token
    :param list board: current board
    :param str token: players token
    :return: list with current token position
    :rtype: list
    """
    print()
    column = int(input("Choose which column: "))

    column -= 1

    if column < 0 or column >= len(board[0]):
        return False

    num_of_col_tokens = get_column_tokens_for_row(board, column)
    if num_of_col_tokens >= len(board):
        return False

    # we want to start from the last row
    start_row = -1
    # for every added token we will move row up
    row = start_row - num_of_col_tokens
    board[row][column] = token

    return [row, column]


def get_column_tokens_for_row(board, column):
    num_of_tokens = 0
    for row in board:
        if row[column]:
            num_of_tokens += 1

    return num_of_tokens


def get_players():
    p1 = input('Please enter the name of Player 1: ')
    p2 = input('Please enter the name of Player 2: ')

    return p1, p2


if __name__ == '__main__':
    main()
