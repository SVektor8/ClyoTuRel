from random import randrange


def print_double_mas(m):
    print('______________________' * len(m[0]))
    for i in m:
        for j in i:
            print(j, end=' ')
        print()


def trans(height, width, box_height, box_width, *args):
    # преобразование для интерпретатора из удобной
    x0 = args[0][0]
    y0 = args[0][1]
    return int(width + x0 - box_width / 2), int(height - box_height / 2 - y0)


def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def random_queue(mas):
    res = []
    while mas != []:
        q = randrange(len(mas))
        res.append(mas[q])
        del mas[q]

    return res


def print_replay_B(m, name, time):
    f = open('Clyo_replays/' + name + '.txt', 'a')
    f.write(reformat(time, 6))
    for i in m:
        for j in i:
            EE = j.Empire
            if EE == 'None':
                f.write('999')  # 3 symbols
            elif EE == 'Landscape':
                f.write('998')
            else:
                EE1 = EE.number
                if EE1 // 10 == 0:
                    f.write('00' + str(EE1))
                elif EE1 // 100 == 0:
                    f.write('0' + str(EE1))
                else:
                    f.write(str(EE))
            q = rreformat(round(j.Asabia, 2), 4)
            f.write(q[0] + q[2:])  # 3 symbols
    f.close()


def reformat(s, l):
    s = str(s)
    return str('0' * (l - len(s)) + s)


def rreformat(s, l):
    s = str(s)
    return str(s + '0' * (l - len(s)))


def print_replay_A2C(m, name, asabia):
    f = open('Clyo_replays/' + name + '.txt', 'a')
    for i in m:
        for j in i:

            EE = j.Empire
            if EE == 'Landscape':
                f.write('l')
            else:
                if EE == 'None':
                    f.write('n')
                else:
                    EE1 = str(EE.number)
                    if len(EE1) == 3:
                        f.write(EE1)
                    elif len(EE1) <= 2:
                        f.write('i')
                        f.write(reformat(EE1, 2))
                    elif len(EE1) <= 4:
                        f.write('j')
                        f.write(reformat(EE1, 4))
                    elif len(EE1) <= 6:
                        f.write('k')
                        f.write(reformat(EE1, 6))
                    else:
                        f.write('K')
                        f.write(EE1)
                        f.write('K')

                # q = round(j.Asabia, 3)
                # if q == 0.000:
                # f.write('z')
                # elif q == 1.000:
                # f.write('o')
                # elif q == asabia:
                # f.write('S')
                # else:
                # q1 = str(q)[0]
                # q = q1 + str(q)[2:]
                # f.write(str(len(q)))
                # f.write('%')
                # f.write(q)
                q = round(j.Asabia, 2)
                if q == 0.000:
                    f.write('z')
                elif q == 1.000:
                    f.write('o')
                elif q == round(asabia, 3):
                    f.write('S')
                else:
                    q1 = str(q)[0]
                    q = q1 + str(q)[2:]
                    f.write(str(len(q)))
                    f.write('%')
                    f.write(q)
    f.write('.')
    f.close()


def print_replay_C(m, name, asabia):
    f = open('Clyo_replays/' + name + '.txt', 'a')
    encode = 'abcdefghiklzos'
    for i in m:
        for j in i:

            EE = j.Empire
            if EE == 'Landscape':
                f.write('l')
            else:
                if EE == 'None':
                    f.write('n')
                else:
                    EE1 = str(EE.number)
                    f.write(EE1)

            q = round(j.Asabia, 2)
            if q == 0.000:
                f.write('z')
            elif q == 1.000:
                f.write('o')
            elif q == round(asabia, 3):
                f.write('S')
            else:
                q1 = str(q)[0]
                q = q1 + str(q)[2:]
                f.write(encode[len(q)])
                f.write(q)
    # f.write('.')
    f.close()


def read_envi(path):
    with open(path, 'r') as f:
        mas = [[j for j in i.split()] for i in f.read().splitlines()]
    for i in range(len(mas)):
        for j in range(1, len(mas[i])):
            if mas[i][0] == 'Emp' and j == 1:
                mas[i][j] = float(mas[i][j])
            else:
                mas[i][j] = int(mas[i][j])
    return mas


def write_envi(path, mas):
    mas = [[str(i) for i in j] for j in mas]
    with open(path, 'w') as f:
        for i in mas:
            for j in i:
                f.write(j)
                f.write(' ')
            f.write('\n')

def read_var(path):
    with open(path, 'r') as f:
        mas = [i for i in f.read().splitlines()]
        
    return mas
