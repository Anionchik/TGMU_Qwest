print ('угадай пароль, состоящий из 2 букв английского алфавита, если хоть 1 будет верна, я тебе сообщу')
while True:
    import random
    c = 0
    a = input('введи первую букву пароля или сдайся (напиши нет)')
    b = input('введи вторую букву пароля или сдайся (напиши нет)')
    code = ord ('a')
    c = code+25
    rand_let1= c - random.randint(0, 25)
    rand_let2 = c - random.randint(0, 25)
    n = chr (rand_let1)
    m = chr(rand_let2)
    if a == rand_let1:
        c += 1
    if b == rand_let2:
        c += 1
    if c == 1:
        print('угадал 1 букву')
    if c == 2:
        print ('ты выиграл')
        break
    repeat = input("обе не верны, сыграем еще? (да/нет).Пароль был "+ n+m )
    if repeat.strip().lower() == 'нет':
        break


