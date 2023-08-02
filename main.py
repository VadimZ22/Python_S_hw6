from test_pack import check_date, create_position, check_position, get_true_positions
from sys import argv

# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на
# проверку.
# print(check_date(*(argv[1:])))


pos = create_position() # Создаем позицию и проверяем ее
print(pos)
print(check_position(pos), '\n\n')

pos_list = get_true_positions(4)         # Получаем 4 верных позиции
for pos in pos_list:
    print(pos)


    # ВЫВОД
    # [[1, 6], [2, 5], [3, 8], [4, 8], [5, 5], [6, 5], [7, 8], [8, 2]]
    # False
    #
    # [[1, 8], [2, 2], [3, 4], [4, 1], [5, 7], [6, 5], [7, 3], [8, 6]]
    # [[1, 4], [2, 2], [3, 8], [4, 6], [5, 1], [6, 3], [7, 5], [8, 7]]
    # [[1, 5], [2, 7], [3, 2], [4, 4], [5, 8], [6, 1], [7, 3], [8, 6]]
    # [[1, 6], [2, 4], [3, 1], [4, 5], [5, 8], [6, 2], [7, 7], [8, 3]]
