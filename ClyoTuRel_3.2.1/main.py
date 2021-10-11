import datetime
import os
from tkinter import *

import pygame

import allcolors
from coms import *
from graph import *


def load_replay():
    global loading_replay

    loading_replay = 1


def creet():
    global txt15, crit_time
    crit_time = int(txt15.get())


def errwindow():
    global erwindow

    erwindow = Tk()
    erwindow.title('Main menu')

    w = erwindow.winfo_screenwidth() - 500
    h = 0
    erwindow.geometry('+{}+{}'.format(w, h))

    lbl0 = Label(erwindow, text="Oh, look, an error.")
    lbl0.grid(column=0, row=0)

    btn2 = Button(erwindow, text='     OK     ', command=main_menu)
    btn2.grid(column=0, row=2)

    window11.mainloop()


def skip_and_GOOOO():
    global txt_skip, real_time

    real_time = int(txt_skip.get())


def save_renamed():
    global name0, txt0000

    name1 = txt0000.get()
    os.renames('Clyo_replays/' + name0 + '.txt', 'Clyo_replays/' + name1 + '.txt')
    name0 = name1

    begin()
    ask()


def rename_replay():
    global rename_window, name0, txt0000

    begin()

    rename_window = Tk()
    rename_window.title('Rename current replay')

    w = rename_window.winfo_screenwidth() - 1000
    h = 300
    rename_window.geometry('+{}+{}'.format(w, h))

    lbl0 = Label(rename_window, text='Name of the replay')
    lbl0.grid(column=0, row=0)

    txt0000 = Entry(rename_window, width=30)
    txt0000.grid(column=1, row=0)
    txt0000.insert(0, name0)

    btn0 = Button(rename_window, text='Save', command=save_renamed)
    btn0.grid(column=2, row=0)

    btn1 = Button(rename_window, text='Go to the main menu', command=main_menu)
    btn1.grid(column=0, row=1)

    rename_window.mainloop()


def default_launch():
    global mode
    mode = 'Launch'
    new()
    begin()


def watch_replay():
    global mode, first, replay_name, txt000, txt111, replay_version, erwindow, loading_replay

    loading_replay = 0
    replay_name = txt000.get()

    try:
        f = open('Clyo_replays/' + replay_name + '.txt', 'r')
        f.close()
    except:
        erwindow = Tk()
        erwindow.title('Main menu')

        w = erwindow.winfo_screenwidth() - 500
        h = 0
        erwindow.geometry('+{}+{}'.format(w, h))

        lbl0 = Label(erwindow, text="Replay with this name doesn't exist")
        lbl0.grid(column=0, row=0)

        btn2 = Button(erwindow, text='     OK     ', command=replay_menu)
        btn2.grid(column=0, row=2)

        erwindow.mainloop()

    finally:
        try:
            replay_version = txt111.get()
        except:
            erwindow = Tk()
            erwindow.title('Main menu')

            w = erwindow.winfo_screenwidth() - 500
            h = 0
            erwindow.geometry('+{}+{}'.format(w, h))

            lbl0 = Label(erwindow, text="Such format doesn't exist")
            lbl0.grid(column=0, row=0)

            btn2 = Button(erwindow, text='     OK     ', command=replay_menu)
            btn2.grid(column=0, row=2)

            erwindow.mainloop()
        finally:
            mode = 'Replay'
            first = True
            begin()


def replay_menu():
    global window11, window, window1, txt000, txt111

    begin()

    window11 = Tk()
    window11.title('Main menu')

    w = window11.winfo_screenwidth() - 500
    h = 0
    window11.geometry('+{}+{}'.format(w, h))

    lbl0 = Label(window11, text='Name of the replay')
    lbl0.grid(column=0, row=0)

    txt000 = Entry(window11, width=30)
    txt000.grid(column=1, row=0)

    btn0 = Button(window11, text='Start', command=watch_replay)
    btn0.grid(column=1, row=2)

    lbl1 = Label(window11, text='Replay format')
    lbl1.grid(column=0, row=1)

    txt111 = Entry(window11, width=30)
    txt111.grid(column=1, row=1)
    txt111.insert(0, 'C')

    btn2 = Button(window11, text='Go to the main menu', command=main_menu)
    btn2.grid(column=0, row=2)

    window11.mainloop()


