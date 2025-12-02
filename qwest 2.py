class PainLevel:
    def __init__(self):
        self.level = 5
    def increase(self, amount=1):
        self.level = min(10, self.level + amount)
        if self.level >= 8:
            print(f"Боль становится невыносимой! Уровень боли: {self.level}/10")
    def decrease(self, amount=1):
        self.level = max(1, self.level - amount)
    def is_critical(self):
        return self.level >= 8
def good():
    e = input("Клиника супер, стоимость 24000р. Лечимся (1), идем в государственную (2): ")
    if e == "1":
        print("Лечимся, Вове восстановили зубы и ничего не болит. Конеч")
    elif e == "2":
        bad()
def bad():
    print("Вове очень сильно везде хамят...")
    if pain.is_critical():
        print("Из-за сильной боли Вова раздражен и менее терпелив...")
    h = input("Продолжаем пробиваться (1) или идём к частнику (2): ")
    if h == "1":
        print("Вове вырвали 4 зуба без анестезии, зато сэкономил 400р. Конец")
    elif h == "2":
        good()
def ploho():
    global pain
    pain = PainLevel()
    while True:
        try:
            print('''У Вовы заболел зуб...''')
            c = input(
                'что делать Володе? Принять обезболивающее (1), пойти к стоматологу (2), терпеть "ты же мужик!"(3): ')
            c = int(c)
            if c > 4 or c < 1:
                print('Введи 1,2 или 3')
                continue
            elif 1 == c:
                pain.decrease(3)
                print('Стало легче, но это не надолго')
                if pain.level >= 6:
                    print("Обезболивающее почти не помогло...")
            elif 2 == c:
                print('Правильное решение! Осталось понять, куда обращаться')
                d = input('государственная (1) или частная (2) стоматология: ')
                if '1' == d:
                    pain.increase(1)
                    bad()
                elif "2" == d:
                    pain.decrease(1)
                    good()
            elif 3 == c:
                pain.increase(2)
                if pain.is_critical():
                    print("Терпит, но боль только усиливается...")
                else:
                    print('Терпит, вроде утихло...')
        except ValueError as error:
            print(f"Получено исключение {type(error)} — введите число 1, 2 или 3!")
            pain.increase(1)
        finally:
            print('Еще раз!')
pain = None
ploho()