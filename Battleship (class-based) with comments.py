# Консольная версия игры "Морской бой" (с имитацией "искуственного интеллекта" в качестве оппонента).

# Из библиотеки 'random' импортирую функцию случайного выбора числа из заданного диапазона.
from random import randint

# Создаю игровое поле в виде двоичной матрицы (поле игрока).
grid_base = {
        0: [" ", "|", "1", "|", "2", "|", "3", "|", "4", "|", "5", "|", "6", "|"],
        1: ["1", "|", "0", "|", "0", "|", "0", "|", "0", "|", "0", "|", "0", "|"],
        2: ["2", "|", "0", "|", "0", "|", "0", "|", "0", "|", "0", "|", "0", "|"],
        3: ["3", "|", "0", "|", "0", "|", "0", "|", "0", "|", "0", "|", "0", "|"],
        4: ["4", "|", "0", "|", "0", "|", "0", "|", "0", "|", "0", "|", "0", "|"],
        5: ["5", "|", "0", "|", "0", "|", "0", "|", "0", "|", "0", "|", "0", "|"],
        6: ["6", "|", "0", "|", "0", "|", "0", "|", "0", "|", "0", "|", "0", "|"]
    }
# Создаю игровое поле в виде двоичной матрицы (поле компьютера-оппонента).
ai_grid_base = {
        0: [" ", "|", "1", "|", "2", "|", "3", "|", "4", "|", "5", "|", "6", "|"],
        1: ["1", "|", "0", "|", "0", "|", "0", "|", "0", "|", "0", "|", "0", "|"],
        2: ["2", "|", "0", "|", "0", "|", "0", "|", "0", "|", "0", "|", "0", "|"],
        3: ["3", "|", "0", "|", "0", "|", "0", "|", "0", "|", "0", "|", "0", "|"],
        4: ["4", "|", "0", "|", "0", "|", "0", "|", "0", "|", "0", "|", "0", "|"],
        5: ["5", "|", "0", "|", "0", "|", "0", "|", "0", "|", "0", "|", "0", "|"],
        6: ["6", "|", "0", "|", "0", "|", "0", "|", "0", "|", "0", "|", "0", "|"]
    }
# Создаю игровое поле в виде двоичной матрицы (поле компьютера-оппонента без отображения его кораблей
# (для показа игроку)).
hidden_ai_grid_base = {
        0: [" ", "|", "1", "|", "2", "|", "3", "|", "4", "|", "5", "|", "6", "|"],
        1: ["1", "|", "0", "|", "0", "|", "0", "|", "0", "|", "0", "|", "0", "|"],
        2: ["2", "|", "0", "|", "0", "|", "0", "|", "0", "|", "0", "|", "0", "|"],
        3: ["3", "|", "0", "|", "0", "|", "0", "|", "0", "|", "0", "|", "0", "|"],
        4: ["4", "|", "0", "|", "0", "|", "0", "|", "0", "|", "0", "|", "0", "|"],
        5: ["5", "|", "0", "|", "0", "|", "0", "|", "0", "|", "0", "|", "0", "|"],
        6: ["6", "|", "0", "|", "0", "|", "0", "|", "0", "|", "0", "|", "0", "|"]
    }