def main_menu():
    global window1, window11, mode

    mode = 'None'

    begin()

    window1 = Tk()
    window1.title('Main menu')

    w = window1.winfo_screenwidth() - 500
    h = 0
    window1.geometry('+{}+{}'.format(w, h))

    btn0 = Button(window1, text='Simulate with default parameters', command=default_launch)
    btn0.grid(column=0, row=0)

    btn1 = Button(window1, text='Go to the managment panel', command=ask)
    btn1.grid(column=0, row=1)

    btn2 = Button(window1, text='Watch a replay', command=replay_menu)
    btn2.grid(column=0, row=2)

    window1.mainloop()


def print_asabia(coords):
    global r0, d, h, dp, S_critical, StartAsabia, Imperial_Asabia
    global chance, length, width, FPS, WIDTH, HEIGHT
    global Empires, BigMap, clrs, Empiresq, lc, do
    global ki, kj, time, res, AllFields, DeltaFields
    global one_step, print_always, crit_time
    i = int(coords[0] // ki)
    j = int(coords[1] // kj)
    global lbl0, txt0, lbl1, txt1, lbl2, txt2, lbl3, txt3
    global lbl4, txt4, lbl5, txt5, lbl6, txt6, lbl7, txt7
    global lbl8, txt8, lbl9, txt9, lbl10, txt10, lbl11
    global txt11, lbl12, txt12, lbl13, txt13, window, time
    global print_always, txt14

    window = Tk()
    window.title('Management panel')

    w = window.winfo_screenwidth() - 300
    h = 0
    window.geometry('+{}+{}'.format(w, h))

    Cell = BigMap[j][i]
    if Cell.Empire == 'None' or Cell.Empire == 'Landscape':
        res = str(Cell.Empire) + ' ' + Cell.Borders + ' ' + str(round(Cell.Asabia, 2))
    else:
        res = str(Cell.Empire.number) + ' ' + Cell.Borders + ' ' + str(round(Cell.Asabia, 2))

    lbl0 = Label(window, text=res)
    lbl0.grid(column=0, row=0)

    btn1 = Button(window, text='            Simulate            ', command=begin)
    btn1.grid(column=0, row=1)

    btn2 = Button(window, text='   Management panel   ', command=ask)
    btn2.grid(column=0, row=2)

    window.mainloop()


def print_asabia_replay(coords):
    global r0, d, h, dp, S_critical, StartAsabia, Imperial_Asabia
    global chance, length, width, FPS, WIDTH, HEIGHT
    global Empires, BigMap, clrs, Empiresq, lc, do
    global ki, kj, time, res, AllFields, DeltaFields
    global one_step, print_always, crit_time
    i = int(coords[0] // ki)
    j = int(coords[1] // kj)
    global lbl0, txt0, lbl1, txt1, lbl2, txt2, lbl3, txt3
    global lbl4, txt4, lbl5, txt5, lbl6, txt6, lbl7, txt7
    global lbl8, txt8, lbl9, txt9, lbl10, txt10, lbl11
    global txt11, lbl12, txt12, lbl13, txt13, window, time
    global print_always, txt14, BiggMapp

    window = Tk()
    window.title('Management panel')

    w = window.winfo_screenwidth() - 300
    h = 0
    window.geometry('+{}+{}'.format(w, h))

    Cell = BiggMapp[j][i]
    res = ''

    if Cell[0] == 'n':
        res += 'None'
    elif Cell[0] == 'l':
        res += 'Landscape'
    else:
        res += str(Cell[0])

    res += ' '
    res += (Cell[1][0] + '.' + Cell[1][1:])

    lbl0 = Label(window, text=res)
    lbl0.grid(column=0, row=0)

    btn1 = Button(window, text='            Simulate            ', command=begin)
    btn1.grid(column=0, row=1)

    btn2 = Button(window, text='   Management panel   ', command=ask_replay)
    btn2.grid(column=0, row=2)

    window.mainloop()


def apply():
    global r0, d, h, dp, S_critical, StartAsabia, Imperial_Asabia
    global chance, length, width, FPS, WIDTH, HEIGHT
    global Empires, BigMap, clrs, Empiresq, lc, do
    global ki, kj, time, res, print_always, mode, txt16, writing_replays

    if mode == 'Launch':
        r0 = float(txt0.get())
        d = float(txt1.get())
        h = float(txt2.get())
        dp = float(txt3.get())
        S_critical = float(txt4.get())
        StartAsabia = float(txt5.get())
        Imperial_Asabia = float(txt6.get())
        chance = float(txt7.get())
        length = int(txt8.get())
        width = int(txt9.get())
    FPS = int(txt10.get())
    WIDTH = int(txt11.get())
    HEIGHT = int(txt12.get())
    print_always = int(txt14.get())
    writing_replays = int(txt16.get())

    ki = HEIGHT / width
    kj = WIDTH / length


def default():
    global lbl0, txt0, lbl1, txt1, lbl2, txt2, lbl3, txt3
    global lbl4, txt4, lbl5, txt5, lbl6, txt6, lbl7, txt7
    global lbl8, txt8, lbl9, txt9, lbl10, txt10, lbl11
    global txt11, lbl12, txt12, lbl13, txt13, window, txt14
    global r0, d, h, dp, S_critical, StartAsabia, Imperial_Asabia
    global chance, length, width, FPS, WIDTH, HEIGHT
    global Empires, Empiresq, BigMap, do, print_always

    do = 1
    r0 = 0.2
    d = 0.1
    h = 2
    dp = 0.1
    S_critical = 0.003
    StartAsabia = 0.003
    Imperial_Asabia = 0.0035
    chance = 1
    print_always = 1

    length = 21
    width = 21

    FPS = 5
    WIDTH = 600  # ширина экрана
    HEIGHT = 600  # высота экрана

    txt14.delete(0, END)
    txt13.delete(0, END)
    txt12.delete(0, END)
    txt11.delete(0, END)
    txt10.delete(0, END)
    txt9.delete(0, END)
    txt8.delete(0, END)
    txt7.delete(0, END)
    txt6.delete(0, END)
    txt5.delete(0, END)
    txt4.delete(0, END)
    txt3.delete(0, END)
    txt2.delete(0, END)
    txt1.delete(0, END)
    txt0.delete(0, END)

    txt14.insert(0, print_always)
    txt13.insert(0, time)
    txt12.insert(0, HEIGHT)
    txt11.insert(0, WIDTH)
    txt10.insert(0, FPS)
    txt9.insert(0, width)
    txt8.insert(0, length)
    txt7.insert(0, chance)
    txt6.insert(0, Imperial_Asabia)
    txt5.insert(0, StartAsabia)
    txt4.insert(0, S_critical)
    txt3.insert(0, dp)
    txt2.insert(0, h)
    txt1.insert(0, d)
    txt0.insert(0, r0)


def new():
    global lbl0, txt0, lbl1, txt1, lbl2, txt2, lbl3, txt3
    global lbl4, txt4, lbl5, txt5, lbl6, txt6, lbl7, txt7
    global lbl8, txt8, lbl9, txt9, lbl10, txt10, lbl11
    global txt11, lbl12, txt12, lbl13, txt13, window
    global r0, d, h, dp, S_critical, StartAsabia, Imperial_Asabia
    global chance, length, width, FPS, WIDTH, HEIGHT
    global Empires, BigMap, clrs, Empiresq, lc, do
    global ki, kj, time, res, AllFields, DeltaFields
    global one_step, crit_time, name0, mode, writing_replays

    clrs = [allcolors.KINOVAR(), allcolors.SKYBLUE(), allcolors.YELLOW(), allcolors.GRAY(),
            allcolors.GREEN(), allcolors.LUMINESCENTRED(), allcolors.BLACK(),
            allcolors.BERLIN_LAZUR(), allcolors.OLIVE(), allcolors.RED(), allcolors.DARKKHAKI()]
    clrs += allcolors.AllColors
    lc = len(clrs)

    Empires = []
    Empiresq = [0]

    f = open('data/map.txt', 'r')

    nums = f.read().splitlines()

    length, width = map(int, nums[0].split())

    WIDTH = int(600 * length / 21)
    HEIGHT = int(600 * width / 21)

    BigMap = [[Field(r0, d, StartAsabia, h, dp, length, width, x, y, chance) for x in range(length)] for y in
              range(width)]

    for i in range(1, len(nums)):
        exec(nums[i])

    f.close

    for i in BigMap:
        for j in i:
            j.BigMapP = BigMap
            j.AllEmpires = Empires

    for i in Empires:
        i.pre_update()

    for i in BigMap:
        for j in i:
            j.pre_update()

    for i in Empires:
        i.update()

    ki = HEIGHT / width
    kj = WIDTH / length

    time = 0
    crit_time = 0
    res = 0

    AllFields = []

    for i in range(width):
        for j in range(length):
            AllFields.append((i, j))

    DeltaFields = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    if mode == 'Launch' and writing_replays:
        name0 = 'v.C_' + str(datetime.datetime.isoformat(datetime.datetime.now(), sep='_'))[:-7].replace(':', '-')

        try:
            os.mkdir('Clyo_replays')
        except:
            time = 0

        f = open('Clyo_replays/' + name0 + '.txt', 'a')

        a0 = max(len(str(length)), len(str(width)))
        wres = str(a0) + '%' + reformat(length, a0) + reformat(width, a0)

        f.write(wres)
        f.close


def begin():
    global window, window1, window11, rename_window, erwindow

    try:
        window.destroy()
    except:
        c = 0

    try:
        window1.destroy()
    except:
        a = 0

    try:
        window11.destroy()
    except:
        b = 0

    try:
        rename_window.destroy()
    except:
        d = 0

    try:
        erwindow.destroy()
    except:
        e = 0


def begin1():
    global mode

    mode = 'Launch'

    begin()


def begin11():
    global window11

    window11.destroy()


def put_out():
    global BigMap
    print_double_mas(BigMap)


def one_move():
    global one_step
    one_step = 1
    begin()


def ask():
    global lbl0, txt0, lbl1, txt1, lbl2, txt2, lbl3, txt3
    global lbl4, txt4, lbl5, txt5, lbl6, txt6, lbl7, txt7
    global lbl8, txt8, lbl9, txt9, lbl10, txt10, lbl11
    global txt11, lbl12, txt12, lbl13, txt13, window, time
    global print_always, txt14, txt15, txt16

    begin()

    window = Tk()
    window.title('Management panel')

    w = window.winfo_screenwidth() - 300
    h = 0
    window.geometry('+{}+{}'.format(w, h))

    lbl0 = Label(window, text='r0')
    lbl0.grid(column=0, row=0)

    txt0 = Entry(window, width=10)
    txt0.grid(column=1, row=0)
    txt0.insert(0, r0)

    lbl1 = Label(window, text='d')
    lbl1.grid(column=0, row=1)

    txt1 = Entry(window, width=10)
    txt1.grid(column=1, row=1)
    txt1.insert(0, d)

    lbl2 = Label(window, text='h')
    lbl2.grid(column=0, row=2)

    txt2 = Entry(window, width=10)
    txt2.grid(column=1, row=2)
    txt2.insert(0, h)

    lbl3 = Label(window, text='dp')
    lbl3.grid(column=0, row=3)

    txt3 = Entry(window, width=10)
    txt3.grid(column=1, row=3)
    txt3.insert(0, dp)

    lbl4 = Label(window, text='S_critical')
    lbl4.grid(column=0, row=4)

    txt4 = Entry(window, width=10)
    txt4.grid(column=1, row=4)
    txt4.insert(0, S_critical)

    lbl5 = Label(window, text='StartAsabia')
    lbl5.grid(column=0, row=5)

    txt5 = Entry(window, width=10)
    txt5.grid(column=1, row=5)
    txt5.insert(0, StartAsabia)

    lbl6 = Label(window, text='Imperial_Asabia')
    lbl6.grid(column=0, row=6)

    txt6 = Entry(window, width=10)
    txt6.grid(column=1, row=6)
    txt6.insert(0, Imperial_Asabia)

    lbl7 = Label(window, text=' chance')
    lbl7.grid(column=0, row=7)

    txt7 = Entry(window, width=10)
    txt7.grid(column=1, row=7)
    txt7.insert(0, chance)

    lbl8 = Label(window, text='length')
    lbl8.grid(column=0, row=8)

    txt8 = Entry(window, width=10)
    txt8.grid(column=1, row=8)
    txt8.insert(0, length)

    lbl9 = Label(window, text='width')
    lbl9.grid(column=0, row=9)

    txt9 = Entry(window, width=10)
    txt9.grid(column=1, row=9)
    txt9.insert(0, width)

    lbl10 = Label(window, text='FPS')
    lbl10.grid(column=0, row=10)

    txt10 = Entry(window, width=10)
    txt10.grid(column=1, row=10)
    txt10.insert(0, FPS)

    lbl11 = Label(window, text='WIDTH')
    lbl11.grid(column=0, row=11)

    txt11 = Entry(window, width=10)
    txt11.grid(column=1, row=11)
    txt11.insert(0, WIDTH)

    lbl12 = Label(window, text='HEIGHT')
    lbl12.grid(column=0, row=12)

    txt12 = Entry(window, width=10)
    txt12.grid(column=1, row=12)
    txt12.insert(0, HEIGHT)

    lbl13 = Label(window, text='Moves')
    lbl13.grid(column=0, row=13)

    txt13 = Entry(window, width=10)
    txt13.grid(column=1, row=13)
    txt13.insert(0, time)

    lbl13 = Label(window, text='Print every move')
    lbl13.grid(column=0, row=14)

    txt14 = Entry(window, width=10)
    txt14.grid(column=1, row=14)
    txt14.insert(0, print_always)

    btn1 = Button(window, text='  Apply  ', command=apply)
    btn1.grid(column=2, row=3)

    btn2 = Button(window, text=' Default ', command=default)
    btn2.grid(column=2, row=2)

    btn3 = Button(window, text='   New    ', command=new)
    btn3.grid(column=2, row=0)

    btn4 = Button(window, text='Simulate', command=begin1)
    btn4.grid(column=2, row=1)

    btn5 = Button(window, text='   Print   ', command=put_out)
    btn5.grid(column=2, row=4)

    btn6 = Button(window, text='  One move  ', command=one_move)
    btn6.grid(column=2, row=5)

    btn7 = Button(window, text='  Main menu  ', command=main_menu)
    btn7.grid(column=2, row=6)

    btn8 = Button(window, text='  Continue  ', command=begin)
    btn8.grid(column=2, row=7)

    btn9 = Button(window, text='Rename current replay', command=rename_replay)
    btn9.grid(column=2, row=8)

    lbl15 = Label(window, text='Skip showing position till move №')
    lbl15.grid(column=0, row=15)

    txt15 = Entry(window, width=10)
    txt15.grid(column=1, row=15)
    try:
        txt15.insert(0, crit_time)
    except:
        crit_time = 0
        txt15.insert(0, crit_time)

    btn15 = Button(window, text='  Skip  ', command=creet)
    btn15.grid(column=2, row=15)

    lbl16 = Label(window, text='Writing replays')
    lbl16.grid(column=0, row=16)

    txt16 = Entry(window, width=10)
    txt16.grid(column=1, row=16)
    txt16.insert(0, writing_replays)

    window.mainloop()


def ask_replay():
    global lbl0, txt0, lbl1, txt1, lbl2, txt2, lbl3, txt3
    global lbl4, txt4, lbl5, txt5, lbl6, txt6, lbl7, txt7
    global lbl8, txt8, lbl9, txt9, lbl10, txt10, lbl11
    global txt11, lbl12, txt12, lbl13, txt13, window, time
    global print_always, txt14, real_time, txt_skip, loading_replay

    begin()

    window = Tk()
    window.title('Management panel')

    w = window.winfo_screenwidth() - 300
    h = 0
    window.geometry('+{}+{}'.format(w, h))

    lbl8 = Label(window, text='length')
    lbl8.grid(column=0, row=0)

    txt8 = Entry(window, width=10)
    txt8.grid(column=1, row=0)
    txt8.insert(0, length)

    lbl9 = Label(window, text='width')
    lbl9.grid(column=0, row=1)

    txt9 = Entry(window, width=10)
    txt9.grid(column=1, row=1)
    txt9.insert(0, width)

    lbl10 = Label(window, text='FPS')
    lbl10.grid(column=0, row=2)

    txt10 = Entry(window, width=10)
    txt10.grid(column=1, row=2)
    txt10.insert(0, FPS)

    lbl11 = Label(window, text='WIDTH')
    lbl11.grid(column=0, row=3)

    txt11 = Entry(window, width=10)
    txt11.grid(column=1, row=3)
    txt11.insert(0, WIDTH)

    lbl12 = Label(window, text='HEIGHT')
    lbl12.grid(column=0, row=4)

    txt12 = Entry(window, width=10)
    txt12.grid(column=1, row=4)
    txt12.insert(0, HEIGHT)

    lbl13 = Label(window, text='Moves')
    lbl13.grid(column=0, row=5)

    txt13 = Entry(window, width=10)
    txt13.grid(column=1, row=5)
    txt13.insert(0, time)

    lbl13 = Label(window, text='Print every move')
    lbl13.grid(column=0, row=6)

    txt14 = Entry(window, width=10)
    txt14.grid(column=1, row=6)
    txt14.insert(0, print_always)

    btn1 = Button(window, text='  Apply  ', command=apply)
    btn1.grid(column=2, row=0)

    btn5 = Button(window, text='   Print   ', command=put_out)
    btn5.grid(column=2, row=1)

    btn6 = Button(window, text='  One move  ', command=one_move)
    btn6.grid(column=2, row=2)

    btn7 = Button(window, text='  Main menu  ', command=main_menu)
    btn7.grid(column=2, row=3)

    btn8 = Button(window, text='  Continue  ', command=begin)
    btn8.grid(column=2, row=4)

    btn9 = Button(window, text='Rename current replay', command=rename_replay)
    btn9.grid(column=2, row=5)

    txt_skip = Entry(window, width=10)
    txt_skip.grid(column=1, row=7)
    txt_skip.insert(0, real_time)

    btn_skip = Button(window, text='GOOOO', command=skip_and_GOOOO)
    btn_skip.grid(column=2, row=7)

    lbl_skip = Label(window, text='Go to this move')
    lbl_skip.grid(column=0, row=7)

    btn9 = Button(window, text='Load full replay', command=load_replay)
    btn9.grid(column=2, row=6)

    window.mainloop()


def start():
    global r0, d, h, dp, S_critical, StartAsabia, Imperial_Asabia
    global chance, length, width, FPS, WIDTH, HEIGHT
    global Empires, BigMap, clrs, Empiresq, lc, do
    global ki, kj, time, res, AllFields, DeltaFields
    global one_step, print_always, crit_time, name0, mode, writing_replays

    one_step = 0
    do = 1
    r0 = 0.2
    d = 0.1
    h = 2
    dp = 0.1
    S_critical = 0.003
    StartAsabia = 0.003
    Imperial_Asabia = 0.0035
    chance = 1
    print_always = 0
    length = 21
    width = 21

    FPS = 5
    WIDTH = 600  # ширина экрана
    HEIGHT = 600  # высота экрана

    clrs = []
    clrs += allcolors.AllColors
    lc = len(clrs)

    Empires = []
    Empiresq = [0]

    f = open('data/map.txt', 'r')

    nums = f.read().splitlines()

    length, width = map(int, nums[0].split())

    WIDTH = int(600 * length / 21)
    HEIGHT = int(600 * width / 21)

    BigMap = [[Field(r0, d, StartAsabia, h, dp, length, width, x, y, chance) for x in range(length)] for y in
              range(width)]

    for i in range(1, len(nums)):
        exec(nums[i])

    f.close

    for i in BigMap:
        for j in i:
            j.BigMapP = BigMap
            j.AllEmpires = Empires

    for i in Empires:
        i.pre_update()

    for i in BigMap:
        for j in i:
            j.pre_update()

    for i in Empires:
        i.update()

    ki = HEIGHT / width
    kj = WIDTH / length

    time = 0
    crittime = 0
    res = 0

    AllFields = []

    for i in range(width):
        for j in range(length):
            AllFields.append((i, j))

    DeltaFields = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    if mode == 'Launch' and writing_replays:
        name0 = 'v.C_' + str(datetime.datetime.isoformat(datetime.datetime.now(), sep='_'))[:-7].replace(':', '-')

        try:
            os.mkdir('Clyo_replays')
        except:
            time = 0

        f = open('Clyo_replays/' + name0 + '.txt', 'a')

        a0 = max(len(str(length)), len(str(width)))
        wres = str(a0) + '%' + reformat(length, a0) + reformat(width, a0)

        f.write(wres)
        f.close


print('''
By Victor.

So, to go to management panel press   SPACE
Being there, on your left you can see the variables, 
which values you can change. To save changes press   Apply  .
To set variables as default, press   Default  . To set 
variables like it is a new simulation with default 
values, press   New  . You also need to press Simulate
to begin/continue simulation. Press   Print   to get 
'the map' here. Press   One move   to simulate the next move
and immediately return to the management panel. To see Asabiyah
and status of the field, you shold tap on it.
For pause press   P  .

''')

while 1:
    print('''To go to management panel after starting,
press SPACE. Now give 'OK' to input and press ENTER''')
    if input() == 'OK':
        break
    else:
        print("Now give 'OK' to input and press ENTER")

mode = 'None'

first = True
last = True
Pause = False
writing_replays = True

start()

main_menu()

crit_time = 0
pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

sc.fill(allcolors.WHITE())

while 1:
    try:
        if not Pause:
            if mode == 'Launch':

                if writing_replays:
                    print_replay_C(BigMap, name0, StartAsabia)

                if print_always:
                    print_double_mas(BigMap)

                time += 1

                AllFields = random_queue(AllFields)
                DeltaFields = random_queue(DeltaFields)
                for f in AllFields:
                    j = BigMap[f[0]][f[1]]
                    for g in DeltaFields:
                        ii = g[0]
                        jj = g[1]
                        if 0 <= j.y + ii < width:
                            if 0 <= j.x + jj < length:
                                if abs(ii) + abs(jj) < 2:
                                    if BigMap[j.y][j.x].status == 'old_fag':
                                        if BigMap[j.y][j.x].Empire != 'Landscape' and \
                                                BigMap[j.y + ii][j.x + jj].Empire != 'Landscape':
                                            BigMap[j.y][j.x].attack(BigMap[j.y + ii][j.x + jj])

                for i in Empires:
                    i.pre_update()

                for i in BigMap:
                    for j in i:
                        if j.Empire != 'Landscape':
                            j.pre_update()
                            j.update()

                for i in Empires:
                    i.update()

                if time > crit_time:
                    for i in range(width):
                        for j in range(length):
                            if time - crit_time > 1:
                                if BigMap[i][j].Borders != 'Center':
                                    if BigMap[i][j].Empire != 'None':
                                        pygame.draw.rect(sc, clrs[BigMap[i][j].Empire.number % lc],
                                                         (round(j * kj), round(i * ki),
                                                          round(kj), round(ki)))
                                    else:
                                        pygame.draw.rect(sc, allcolors.WHITE(),
                                                         (round(j * kj), round(i * ki),
                                                          round(kj), round(ki)))
                                else:
                                    if BigMap[i][j].Empire == 'Landscape':
                                        pygame.draw.rect(sc, allcolors.BLACK(),
                                                         (round(j * kj), round(i * ki),
                                                          round(kj), round(ki)))
                                    elif BigMap[i][j].Empire != 'None':
                                        pygame.draw.rect(sc, clrs[BigMap[i][j].Empire.number % lc],
                                                         (round(j * kj), round(i * ki),
                                                          round(kj), round(ki)))
                                    else:
                                        pygame.draw.rect(sc, allcolors.WHITE(),
                                                         (round(j * kj), round(i * ki),
                                                          round(kj), round(ki)))

                    for i in range(length + 1):
                        k = round(i * WIDTH / length)
                        pygame.draw.line(sc, allcolors.BLACK(), (k, 0), (k, HEIGHT))

                    for i in range(width + 1):
                        k = round(i * HEIGHT / width)
                        pygame.draw.line(sc, allcolors.BLACK(), (0, k), (WIDTH, k))

            elif mode == 'Replay':

                if replay_version == 'B':
                    if first:
                        f = open('Clyo_replays/' + replay_name + '.txt', 'r')

                        s = f.read(6)
                        length, width = int(s[:3]), int(s[3:])

                        first = False
                        last = True
                        time = 0

                        CurrReplay = []
                        real_time = 1

                    if last:
                        try:
                            if real_time > time or time <= 1:
                                time = int(f.read(6))
                        except:
                            real_time += 1
                            last = False
                        finally:
                            try:
                                if real_time > time or time <= 1:
                                    BiggMapp = [[(int(f.read(3)), int(f.read(3)) / 100) for i in range(length)] for j in
                                                range(width)]
                                    CurrReplay.append(BiggMapp)
                                else:
                                    BiggMapp = CurrReplay[real_time - 1]
                            except:
                                last = False
                            finally:
                                real_time += 1
                                if not loading_replay:
                                    for i in range(width):
                                        for j in range(length):
                                            if BiggMapp[i][j][0] == 998:
                                                pygame.draw.rect(sc, allcolors.BLACK(),
                                                                 (round(j * kj), round(i * ki),
                                                                  round((j + 1) * kj), round((i + 1) * ki)))
                                            elif BiggMapp[i][j][0] != 999:
                                                pygame.draw.rect(sc, clrs[BiggMapp[i][j][0] % lc],
                                                                 (round(j * kj), round(i * ki),
                                                                  round((j + 1) * kj), round((i + 1) * ki)))
                                            else:
                                                pygame.draw.rect(sc, allcolors.WHITE(),
                                                                 (round(j * kj), round(i * ki),
                                                                  round((j + 1) * kj), round((i + 1) * ki)))

                                for i in range(length + 1):
                                    k = round(i * WIDTH / length)
                                    pygame.draw.line(sc, allcolors.BLACK(), (k, 0), (k, HEIGHT))

                                for i in range(width + 1):
                                    k = round(i * HEIGHT / width)
                                    pygame.draw.line(sc, allcolors.BLACK(), (0, k), (WIDTH, k))

                elif replay_version == 'C':
                    if first:
                        f = open('Clyo_replays/' + replay_name + '.txt', 'r')

                        s = f.read(1)
                        while s[-1] != '%':
                            s += f.read(1)
                        s = int(s[:-1])
                        length, width = int(f.read(s)), int(f.read(s))

                        first = False
                        last = True
                        time = 0
                        encode = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'z', 'o', 'S']

                        CurrReplay = []
                        real_time = 1

                    if last:

                        try:
                            if real_time > time or time <= 1:
                                BiggMapp = []
                                for i in range(width):
                                    BiggMapp.append([])
                                    for j in range(length):
                                        s = f.read(2)

                                        while s[-1] not in encode:
                                            s += f.read(1)

                                        m = s[-1]
                                        imp = s[:-1]

                                        if m == 'z':
                                            ass = '00'
                                        elif m == 'o':
                                            ass = '10'
                                        elif m == 'S':
                                            ass = StartAsabia
                                        else:
                                            m = encode.index(m)
                                            ass = (f.read(m))

                                        BiggMapp[-1].append((imp, ass))

                                CurrReplay.append(BiggMapp)
                            else:
                                BiggMapp = CurrReplay[real_time - 1]
                        except:
                            last = False
                            last = True
                        finally:
                            real_time += 1
                            time = len(CurrReplay)
                            try:
                                qqqq = BiggMapp[length - 1][width - 1][0]
                            except:
                                loading_replay = 0
                            if not loading_replay:
                                for i in range(width):
                                    for j in range(length):
                                        try:
                                            if BiggMapp[i][j][0] == 'l':
                                                pygame.draw.rect(sc, allcolors.BLACK(),
                                                                 (round(j * kj), round(i * ki),
                                                                  round((j + 1) * kj), round((i + 1) * ki)))
                                            elif BiggMapp[i][j][0] != 'n':
                                                pygame.draw.rect(sc, clrs[int(BiggMapp[i][j][0]) % lc],
                                                                 (round(j * kj), round(i * ki),
                                                                  round((j + 1) * kj), round((i + 1) * ki)))
                                            else:
                                                pygame.draw.rect(sc, allcolors.WHITE(),
                                                                 (round(j * kj), round(i * ki),
                                                                  round((j + 1) * kj), round((i + 1) * ki)))
                                        except:
                                            kkkkk = 1
                                        finally:
                                            kkkkk = 0
                            for i in range(length + 1):
                                k = round(i * WIDTH / length)
                                pygame.draw.line(sc, allcolors.BLACK(), (k, 0), (k, HEIGHT))

                            for i in range(width + 1):
                                k = round(i * HEIGHT / width)
                                pygame.draw.line(sc, allcolors.BLACK(), (0, k), (WIDTH, k))
    except:
        errwindow()
    finally:
        pygame.display.update()

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_SPACE:
                if mode == 'Launch':
                    ask()
                elif mode == 'Replay':
                    ask_replay()
                elif mode == 'None':
                    main_menu()
            elif i.key == pygame.K_p:
                if Pause:
                    Pause = False
                else:
                    Pause = True
        elif one_step:
            one_step = 0
            if mode == 'Launch':
                ask()
            elif mode == 'Replay':
                ask_replay()
            break
        elif i.type == pygame.MOUSEBUTTONDOWN:
            if i.type == 1 or 1:
                if mode == 'Launch':
                    print_asabia(i.pos)
                elif mode == 'Replay':
                    print_asabia_replay(i.pos)

    clock.tick(FPS)
