# Створення ігрового поля 6x7
ROWS = 6
COLS = 7
EMPTY = " "
PLAYER1 = "X"
PLAYER2 = "O"


def create_board():
    return [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]


def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * (COLS * 2 - 1))
    print(" ".join(map(str, range(1, COLS + 1))))  # Номери стовпців


def is_valid_move(board, col):
    return board[0][col] == EMPTY


def drop_piece(board, col, piece):
    for row in reversed(board):
        if row[col] == EMPTY:
            row[col] = piece
            return True
    return False


def check_winner(board, piece):
    # Перевірка горизонтальних ліній
    for row in board:
        for col in range(COLS - 3):
            if all(row[col + i] == piece for i in range(4)):
                return True

    # Перевірка вертикальних ліній
    for col in range(COLS):
        for row in range(ROWS - 3):
            if all(board[row + i][col] == piece for i in range(4)):
                return True

    # Перевірка діагоналей (зліва направо)
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if all(board[row + i][col + i] == piece for i in range(4)):
                return True

    # Перевірка діагоналей (справа наліво)
    for row in range(ROWS - 3):
        for col in range(3, COLS):
            if all(board[row + i][col - i] == piece for i in range(4)):
                return True

    return False


def is_board_full(board):
    return all(cell != EMPTY for row in board for cell in row)


def main():
    board = create_board()
    current_player = PLAYER1

    while True:
        print_board(board)
        print(f"Гравець {current_player}, ваш хід!")

        try:
            col = int(input(f"Виберіть стовпець (1-{COLS}): ")) - 1
            if col < 0 or col >= COLS:
                print("Невірний стовпець. Спробуйте ще раз.")
                continue
        except ValueError:
            print("Будь ласка, введіть число.")
            continue

        if not is_valid_move(board, col):
            print("Стовпець заповнений. Спробуйте інший.")
            continue

        drop_piece(board, col, current_player)

        if check_winner(board, current_player):
            print_board(board)
            print(f"Гравець {current_player} переміг!")
            break

        if is_board_full(board):
            print_board(board)
            print("Нічия!")
            break

        current_player = PLAYER2 if current_player == PLAYER1 else PLAYER1


if __name__ == "__main__":
    main()
