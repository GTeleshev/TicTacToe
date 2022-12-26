where Python

print('Крестики-нолики')
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
position_numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def print_matrix(d2_list):
    for i in range(len(d2_list)):
        for j in range(len(d2_list[i])):
            print(d2_list[i][j], end=" ")
        print()
    print("_____")


def print_positions(d2_list: list):
    for i in range(len(d2_list)):
        for j in range(len(d2_list[i])):
            x = d2_list[i][j]
            if x == -1:
                print('x', end=" ")
            elif x == 1:
                print('o', end=" ")
            else:
                print("-", end=" ")
        print(" ")
    print("_____")


def check_score(pos_matrix: list):
    a = [0] * 8
    a[0] = pos_matrix[0][0] + pos_matrix[1][1] + pos_matrix[2][2]  # первая диагональ
    a[1] = pos_matrix[0][2] + pos_matrix[1][1] + pos_matrix[2][0]  # вторая диагональ
    a[2] = pos_matrix[0][0] + pos_matrix[1][0] + pos_matrix[2][0]  # столбец 1
    a[3] = pos_matrix[0][1] + pos_matrix[1][1] + pos_matrix[2][1]  # столбец 2
    a[4] = pos_matrix[0][2] + pos_matrix[1][2] + pos_matrix[2][2]  # столбец 3
    a[5] = pos_matrix[0][0] + pos_matrix[0][1] + pos_matrix[0][2]  # строка 1
    a[6] = pos_matrix[1][0] + pos_matrix[1][1] + pos_matrix[1][2]  # строка 2
    a[7] = pos_matrix[2][0] + pos_matrix[2][1] + pos_matrix[2][2]  # строка 3
    min_sc = min(*a)
    max_sc = max(*a)
    if min_sc == -3 and max_sc != 3:
        return -3
    elif max_sc == 3 and min_sc != -3:
        return 3
    elif max_sc == 3 and min_sc == -3:
        return 100
    else:
        return 0


def place_xo(board: list, player):
    pos = int(input('Введите позицию: '))
    row = 0
    column = 0
    for i in range(len(position_numbers)):
        for j in range(len(position_numbers)):
            if position_numbers[i][j] == pos:
                row = i
                column = j
    if board[row][column] != 0:
        return False
    else:
        board[row][column] = player
        return True


def rotate_player(player):
    if player == -1: return 1
    if player == 1: return -1


def game(board: list, player=-1):
    count = 1
    print("Номера клеток: ")
    print_matrix(position_numbers)
    while check_score(board) == 0 and count <= 9:
        print('Игрок: ', player)
        print('Ход: ', count)
        place_xo(board, player)
        score = check_score(board)
        player = rotate_player(player)
        print_positions(board)
        count += 1
    if score == -3:
        print("Игрок 1 выиграл")
    elif score == 3:
        print("Игрок 2 выиграл")
    elif score == 100 or count > 9:
        print("Ничья")


game(board)