from random import randint

total_stick = 21
running = True

while running:
    print("""
Привет! Добро пожаловать в игру "21 палочка". 
                    Вы можете выйти в любой момент набрав - "quit"
                                Желаем удачи!

На столе 21 палочка.                             
    """)
    while total_stick > 0:

        player_turn = True
        if player_turn:

            print('Ход игрока!'.center(30, '-'))
            if total_stick == 1 and player_turn:
                print('Последняя палочка достается вам. Увы!')
                running = False
                break
            stick_taken = input('Сколько палочек вы хотите взять?\n')
            if stick_taken.isdigit():
                stick_taken = int(stick_taken)
                if stick_taken not in range(1, 4):
                    print('Слишком много!')
                    continue
                if total_stick == 2 and stick_taken > 2:
                    print('Вы можете взять только 1 или 2 палочки')
                    continue
                if total_stick == 1 and stick_taken > 1:
                    print('Вы можете взять только 1 палочку')
                    continue
            elif stick_taken.lower() == 'quit':
                running = False
                print('Удачи!')
                break
            else:
                print('Некорректный ввод, попробуйте снова')
                continue

            total_stick -= stick_taken      # ## расчет
            if total_stick == 0 and player_turn:
                print(f'Игрок взял {stick_taken} и проиграл! Сожалеем, приходите снова!')
                running = False
                break
            print(f'Вы взяли {stick_taken}, осталось {total_stick}', '\n')
            player_turn = False

        if not player_turn:
            print('Ход компьютера'.center(30, '-'))
            stick_taken = randint(1, 3)
            if total_stick == 2 and stick_taken > 2:
                stick_taken = randint(1, 2)
            if total_stick == 1 and not player_turn:
                print('На столе осталась одна палочка, и сейчас ход компьютера! Вы выйграли!')
                running = False
                break

            total_stick -= stick_taken    # ## расчет

            if total_stick == 0 and not player_turn:
                print(f'Компьютер взял {stick_taken} и проиграл! Подзравляем, приходите снова!')
                running = False
                break
            print(f'*Компьютер взял {stick_taken}, осталось {total_stick}', '\n')
            player_turn = True
