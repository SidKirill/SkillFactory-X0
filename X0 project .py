def play_game():
    print("Добро пожаловать в игру КРЕСТИКИ НОЛИКИ!\nПеред вами классическая версия игры.\nПрограмма принимает значения от 1 до 9.\n")


field = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def print_field():
    print(f"{field[0]} {field[1]} {field[2]}")
    print(f"{field[3]} {field[4]} {field[5]}")
    print(f"{field[6]} {field[7]} {field[8]}")


winning_comb = [[0, 1, 2], [4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]


def step_cell(step, sym):
    sign = field.index(step)
    field[sign] = sym


# функция передает позицию и рисует в поле переданное значение (X or 0)

def game_result():
    winner = ""
    for i in winning_comb:
        if field[i[0]] == "X" and field[i[1]] == "X" and field[i[2]] == "X":
            winner = "X"
        if field[i[0]] == "0" and field[i[1]] == "0" and field[i[2]] == "0":
            winner = "0"

    return winner
# после каждого хода проверяем на соответствие выигрышной комбинации

play_game()
game = False
player_ = True
count = 0
while game is False:
    count += 1
    print_field()
    if player_ is True:
        sym = "X"
        step = int(input("Ходит крестик: "))
    else:
        sym = "0"
        step = int(input("Ходит нолик: "))
    if count == 9:
        print_field()
        print("Игра окончена, ничья!")
        break
    if step < 1 or step > 9:
        print("Ошибка! Пожалуйста, начните заново.")
        print("Программа принимает значения от 1 от 9")
        break
    step_cell(step, sym)
    if type(str(step)) is False:
        print("Программа принимает только числа.")
        break
    # сделать ход в указанную ячейку
    winner = game_result()
    # проверяем условия победы
    if winner != "":
        game = True
        print_field()
        print("Выиграл ", winner)
#здесь выводит игровое поле и сообщение о победе, иначе цикл продолжается
    else:
        game = False
    player_ = not(player_)