# Создаю класс, управляющий действиями с игровыми полями.
class Grid:
    # Создаю метод класса, печатающий в консоли матрицу пользовательского поля
    @classmethod
    def show_grid(cls):
        print("        User grid: ")
        for i in range(len(grid_base)):
            for j in range(len(grid_base[i])):
                print(grid_base[i][j], end=' ')
            print()

    # Создаю метод класса, печатающий в консоли матрицу поля компьютера-оппонента игрока
    @classmethod
    def show_ai_grid(cls):
        print("        AI grid: ")
        for i in range(len(ai_grid_base)):
            for j in range(len(ai_grid_base[i])):
                print(ai_grid_base[i][j], end=' ')
            print()

    # Создаю метод класса, печатающий в консоли матрицу поля компьютера-оппонента (без отображения его кораблей)
    @classmethod
    def show_hidden_ai_grid(cls):
        print("        AI grid: ")
        for i in range(len(hidden_ai_grid_base)):
            for j in range(len(hidden_ai_grid_base[i])):
                print(hidden_ai_grid_base[i][j], end=' ')
            print()

    # Создаю метод класса, печатающий в консоли экран приветствия, инструкции по количеству создаваемых кораблей и
    # матрицу поля игрока
    @classmethod
    def starting_screen(cls):
        print()
        print("\u2B50", "Welcome to Battleships!", "\u2B50")
        print()
        cls.show_grid()
        print("""
Before the start you need to place: 
- ONE three-deck ship, 
- TWO two-deck ships,
- THREE one-deck ships""")

    # Создаю метод, имитирующий стрельбу игрока по полю компьютера-оппонента
    @classmethod
    def user_shoot(cls):
        # Пояснение по отображению промахов и попаданий
        print()
        print("('x' = miss; 'Y' = hit)")
        print("Choose a position to shoot at.")
        # Отлов ошибки в случае, если пользователь вводит не цифры координат, а, например, текст
        # В случае срабатывания исключения вызывается сообщение об ошибке и метод перезапускается снова
        try:
            x = int(input("Enter x-coordinate: "))
            y = int(input("Enter y-coordinate: "))
            print()
        except ValueError:
            print("Please, enter correct coordinates!")
            cls.user_shoot()
        else:
            # Проверка на выход за пределы возможных значений координат
            # В случае выхода за пределы доступного диапазона вызывается сообщение об ошибке и
            # метод перезапускается снова
            if x < 1 or x > 6 or y < 1 or y > 6:
                print("Please, enter correct coordinates!")
                cls.user_shoot()
            else:
                # Проверка на позицию, уже занятую выстрелом ранее
                # В случае попадания в позицию, в которую пользователь уже стрелял ранее, вызывается сообщение об ошибке
                # и метод перезапускается снова
                if ai_grid_base[x][y * 2] == "x":
                    print("This position has already been shot at! Please, choose another position.")
                    cls.user_shoot()
                # Проверка на наличие корабля на позиции, введённой пользователем для выстрела
                # В случае попадания в корабль вызывается сообщение о попадании и символ, ранее обозначавший корабль,
                # меняется на символ, обозначающий подбитый корабль
                elif ai_grid_base[x][y * 2] == "\u25A0":
                    print("---You've hit an enemy's ship!---")
                    ai_grid_base[x].pop(y * 2)
                    ai_grid_base[x].insert(y * 2, "Y")
                    hidden_ai_grid_base[x].pop(y * 2)
                    hidden_ai_grid_base[x].insert(y * 2, "Y")
                    return ai_grid_base
                # В случае непопадания в корабль вызывается сообщение о промахе и символ, ранее обозначавший ещё не
                # обстрелянную позицию, меняется на символ, обозначающий уже обстрелянную позицию
                else:
                    print("---You've missed the shot.---")
                    ai_grid_base[x].pop(y * 2)
                    ai_grid_base[x].insert(y * 2, "x")
                    hidden_ai_grid_base[x].pop(y * 2)
                    hidden_ai_grid_base[x].insert(y * 2, "x")
                    return ai_grid_base

    # Создаю класс, имитирующий стрельбу компьютера-оппонента по полю игрока
    # По сути, он работает идентично методу, отвечающему за стрельбу игрока, описанному выше, но в нём, естественно,
    # отсутствуют проверки на введённые данные (так как ввод данных заменён в данном случае генерацией случайных чисел)
    # Единственная проверка - на уже обстрелянную позицию (при срабатывании она перезапускает метод)
    # Так же переписаны сообщения о попадании или промахе (уже не игрока, а оппонента-компьютера)
    @classmethod
    def ai_shoot(cls):
        x = randint(1, 6)
        y = randint(1, 6)
        if grid_base[x][y * 2] == "x":
            cls.ai_shoot()
        elif grid_base[x][y * 2] == "\u25A0":
            print("---Your ship has been hit by an enemy!---")
            grid_base[x].pop(y * 2)
            grid_base[x].insert(y * 2, "Y")
            return grid_base
        else:
            print("---Your enemy has missed the shot.---")
            grid_base[x].pop(y * 2)
            grid_base[x].insert(y * 2, "x")
            return grid_base


