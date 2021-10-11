import datetime
import os

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import allcolors
from coms import *
from graph import *
from math import *
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtCore import QSize


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.default_path = 'data/map.txt'
        self.path = self.default_path
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 1350, 670)
        self.setWindowTitle('Clyodynamics simulator')

        self.qw = Example(self)
        self.setCentralWidget(self.qw)

        self.statusBar()
        self.statusBar().showMessage('Добро пожаловать!')
        # self.do_buttons()
        # self.Watch_replay()

        self.show()

        self.qw.mousePressEvent = self.getPos

        self.def_actions()
        self.do_menubar()

    def getPos(self, event):
        try:
            x = event.pos().x()
            y = event.pos().y()
            # print('OK')
            if self.qw.mode == 'Replay' or self.qw.mode == 'Launch':
                self.print_Asabia(x, y)
            elif self.qw.mode == 'Environment':
                if event.button() == Qt.LeftButton:
                    print(self.qw.PaintMode[self.qw.cur])
                    if self.qw.PaintMode[self.qw.cur] == 'Point':
                        self.ChangeField(x, y, 'coo')
                    elif self.qw.PaintMode[self.qw.cur] == 'Line':
                        try:
                            i = int(y // self.qw.ki)
                            j = int(x // self.qw.kj)
                        except:
                            print('not ok')
                        finally:
                            if self.qw.step:
                                self.qw.step = 0

                                x1, y1 = self.qw.mem[0], self.qw.mem[1]

                                i = int(y // self.qw.ki)
                                j = int(x // self.qw.kj)
                                i1 = int(y1 // self.qw.ki)
                                j1 = int(x1 // self.qw.kj)

                                if i == i1:
                                    if j > j1:
                                        for ij in range(j1, j + 1):
                                            self.ChangeField(i, ij, 'index')
                                    else:
                                        for ij in range(j, j1 + 1):
                                            self.ChangeField(i, ij, 'index')
                                elif j == j1:
                                    if i > i1:
                                        for ij in range(i1, i + 1):
                                            self.ChangeField(ij, j, 'index')
                                    else:
                                        for ij in range(i, i1 + 1):
                                            self.ChangeField(ij, j, 'index')

                                self.qw.mem = []

                            else:
                                self.qw.step = 1

                                self.qw.mem.append(x)
                                self.qw.mem.append(y)
                    elif self.qw.PaintMode[self.qw.cur] == 'Rect':
                        try:
                            i = int(y // self.qw.ki)
                            j = int(x // self.qw.kj)
                        except:
                            print('nnot ok')
                        finally:
                            if self.qw.step:
                                self.qw.step = 0

                                x1, y1 = self.qw.mem[0], self.qw.mem[1]

                                i = int(y // self.qw.ki)
                                j = int(x // self.qw.kj)
                                i1 = int(y1 // self.qw.ki)
                                j1 = int(x1 // self.qw.kj)

                                i, i1 = min(i, i1), max(i, i1)
                                j, j1 = min(j, j1), max(j, j1)

                                for _ in range(i, i1 + 1):
                                    for __ in range(j, j1 + 1):
                                        self.ChangeField(_, __, 'index')

                                self.qw.mem = []

                            else:
                                self.qw.step = 1

                                self.qw.mem.append(x)
                                self.qw.mem.append(y)
                else:
                    self.qw.cur += 1
                    self.qw.mem = []
                    self.qw.step = 0
                    self.qw.cur %= 3
        except:
            print('WTF')

    def ChangeField(self, x, y, mode):
        if mode == 'coo':
            # print(x, y, self.qw.EnvChangeMode)
            try:
                if self.qw.EnvChangeMode == 'Landscape':
                    i = int(y // self.qw.ki)
                    j = int(x // self.qw.kj)
                    xx, yy = i, j
                    # print(xx, yy)
                    # print('OK')
                    r'''
                    f = open('data/map.txt', 'a')
                    if str(self.qw.BigMap[i][j].Empire) != 'Landscape':
                        f.write('\n' + 'self.BigMap[' + str(i) + '][' + str(j) + "].Empire = 'Landscape'")
                    else:
                        f.write('\n' + 'self.BigMap[' + str(i) + '][' + str(j) + "].Empire = 'None'")
                    f.close()'''
                    mas = read_envi(self.path)
                    # print(mas, xx, yy)
                    for _ in range(len(mas)):
                        # print(_, 'hh')
                        if mas[_][0] == 'Lan':
                            mas[_].append(xx)
                            mas[_].append(yy)
                            # print('OK')
                        elif mas[_][0] == 'Emp':
                            quan = len(mas[_]) // 2 - 1
                            # print(len(mas[_]) - 1, 3 + 2 * (quan-1))
                            for __ in range(quan):
                                if mas[_][2 + 2 * __] == xx:
                                    if mas[_][3 + 2 * __] == yy:
                                        # print(mas[_])
                                        del mas[_][2 + 2 * __]
                                        del mas[_][2 + 2 * __]
                                        # print(mas[_])
                                        break

                elif self.qw.EnvChangeMode == 'None':
                    i = int(y // self.qw.ki)
                    j = int(x // self.qw.kj)
                    xx, yy = i, j
                    mas = read_envi(self.path)

                    for _ in range(len(mas)):

                        # print(mas[_][0])
                        if mas[_][0] == 'Emp':
                            quan = len(mas[_]) // 2 - 1
                            for __ in range(quan):
                                if mas[_][2 + 2 * __] == xx:
                                    if mas[_][3 + 2 * __] == yy:
                                        del mas[_][2 + 2 * __]
                                        del mas[_][2 + 2 * __]
                                        break
                        elif mas[_][0] == 'Lan':
                            # print('ok)')
                            quan = (len(mas[_]) - 1) // 2
                            for __ in range(quan):
                                # print('HELLO THERE')
                                if mas[_][1 + 2 * __] == xx:
                                    if mas[_][2 + 2 * __] == yy:
                                        # print('hi there')
                                        del mas[_][1 + 2 * __]
                                        del mas[_][1 + 2 * __]
                                        break

                elif self.qw.EnvChangeMode.split()[0] == 'Empire':
                    empire_number = int(self.qw.EnvChangeMode.split()[1])

                    i = int(y // self.qw.ki)
                    j = int(x // self.qw.kj)
                    xx, yy = i, j

                    self.qw.EnvChangeMode = 'None'
                    self.ChangeField(x, y, 'coo')
                    self.qw.EnvChangeMode = 'Empire ' + str(empire_number)

                    mas = read_envi(self.path)
                    mas[2 + empire_number].append(xx)
                    mas[2 + empire_number].append(yy)

                elif self.qw.EnvChangeMode == 'Add empire':

                    #print('ok')
                    i = int(y // self.qw.ki)
                    j = int(x // self.qw.kj)
                    xx, yy = i, j

                    self.qw.EnvChangeMode = 'None'
                    self.ChangeField(x, y, 'coo')
                    self.qw.EnvChangeMode = 'Add empire'

                    #print('OKOK')

                    mas = read_envi(self.path)
                    if self.qw.PaintMode[self.qw.cur] == 'Point':
                        mas.append(['Emp', self.qw.Imperial_Asabia, xx, yy])

                    #print(mas)

                else:
                    print(self.qw.EnvChangeMode, self.qw.Empiresq)

                write_envi(self.path, mas)


            except:
                x = x
            finally:
                y = y
        elif mode == 'index':
            self.ChangeField(y * self.qw.ki + 1, x * self.qw.kj + 1, 'coo')
        elif mode == 'indexx':
            i, j = x, y
            f = open(self.path, 'a')
            if str(self.qw.BigMap[i][j].Empire) != 'Landscape':
                f.write('\n' + 'self.BigMap[' + str(i) + '][' + str(j) + "].Empire = 'Landscape'")
            else:
                f.write('\n' + 'self.BigMap[' + str(i) + '][' + str(j) + "].Empire = 'None'")
            f.close()

    def print_Asabia(self, x, y):

        try:
            i = int(y // self.qw.ki)
            j = int(x // self.qw.kj)
        except:
            return 'Cursor outside of the field'
        finally:
            if self.qw.mode == 'Launch':
                print(self.qw.BigMap[i][j].Asabia)

    def do_menubar(self):

        self.menubar = self.menuBar()

        self.openreplayMenu = QMenu('&Open as')
        self.openreplayMenu.addAction(self.asBAction)
        self.openreplayMenu.addAction(self.asCAction)

        self.fileMenu = self.menubar.addMenu('&File')
        self.fileMenu.addAction(self.exitAction)
        self.fileMenu.addAction(self.saveasAction)

        self.mainMenu = self.menubar.addMenu('&Main menu')
        self.mainMenu.addAction(self.startAction)

        self.settingsMenu = self.menubar.addMenu('&Settings')
        self.settingsMenu.addAction(self.changeAction)
        self.settingsMenu.addAction(self.additionalAction)

        self.replayMenu = self.menubar.addMenu('&Replays')
        self.replayMenu.addAction(self.openAction)
        self.replayMenu.addMenu(self.openreplayMenu)

        self.environmentMenu = self.menubar.addMenu('&Environment')
        self.environmentMenu.addAction(self.ChangeEnvAction)
        self.environmentMenu.addAction(self.OpenEnvAction)
        self.environmentMenu.addAction(self.DefaultEnvAction)
        '''

        saveAction = QAction(QIcon('pics/save.png'), '&Save', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.setStatusTip('Сохранить изменения')
        saveAction.triggered.connect(save)

        searchAction = QAction(QIcon('pics/search.png'), '&Search', self)
        searchAction.setShortcut('Ctrl+F')
        searchAction.setStatusTip('Искать')
        searchAction.triggered.connect(self.searchDialog)

        addAction = QAction(QIcon('pics/add.png'), '&Add', self)
        addAction.setShortcut('Ctrl+A')
        addAction.setStatusTip('Добавить произведение')
        addAction.triggered.connect(self.addDialog)

        caddAction = QAction(QIcon('pics/cadd.png'), '&Cadd', self)
        caddAction.setShortcut('Ctrl+J')
        caddAction.setStatusTip('Добавить произведение в последнюю книгу')
        caddAction.triggered.connect(self.caddDialog)

        naddAction = QAction(QIcon('pics/nadd.png'), '&Nadd', self)
        naddAction.setShortcut('Ctrl+N')
        naddAction.setStatusTip('Добавить произведение в книгу с выбранным номером')
        naddAction.triggered.connect(self.naddDialog)

        scacheAction = QAction(QIcon('pics/scache.png'), '&Show cache', self)
        scacheAction.setStatusTip('Показать кэш')
        scacheAction.triggered.connect(self.scDialog)

        ccacheAction = QAction(QIcon('pics/ccache.png'), '&Clear cache', self)
        ccacheAction.setStatusTip('Очиистить кэш')
        ccacheAction.triggered.connect(clearcache)

        sallAction = QAction(QIcon('pics/sall.png'), '&Show base', self)
        sallAction.setStatusTip('Показать базу книг')
        sallAction.triggered.connect(self.saDialog)

        callAction = QAction(QIcon('pics/call.png'), '&Clear base', self)
        callAction.setStatusTip('Очистить базу книг')
        callAction.triggered.connect(clearall)

        helAction = QAction(QIcon('pics/hel.png'), '&Show file', self)
        helAction.setStatusTip('Показать вспомогательный файл')
        helAction.triggered.connect(self.helDialog)

        undoAction = QAction(QIcon('pics/undo.png'), '&Undo', self)
        undoAction.setStatusTip('Отменить последнее действие')
        undoAction.setShortcut('Ctrl+Z')
        undoAction.triggered.connect(self.unDialog)

        redoAction = QAction(QIcon('pics/redo.png'), '&Redo', self)
        redoAction.setStatusTip('Повторить отменённое действие')
        redoAction.setShortcut('Ctrl+Shift+Z')
        # redoAction.triggered.connect(self.reDialog)

        deleteAction = QAction(QIcon('pics/del.png'), '&Delete', self)
        deleteAction.setStatusTip('Удалить книгу')
        deleteAction.setShortcut('Ctrl+delete')
        deleteAction.triggered.connect(self.delDialog)

        changeAction = QAction(QIcon('pics/change.png'), '&Change', self)
        changeAction.setShortcut('Ctrl+R')
        changeAction.setStatusTip('Изменить произведение')
        changeAction.triggered.connect(self.chaDialog)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)
        self.toolbar = self.addToolBar('Search')
        self.toolbar.addAction(searchAction)
        self.toolbar = self.addToolBar('Add')
        self.toolbar.addAction(addAction)
        self.toolbar = self.addToolBar('Delete')
        self.toolbar.addAction(deleteAction)
        self.toolbar = self.addToolBar('Change')
        self.toolbar.addAction(changeAction)

        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)

        menubar = self.menuBar()

        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        fileMenu.addAction(undoAction)
        fileMenu.addAction(redoAction)
        fileMenu.addAction(saveAction)

        addMenu = menubar.addMenu('&Add')
        addMenu.addAction(addAction)
        addMenu.addAction(caddAction)
        addMenu.addAction(naddAction)

        settMenu = menubar.addMenu('&Special Settings')
        settMenu.addAction(scacheAction)
        settMenu.addAction(ccacheAction)
        settMenu.addAction(sallAction)
        settMenu.addAction(callAction)
        settMenu.addAction(helAction)

        self.statusBar()
        self.statusBar().showMessage('Добро пожаловать!')'''

    def def_actions(self):
        self.exitAction = QAction(QIcon('pics/exit.png'), '&Save and exit', self)
        self.exitAction.setShortcut('Ctrl+Q')
        self.exitAction.setStatusTip('Выйти')
        self.exitAction.triggered.connect(self.exitDialog)

        self.startAction = QAction(QIcon('pics/start.png'), '&Simulate with default parameters', self)
        self.startAction.setShortcut('Ctrl+D')
        self.startAction.setStatusTip('Тут пока не доделана подсказка')
        self.startAction.triggered.connect(self.Simulate_default)

        self.saveasAction = QAction(QIcon('pics/saveas.png'), '&Save replay as', self)
        self.saveasAction.setShortcut('Ctrl+Shift+S')
        self.saveasAction.setStatusTip('Тут пока не доделана подсказка')

        self.openAction = QAction(QIcon('pics/open.png'), '&Open', self)
        self.openAction.setShortcut('Ctrl+O')
        self.openAction.setStatusTip('Тут пока не доделана подсказка')
        self.openAction.triggered.connect(self.Watch_replay)

        self.changeAction = QAction(QIcon('pics/change.png'), '&Change variables', self)
        #self.changeAction.setShortcut('Ctrl+E')
        self.changeAction.setStatusTip('Тут пока не доделана подсказка')

        self.additionalAction = QAction(QIcon('pics/additional.png'), '&Other options', self)
        self.additionalAction.setShortcut('Ctrl+Shift+E')
        self.additionalAction.setStatusTip('Тут пока не доделана подсказка')

        self.asBAction = QAction(QIcon('pics/asB.png'), '&Open format B', self)
        # self.asBAction.setShortcut('Ctrl+Shift+E')
        self.asBAction.setStatusTip('Тут пока не доделана подсказка')
        self.asBAction.triggered.connect(self.Watch_B)

        self.asCAction = QAction(QIcon('pics/asC.png'), '&Open format C', self)
        # self.asCAction.setShortcut('Ctrl+Shift+E')
        self.asCAction.setStatusTip('Тут пока не доделана подсказка')
        self.asCAction.triggered.connect(self.Watch_C)

        self.ChangeEnvAction = QAction(QIcon('pics/ChangeEnv.png'), '&Change current environment', self)
        self.ChangeEnvAction.setShortcut('Ctrl+E')
        self.ChangeEnvAction.setStatusTip('Тут пока не доделана подсказка')
        self.ChangeEnvAction.triggered.connect(self.ChangeEnv)

        self.OpenEnvAction = QAction(QIcon('pics/OpenEnv.png'), '&Open environment', self)
        #self.OpenEnvAction.setShortcut('Ctrl+E')
        self.OpenEnvAction.setStatusTip('Тут пока не доделана подсказка')
        self.OpenEnvAction.triggered.connect(self.OpenEnv)

        self.DefaultEnvAction = QAction(QIcon('pics/DefaultEnv.png'), '&Open default environment', self)
        #self.asCAction.setShortcut('Ctrl+E')
        self.DefaultEnvAction.setStatusTip('Тут пока не доделана подсказка')
        self.DefaultEnvAction.triggered.connect(self.DefaultEnv)

    def OpenEnv(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
        self.path = fname

    def DefaultEnv(self):
        self.path = self.default_path

    def ChangeEnv(self):
        self.qw.mode = 'Environment'
        self.oppa = Envi(self.qw, len(read_envi(self.path)) - 2)

    def Simulate_default(self):

        self.qw.mode = 'Launch'
        self.qw.start('start')
        # self.qw.Pause = True

    def exitDialog(self):
        self.close()

    def Watch_replay(self):

        self.qw.ReplayMode = 'Short'
        self.rep = Replay(self.qw)

    def Watch_B(self):
        self.qw.ReplayMode = 'Long'
        self.qw.replay_version = 'B'
        self.qw.mode = 'Replay'
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
        self.qw.replay_name = fname

    def Watch_C(self):

        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
        self.qw.replay_name = fname
        self.qw.ReplayMode = 'Long'
        self.qw.replay_version = 'C'
        self.qw.mode = 'Replay'

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_P:
            if self.qw.Pause:
                self.qw.Pause = False
            else:
                self.qw.Pause = True
        # elif event.key() == Qt.Key_E:
        # self.qw.mode = 'Environment'
        event.accept()


class Example(QWidget):

    def __init__(self, host):
        super().__init__()

        self.host = host
        self.initUI()

    def initUI(self):
        self.text = u'uu'
        self.i = 0
        self.speed = 1

        self.cur = 0
        self.step = 0
        self.mem = []

        self.mode = 'None'
        self.writing_replays = True

        self.start('start')
        self.do_buttons()
        self.timer = QBasicTimer()
        self.timer.start(int(1000 / self.FPS), self)

        self.setGeometry(0, 0, self.WIDTH, self.HEIGHT)
        self.setWindowTitle('Draw text')
        self.show()

    def paintEvent(self, event):

        qp = QPainter()
        qp.begin(self)
        clr = allcolors.BLACK()
        qp.setPen(QColor(clr[0], clr[1], clr[2]))
        self.drawText(qp)

        if self.mode == 'Launch':
            self.host.statusBar().showMessage(str(self.time))
        elif self.mode == 'Environment':
            self.host.statusBar().showMessage(str(self.PaintMode[self.cur]))
        # qp.end()

    def drawText(self, qp):

        if self.mode == 'Launch':

            if self.writing_replays:
                print_replay_C(self.BigMap, self.name0, self.StartAsabia)

            if self.print_always:
                print_double_mas(self.BigMap)

            self.time += 1

            self.AllFields = random_queue(self.AllFields)
            self.DeltaFields = random_queue(self.DeltaFields)

            for f in self.AllFields:
                j = self.BigMap[f[0]][f[1]]
                for g in self.DeltaFields:
                    ii = g[0]
                    jj = g[1]
                    if 0 <= j.y + ii < self.width:
                        if 0 <= j.x + jj < self.length:
                            if abs(ii) + abs(jj) < 2:
                                if self.BigMap[j.y][j.x].status == 'old_fag':
                                    if self.BigMap[j.y][j.x].Empire != 'Landscape' and \
                                            self.BigMap[j.y + ii][j.x + jj].Empire != 'Landscape':
                                        self.BigMap[j.y][j.x].attack(self.BigMap[j.y + ii][j.x + jj])

            for i in self.Empires:
                i.pre_update()

            for i in self.BigMap:
                for j in i:
                    if j.Empire != 'Landscape':
                        j.pre_update()
                        j.update()

            for i in self.Empires:
                i.update()

            if 1 or self.time > self.crit_time:
                for i in range(self.width):
                    for j in range(self.length):
                        if 1 or self.BigMap[i][j].Borders != 'Center' or self.time <= 2:
                            if self.BigMap[i][j].Empire == 'Landscape':
                                clr = allcolors.BLACK()
                            elif self.BigMap[i][j].Empire != 'None':
                                clr = self.clrs[self.BigMap[i][j].Empire.number % self.lc]
                            else:
                                clr = allcolors.WHITE()
                            qp.setBrush(QColor(clr[0], clr[1], clr[2]))
                            qp.drawRect(round(j * self.kj), round(i * self.ki), round(self.kj), round(self.ki))

        elif self.mode == 'Replay':

            if self.replay_version == 'B':
                if self.first:

                    if self.ReplayMode == 'Short':
                        f = open('Clyo_replays/' + self.replay_name + '.txt', 'r')
                    elif self.ReplayMode == 'Long':
                        f = open(self.replay_name, 'r')

                    s = f.read(6)
                    self.length, self.width = int(s[:3]), int(s[3:])

                    self.first = False
                    self.last = True
                    self.time = 0

                    self.CurrReplay = []
                    self.real_time = 1

                if self.last and not self.Pause:
                    try:
                        if self.real_time > self.time or self.time <= 1:
                            self.time = int(f.read(6))
                    except:
                        self.real_time += 1
                        self.last = False
                    finally:
                        try:
                            if self.real_time > self.time or self.time <= 1:
                                self.BiggMapp = [[(int(f.read(3)), int(f.read(3)) / 100) for i in range(self.length)]
                                                 for j in
                                                 range(self.width)]
                                self.CurrReplay.append(self.BiggMapp)
                            else:
                                self.BiggMapp = self.CurrReplay[self.real_time - 1]
                        except:
                            self.last = False
                        finally:
                            self.real_time += 1
                            if not self.loading_replay:
                                for i in range(self.width):
                                    for j in range(self.length):
                                        if self.BiggMapp[i][j][0] == 998:
                                            clr = allcolors.BLACK()
                                        elif self.BiggMapp[i][j][0] != 999:
                                            clr = self.clrs[self.BigMap[i][j].Empire.number % self.lc]
                                        else:
                                            clr = allcolors.WHITE()
                                        qp.setBrush(QColor(clr[0], clr[1], clr[2]))
                                        qp.drawRect(round(j * self.kj), round(i * self.ki), round(self.kj),
                                                    round(self.ki))


            elif self.replay_version == 'C':
                if self.first:

                    if self.ReplayMode == 'Short':
                        self.f = open('Clyo_replays/' + self.replay_name + '.txt', 'r')
                    elif self.ReplayMode == 'Long':
                        self.f = open(self.replay_name, 'r')

                    s = self.f.read(1)
                    while s[-1] != '%':
                        s += self.f.read(1)
                    s = int(s[:-1])
                    self.length, self.width = int(self.f.read(s)), int(self.f.read(s))

                    self.first = False
                    self.last = True
                    self.time = 0
                    self.encode = ['a', 'b', 'c',
                                   'd', 'e', 'f',
                                   'g', 'h', 'i',
                                   'k', 'l', 'z',
                                   'o', 'S']

                    self.CurrReplay = []
                    self.real_time = 1

                if self.last and not self.Pause:

                    try:
                        if self.real_time > self.time or self.time <= 1:
                            self.BiggMapp = []

                            for i in range(self.width):

                                self.BiggMapp.append([])
                                for j in range(self.length):
                                    s = self.f.read(2)

                                    while s[-1] not in self.encode:
                                        s += self.f.read(1)

                                    m = s[-1]
                                    imp = s[:-1]

                                    if m == 'z':
                                        ass = '00'
                                    elif m == 'o':
                                        ass = '10'
                                    elif m == 'S':
                                        ass = self.StartAsabia
                                    else:
                                        m = self.encode.index(m)
                                        ass = (self.f.read(m))

                                    # print(self.real_time)

                                    self.BiggMapp[-1].append((imp, ass))
                                    # print('OK assir')

                            self.CurrReplay.append(self.BiggMapp)
                        else:
                            self.BiggMapp = self.CurrReplay[self.real_time - 1]
                    except:
                        self.last = False
                        self.last = True

                    finally:
                        self.real_time += 1
                        self.time = len(self.CurrReplay)
                        try:
                            qqqq = self.BiggMapp[self.length - 1][self.width - 1][0]
                        except:
                            self.loading_replay = 0
                        print(self.BiggMapp)
                        if not self.loading_replay:
                            for i in range(self.width):
                                for j in range(self.length):
                                    try:
                                        if self.BiggMapp[i][j][0] == 'l':
                                            clr = allcolors.BLACK()
                                        elif self.BiggMapp[i][j][0] != 'n':
                                            # print('hm?, i, j')
                                            # clr = self.clrs[self.BigMap[i][j].Empire.number % self.lc]
                                            clr = self.clrs[int(self.BiggMapp[i][j][0]) % self.lc]
                                            # print('hell yeah')
                                        else:
                                            clr = allcolors.WHITE()

                                        qp.setBrush(QColor(clr[0], clr[1], clr[2]))
                                        qp.drawRect(round(j * self.kj), round(i * self.ki), round(self.kj),
                                                    round(self.ki))

                                    except:
                                        kkkkk = 1
                                        # print('FCNERROR')
                                    finally:
                                        kkkkk = 0

        elif self.mode == 'Environment':
            self.start('start')

            for i in range(self.width):
                for j in range(self.length):
                    if self.BigMap[i][j].Borders != 'Center' or self.time <= 2:
                        if self.BigMap[i][j].Empire == 'Landscape':
                            clr = allcolors.BLACK()
                        elif self.BigMap[i][j].Empire != 'None':
                            clr = self.clrs[self.BigMap[i][j].Empire.number % self.lc]
                        else:
                            clr = allcolors.WHITE()
                        qp.setBrush(QColor(clr[0], clr[1], clr[2]))
                        qp.drawRect(round(j * self.kj), round(i * self.ki), round(self.kj), round(self.ki))

    def timerEvent(self, event):
        if not self.Pause:
            self.update()

    def start(self, parameter):

        if parameter == 'start':
            self.one_step = 0
            self.do = 1
            self.r0 = 0.2
            self.d = 0.1
            self.h = 2
            self.dp = 0.1
            self.S_critical = 0.003
            self.StartAsabia = 0.003
            self.Imperial_Asabia = 0.0035
            self.chance = 1
            self.print_always = 0
            self.length = 65
            self.width = 31

            self.FPS = 5
            self.WIDTH = 600  # ширина экрана
            self.HEIGHT = 600  # высота экрана

        self.PaintMode = ['Point', 'Line', 'Rect']

        self.clrs = []
        self.clrs += allcolors.AllColors
        self.lc = len(self.clrs)

        self.first = 1
        self.last = 1
        self.loading_replay = 0
        self.ReplayMode = 'None'
        
        self.Empires = []
        self.Empiresq = [0]

        Mas = read_var(r'data\var.txt')

        for i in Mas:
            exec(i)

        if self.mode != 'Replay':

            mas = read_envi(self.host.path)

            for i in mas:
                if i[0] == 'Par':
                    self.length, self.width = i[1], i[2]

                    self.WIDTH = int(350 * self.length / 21)
                    self.HEIGHT = int(350 * self.width / 21)

                    self.BigMap = [[Field(self.r0, self.d, self.StartAsabia, self.h,
                                          self.dp, self.length, self.width, x, y,
                                          self.chance) for x in range(self.length)] for y in range(self.width)]
                elif i[0] == 'Lan':

                    quan = len(i) - 1

                    for j in range(quan // 2):
                        x, y = i[1 + 2 * j], i[2 + 2 * j]
                        self.BigMap[x][y].Empire = 'Landscape'
                elif i[0] == 'Emp':

                    # self.Empires.append(Empire(self.Imperial_Asabia, self.Empiresq, self.S_critical, self.BigMap[10][10], self.BigMap[10][11], self.BigMap[11][10], self.BigMap[11][11]))

                    asabia = i[1]
                    quan = len(i) - 2

                    s = 'self.Empires.append(Empire(asabia, self.Empiresq, self.S_critical'

                    for j in range(quan // 2):
                        ds = ', self.BigMap['
                        ds += str(i[2 + 2 * j])
                        ds += ']['
                        ds += str(i[3 + 2 * j])
                        ds += ']'
                        s += ds

                    s += '))'
                    exec(s)

        else:
            self.WIDTH = int(350 * self.length / 21)
            self.HEIGHT = int(350 * self.width / 21)

            self.BigMap = [[Field(self.r0, self.d, self.StartAsabia, self.h,
                                  self.dp, self.length, self.width, x, y,
                                  self.chance) for x in range(self.length)] for y in range(self.width)]

        for i in self.BigMap:
            for j in i:
                j.BigMapP = self.BigMap
                j.AllEmpires = self.Empires

        for i in self.Empires:
            i.pre_update()

        for i in self.BigMap:
            for j in i:
                j.pre_update()

        for i in self.Empires:
            i.update()

        self.ki = self.HEIGHT / self.width
        self.kj = self.WIDTH / self.length

        self.time = 0
        self.crittime = 0
        self.res = 0

        self.AllFields = []

        for i in range(self.width):
            for j in range(self.length):
                self.AllFields.append((i, j))

        self.DeltaFields = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # self.mode = 'Launch'
        # self.writing_replays = True
        self.Pause = False

        if self.mode == 'Launch' and self.writing_replays:
            self.name0 = 'v.C_' + str(datetime.datetime.isoformat(datetime.datetime.now(), sep='_'))[:-7].replace(':',
                                                                                                                  '-')

            try:
                os.mkdir('Clyo_replays')
            except:
                time = 0

            f = open('Clyo_replays/' + self.name0 + '.txt', 'a')

            a0 = max(len(str(self.length)), len(str(self.width)))
            wres = str(a0) + '%' + reformat(self.length, a0) + reformat(self.width, a0)

            f.write(wres)
            f.close

    def do_buttons(self):
        self.pause_button = QPushButton(QIcon('pics/pause.png'), '', self)
        self.pause_button.setToolTip('<b>Stop</b>')
        self.pause_button.resize(self.pause_button.sizeHint())
        self.pause_button.move(self.WIDTH + 100, 0)
        self.pause_button.clicked.connect(self.do_Pause)

        self.play_button = QPushButton(QIcon('pics/play.png'), '', self)
        self.play_button.setToolTip('<b>Start/Continue</b>')
        self.play_button.resize(self.play_button.sizeHint())
        self.play_button.move(self.WIDTH + 50, 0)
        self.play_button.clicked.connect(self.do_Play)

    def do_Pause(self):
        self.Pause = 1

    def do_Play(self):
        self.Pause = 0

    def read_Environment(self):
        with open(r'data\nmap.txt', 'r') as f:
            mas = [i.split() for i in f.read().splitlines()]


class Replay(QWidget):

    def __init__(self, qw):
        super().__init__()

        self.initUI()
        self.qw = qw

    def initUI(self):
        self.lbl1 = QLabel("Choose the replay format", self)
        self.lbl2 = QLabel("Type the name of the replay", self)

        self.txt = QLineEdit(self)

        self.combo = QComboBox(self)
        self.combo.addItems(['B', 'C'])

        self.btn = QPushButton('    Ok    ', self)

        self.combo.move(180, 18)
        self.lbl1.move(30, 20)
        self.lbl2.move(30, 45)
        self.txt.move(180, 45)
        self.btn.move(130, 80)

        self.combo.activated[str].connect(self.onActivated)
        self.txt.textChanged[str].connect(self.onChanged)
        self.btn.clicked.connect(self.onClose)

        self.setGeometry(300, 300, 320, 110)
        self.setWindowTitle('QComboBox')
        self.show()

    def onActivated(self, text):
        self.qw.replay_version = text
        # print(self.qw.replay_version)

    def onChanged(self, text):
        self.qw.replay_name = text
        # print(self.qw.replay_name)

    def onClose(self):
        self.qw.mode = 'Replay'
        self.qw.start('start')

        self.close()


class Envi(QWidget):

    def __init__(self, qw, number):
        super().__init__()

        self.mas = ['...', 'Add empire', 'None', 'Landscape']
        for i in range(number):
            self.mas.append('Empire ' + str(i))

        self.qw = qw

        self.initUI()

    def initUI(self):
        self.lbl1 = QLabel("The type of edited field", self)
        self.lbl2 = QLabel("Asabiyah value", self)

        self.txt = QLineEdit(self)

        self.combo = QComboBox(self)
        self.combo.addItems(self.mas)

        self.btn = QPushButton('    Ok    ', self)

        self.btn1 = QPushButton('    x    ', self)
        self.btn2 = QPushButton('    +    ', self)

        self.combo.move(180, 18)
        self.lbl1.move(20, 20)
        self.lbl2.move(20, 45)
        self.txt.move(180, 45)
        self.btn.move(130, 80)
        self.btn1.move(20, 80)
        self.btn2.move(240, 80)

        self.combo.activated[str].connect(self.onActivated)
        self.txt.textChanged[str].connect(self.onChanged)
        self.btn.clicked.connect(self.onClose)

        self.setGeometry(300, 300, 340, 110)
        self.setWindowTitle('QComboBox')
        self.show()

    def onActivated(self, text):
        self.qw.EnvChangeMode = text
        # print(self.qw.replay_version)

    def onChanged(self, text):
        self.qw.replay_name = text
        # print(self.qw.replay_name)

    def onClose(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex1 = Window()
    # ex2 = Envi(2)

    sys.exit(app.exec_())
