from random import randint


def create_position():                      # создание случайной позиции
    chess_board = [[i, j] for i in range(1, 9) for j in range(1, 9)]
    pos = []
    i = 1
    while len(pos) < 8:
        put = [i, randint(1, 8)]
        # print(put)
        if put not in pos:
            pos.append(put)
            i+=1
    # print(pos)
    return (pos)


def check_position(position):               # проверка позиции, принимает на вход список из координат
    x_pos = set(i[0] for i in position)
    y_pos = set(i[1] for i in position)
    # print(x_pos)
    # print(y_pos)
    if len(x_pos) != 8 or len(y_pos) != 8:
        # print('на одной оси')
        return False
    else:
        for i in position:
            for j in position:
                if i != j:
                    if abs(i[0] - j[0]) == abs(i[1] - j[1]):
                        # print('на одной диагонали')
                        return False
        return True


def get_true_positions(n):                  # получить n верных позиций
    list_positions = []

    while len(list_positions) < n:
        position = create_position()
        if check_position(position) and position not in list_positions:
            list_positions.append(position)

    return list_positions