# Создаю класс, управляющий созданием и расположением на поле кораблей игрока.
class UserShip:

    # Метод, порождаюий и размещающий однопалубные корабли на поле игрока
    def create_ship_1(self):
        # Объявление, что создаётся однопалубный корабль
        print()
        print("Let's create a ONE-DECK ship")
        print()
        # Отлов ошибки в случае, если пользователь вводит не цифры координат, а что-то другое
        # В случае срабатывания исключения вызывается сообщение об ошибке и метод перезапускается снова
        try:
            x = int(input("Enter x-coordinate for your ship: "))
            y = int(input("Enter y-coordinate for your ship: "))
        except ValueError:
            print()
            print("Please, enter the correct coordinates!")
            self.create_ship_1()
        else:
            # Проверки на принадлежность введённых игроком координат к допустимому диапазону, а также на занятость
            # указанной позиции другим кораблём. В случае срабатывания выводятся сообщения о соответствующих ошибках
            # и метод перезапускается
            if 1 <= x <= 6 and 1 <= y <= 6:
                if grid_base[x][y * 2] == "\u25A0":
                    print()
                    print("This position has already been taken by another ship! Please, choose a different position.")
                    self.create_ship_1()
                else:
                    # В случае удовлетворения всех ограничивающих условий, исходные символы на игровом поле меняются
                    # на символы квадрата (обозначающие, что в том или ином месте находится корабль игрока)
                    print()
                    grid_base[x].pop(y * 2)
                    grid_base[x].insert(y * 2, "\u25A0")
                    return grid_base
            else:
                print()
                print("Please, enter the correct coordinates!")
                self.create_ship_1()

    # Метод, порождающий и размещающий на поле игрока двухпалубные корабли. Работает по схожей с предыдущим методом
    # (описанным выше) механике. Добавляется лишь дополнительная проверка на вхождение корабля в игровое поле. Если
    # создаваемый игроком корабль выходит за его пределы - выводится текст ошибки и метод перезапускается снова.
    def create_ship_2(self):
        print()
        print("Let's create a TWO-DECK ship")
        print()
        try:
            x = int(input("Enter x-coordinate for your ship: "))
            y = int(input("Enter y-coordinate for your ship: "))
        except ValueError:
            print("Please, enter the correct coordinates!")
            self.create_ship_2()
        else:
            if 1 <= x <= 6 and 1 <= y <= 6:
                print()
                orientation = input(
                    "Will your ship be placed horizontally (otherwise - vertically)? (y - yes, n - no): ")
                print()
                if orientation == "y" or orientation == "Y":
                    if grid_base[x][y * 2] == "\u25A0":
                        print(
                            "This position has already been taken by another ship! "
                            "Please, choose a different position."
                        )
                        self.create_ship_2()
                    else:
                        try:
                            if grid_base[x][(y+1) * 2] == "\u25A0":
                                print(
                                    "This position has already been taken by another ship! "
                                    "Please, choose a different position."
                                )
                                self.create_ship_2()
                            else:
                                grid_base[x].pop(y * 2)
                                grid_base[x].insert(y * 2, "\u25A0")
                                grid_base[x].pop((y + 1) * 2)
                                grid_base[x].insert((y + 1) * 2, "\u25A0")
                                return grid_base
                        except IndexError:
                            print("The ship goes outside the grid! Please, choose a different position.")
                            self.create_ship_2()
                        except KeyError:
                            print("The ship goes outside the grid! Please, choose a different position.")
                            self.create_ship_2()
                elif orientation == "n" or orientation == "N":
                    if grid_base[x][y * 2] == "\u25A0":
                        print(
                            "This position has already been taken by another ship! "
                            "Please, choose a different position."
                        )
                        self.create_ship_2()
                    else:
                        try:
                            if grid_base[x+1][y * 2] == "\u25A0":
                                print(
                                    "This position has already been taken by another ship! "
                                    "Please, choose a different position."
                                )
                                self.create_ship_2()
                            else:
                                grid_base[x].pop(y * 2)
                                grid_base[x].insert(y * 2, "\u25A0")
                                grid_base[x + 1].pop(y * 2)
                                grid_base[x + 1].insert(y * 2, "\u25A0")
                                return grid_base
                        except IndexError:
                            print("The ship goes outside the grid! Please, choose a different position.")
                            self.create_ship_2()
                        except KeyError:
                            print("The ship goes outside the grid! Please, choose a different position.")
                            self.create_ship_2()
                else:
                    print()
                    print("Please, enter correct answer (y / n)!")
                    self.create_ship_2()
            else:
                print()
                print("Please, enter the correct coordinates!")
                self.create_ship_2()

    # Метод, порождающий и размещающий на поле игрока трёхпалубные корабли. Работает по схожей с предыдущим методом
    # создания двухпалубных кораблей (описанным выше) механике.
    def create_ship_3(self):
        print()
        print("Let's create a THREE-DECK ship")
        print()
        try:
            x = int(input("Enter x-coordinate for your ship: "))
            y = int(input("Enter y-coordinate for your ship: "))
        except ValueError:
            print("Please, enter the correct coordinates!")
            self.create_ship_3()
        else:
            if 1 <= x <= 6 and 1 <= y <= 6:
                print()
                orientation = input(
                    "Will your ship be placed horizontally (otherwise - vertically)? (y - yes, n - no): ")
                print()
                if orientation == "y" or orientation == "Y":
                    if grid_base[x][y * 2] == "\u25A0":
                        print(
                            "This position has already been taken by another ship! "
                            "Please, choose a different position."
                        )
                        self.create_ship_3()
                    else:
                        try:
                            if grid_base[x][(y+1) * 2] == "\u25A0" or grid_base[x][(y+2) * 2] == "\u25A0":
                                print(
                                    "This position has already been taken by another ship! "
                                    "Please, choose a different position."
                                )
                                self.create_ship_3()
                            else:
                                grid_base[x].pop(y * 2)
                                grid_base[x].insert(y * 2, "\u25A0")
                                grid_base[x].pop((y + 1) * 2)
                                grid_base[x].insert((y + 1) * 2, "\u25A0")
                                grid_base[x].pop((y + 2) * 2)
                                grid_base[x].insert((y + 2) * 2, "\u25A0")
                                return grid_base
                        except IndexError:
                            print("The ship goes outside the grid! Please, choose a different position.")
                            self.create_ship_3()
                        except KeyError:
                            print("The ship goes outside the grid! Please, choose a different position.")
                            self.create_ship_3()
                elif orientation == "n" or orientation == "N":
                    if grid_base[x][y * 2] == "\u25A0":
                        print(
                            "This position has already been taken by another ship! "
                            "Please, choose a different position."
                        )
                        self.create_ship_3()
                    else:
                        try:
                            if grid_base[x+1][y * 2] == "\u25A0" or grid_base[x+2][y * 2] == "\u25A0":
                                print(
                                    "This position has already been taken by another ship! "
                                    "Please, choose a different position."
                                )
                                self.create_ship_3()
                            else:
                                grid_base[x].pop(y * 2)
                                grid_base[x].insert(y * 2, "\u25A0")
                                grid_base[x + 1].pop(y * 2)
                                grid_base[x + 1].insert(y * 2, "\u25A0")
                                grid_base[x + 2].pop(y * 2)
                                grid_base[x + 2].insert(y * 2, "\u25A0")
                                return grid_base
                        except IndexError:
                            print("The ship goes outside the grid! Please, choose a different position.")
                            self.create_ship_3()
                        except KeyError:
                            print("The ship goes outside the grid! Please, choose a different position.")
                            self.create_ship_3()
                else:
                    print()
                    print("Please, enter correct answer (y / n)!")
                    self.create_ship_3()
            else:
                print()
                print("Please, enter the correct coordinates!")
                self.create_ship_3()

    # Статический метод, собирающий вышеизложенные методы воедино, для создания полного набора кораблей игрока. Основан
    # на цикле со счётчиком. Создаются последовательно: 3 однопалубных корабля, 2 двухпалубных корабля и 1 трёхпалубный
    # корабль. После того, как счётчик создания кораблей получает значение 6 (по общему количеству созданных кораблей),
    # цикл прерывается.
    @staticmethod
    def create_user_ships():
        counter = 0
        ship = UserShip()

        while counter != 6:
            ship.create_ship_1()
            counter += 1
            Grid.show_grid()
            ship.create_ship_1()
            counter += 1
            Grid.show_grid()
            ship.create_ship_1()
            counter += 1
            Grid.show_grid()
            ship.create_ship_2()
            counter += 1
            Grid.show_grid()
            ship.create_ship_2()
            counter += 1
            Grid.show_grid()
            ship.create_ship_3()
            counter += 1
            Grid.show_grid()


