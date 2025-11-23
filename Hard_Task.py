print ('угадай пароль, состоящий из 2 букв английского алфавита, если хоть 1 будет верна, я тебе сообщу')
while True:
    import random
    c = 0
    a = input('введи первую букву пароля или сдайся (напиши нет)')
    b = input('введи вторую букву пароля или сдайся (напиши нет)')
    code = ord ('a')
    v = code+25
    rand_let1= v - random.randint(0, 25)
    rand_let2 = v - random.randint(0, 25)
    n = chr (rand_let1)
    m = chr(rand_let2)
    if a == n:
        c += 1
    if b == m:
        c += 1
    if c == 1:
        print('угадал 1 букву')
    if c == 2:
        print ('Tы выиграл')
        break
    elif c ==0:
        print ("Не угадал ни одной буквы. Пароль был "+ n+m)
    repeat = input("Cыграем еще? (да/нет).")
    if repeat.strip().lower() == 'нет':
        break