# Создаю класс (наследник класса-родителя, создающего корабли игрока), управляющий созданием и расположением на поле
# кораблей компьютера-оппонента. Работает по схожей логике и имеет те же методы, что и класс-родитель. Так же, как и
# с методами, отвечвющими за стрельбу, описанными в предыдущем классе 'Grid', в отличие от методов создания кораблей
# игрока, работает не на введённых пользователем данных, а на генерации случайных чисел в заданном диапазоне. Также
# отсутствует большинство проверок (кроме отвечающих за уже занятые позиции или за невыход корабля за пределы
# игрового поля).
class AiShip(UserShip):

    def create_ship_1(self):
        x = randint(1, 6)
        y = randint(1, 6)
        if ai_grid_base[x][y * 2] == "\u25A0":
            self.create_ship_1()
        else:
            ai_grid_base[x].pop(y * 2)
            ai_grid_base[x].insert(y * 2, "\u25A0")
            return ai_grid_base

    def create_ship_2(self):
        x = randint(1, 6)
        y = randint(1, 6)
        orientation = randint(1, 2)
        if orientation == 1:
            if ai_grid_base[x][y * 2] == "\u25A0":
                self.create_ship_2()
            else:
                try:
                    if ai_grid_base[x][(y+1) * 2] == "\u25A0":
                        self.create_ship_2()
                    else:
                        ai_grid_base[x].pop(y * 2)
                        ai_grid_base[x].insert(y * 2, "\u25A0")
                        ai_grid_base[x].pop((y + 1) * 2)
                        ai_grid_base[x].insert((y + 1) * 2, "\u25A0")
                        return ai_grid_base
                except IndexError:
                    self.create_ship_2()
                except KeyError:
                    self.create_ship_2()
        elif orientation == 2:
            if ai_grid_base[x][y * 2] == "\u25A0":
                self.create_ship_2()
            else:
                try:
                    if ai_grid_base[x+1][y * 2] == "\u25A0":
                        self.create_ship_2()
                    else:
                        ai_grid_base[x].pop(y * 2)
                        ai_grid_base[x].insert(y * 2, "\u25A0")
                        ai_grid_base[x + 1].pop(y * 2)
                        ai_grid_base[x + 1].insert(y * 2, "\u25A0")
                        return ai_grid_base
                except IndexError:
                    self.create_ship_2()
                except KeyError:
                    self.create_ship_2()

    def create_ship_3(self):
        x = randint(1, 6)
        y = randint(1, 6)
        orientation = randint(1, 2)
        if orientation == 1:
            if ai_grid_base[x][y * 2] == "\u25A0":
                self.create_ship_3()
            else:
                try:
                    if ai_grid_base[x][(y + 1) * 2] == "\u25A0" or ai_grid_base[x][(y + 2) * 2] == "\u25A0":
                        self.create_ship_3()
                    else:
                        ai_grid_base[x].pop(y * 2)
                        ai_grid_base[x].insert(y * 2, "\u25A0")
                        ai_grid_base[x].pop((y + 1) * 2)
                        ai_grid_base[x].insert((y + 1) * 2, "\u25A0")
                        ai_grid_base[x].pop((y + 2) * 2)
                        ai_grid_base[x].insert((y + 2) * 2, "\u25A0")
                        return ai_grid_base
                except IndexError:
                    self.create_ship_3()
                except KeyError:
                    self.create_ship_3()
        elif orientation == 2:
            if ai_grid_base[x][y * 2] == "\u25A0":
                self.create_ship_3()
            else:
                try:
                    if ai_grid_base[x + 1][y * 2] == "\u25A0" or ai_grid_base[x + 2][y * 2] == "\u25A0":
                        self.create_ship_3()
                    else:
                        ai_grid_base[x].pop(y * 2)
                        ai_grid_base[x].insert(y * 2, "\u25A0")
                        ai_grid_base[x + 1].pop(y * 2)
                        ai_grid_base[x + 1].insert(y * 2, "\u25A0")
                        ai_grid_base[x + 2].pop(y * 2)
                        ai_grid_base[x + 2].insert(y * 2, "\u25A0")
                        return ai_grid_base
                except IndexError:
                    self.create_ship_3()
                except KeyError:
                    self.create_ship_3()

    @staticmethod
    def create_ai_ships():
        counter = 0
        ai_ship = AiShip()

        while counter != 6:
            ai_ship.create_ship_1()
            counter += 1
            ai_ship.create_ship_1()
            counter += 1
            ai_ship.create_ship_1()
            counter += 1
            ai_ship.create_ship_2()
            counter += 1
            ai_ship.create_ship_2()
            counter += 1
            ai_ship.create_ship_3()
            counter += 1
            Grid.show_hidden_ai_grid()


# Создаю класс, отвечающий за общую логику игры.
class Game:
    # Единственный метод класса отвечает за сбор методов других классов в единый механизм (логику игры)
    @classmethod
    def initialize_game(cls):
        # Вызов метода отображения стартового экрана, вызов методов создания кораблей (сначала игрока, затем
        # компьютера-оппонента)
        Grid.starting_screen()
        UserShip.create_user_ships()
        print()
        AiShip.create_ai_ships()
        # Создание цикла с пост-условием, чередующего ходы игрока и компьютера-оппонента, а также выводящий в консоль
        # текущее состояние игровых полей
        while True:
            Grid.user_shoot()
            Grid.show_hidden_ai_grid()
            print()
            Grid.ai_shoot()
            Grid.show_grid()
            # Создание условия окончания игры. Если на поле компьютера-оппонента не остаётся символов, обозначающих
            # корабли - выводится сообщение о победе игрока и цикл (и игра вместе с ним) прерывается. Если же на поле
            # игрока не остаётся символов, обозначающих корабли - выводится сообщение о поражении игрока и игра также
            # прерывается.
            if "\u25A0" not in ai_grid_base[1] and "\u25A0" not in ai_grid_base[2] and "\u25A0" not in ai_grid_base[3] \
                    and "\u25A0" not in ai_grid_base[4] and "\u25A0" not in ai_grid_base[5] and "\u25A0" not in \
                    ai_grid_base[6]:
                print()
                print("\U0001F601", "You have destroyed all enemy's ships! You've won!", "\U0001F601")
                print("Press 'Shift' + 'f10' to start a new game.")
                break
            elif "\u25A0" not in grid_base[1] and "\u25A0" not in grid_base[2] and "\u25A0" not in grid_base[3] \
                    and "\u25A0" not in grid_base[4] and "\u25A0" not in grid_base[5] and "\u25A0" not in grid_base[6]:
                print()
                print("\U0001F622", "The enemy has destroyed all your ships! You've lost!", "\U0001F622")
                print("Press 'Shift' + 'f10' to start a new game.")
                break


# Запуск игры с помощью главного метода.
Game.initialize_game()
