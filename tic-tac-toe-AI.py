from tkinter import *
import tkinter
from typing import DefaultDict


root = Tk()
root.title("Tutorial")
root.iconbitmap('tic_tac_toe.ico')

button_0 = Button(root, text='  ', padx=40, pady=40, command=lambda:turno(0))
button_1 = Button(root, text='  ', padx=40, pady=40, command=lambda:turno(1))
button_2 = Button(root, text='  ', padx=40, pady=40, command=lambda:turno(2))
button_3 = Button(root, text='  ', padx=40, pady=40, command=lambda:turno(3))
button_4 = Button(root, text='  ', padx=40, pady=40, command=lambda:turno(4))
button_5 = Button(root, text='  ', padx=40, pady=40, command=lambda:turno(5))
button_6 = Button(root, text='  ', padx=40, pady=40, command=lambda:turno(6))
button_7 = Button(root, text='  ', padx=40, pady=40, command=lambda:turno(7))
button_8 = Button(root, text='  ', padx=40, pady=40, command=lambda:turno(8))

caselle = [
    button_0, 
    button_1, 
    button_2, 
    button_3, 
    button_4, 
    button_5, 
    button_6, 
    button_7, 
    button_8
]

button_0.grid(row=0, column=0)
button_1.grid(row=0, column=1)
button_2.grid(row=0, column=2)

button_3.grid(row=1, column=0)
button_4.grid(row=1, column=1)
button_5.grid(row=1, column=2)

button_6.grid(row=2, column=0)
button_7.grid(row=2, column=1)
button_8.grid(row=2, column=2)

class nP:
    def __init__(self, man, computer):
        self.man = man
        self.computer = computer

PLAYER = nP('X', 'O')

gameData = ['', '', '', '', '', '', '', '', '',]

win_combos = [
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 4, 8],
    [2, 4, 6]
]

def turno(casella):
    if gameData[casella]: return

    caselle[casella].config(text=PLAYER.man)
    gameData[casella] = PLAYER.man

    if check_winner(gameData, PLAYER.man):
        return print('WIN')#gameOver(variabile_turno)
    if check_tie(gameData):
        return print('TIE')#gameOver('Pareggio')
    
    id = minimax(gameData, PLAYER.computer)['id']
    caselle[id].config(text=PLAYER.computer)
    gameData[id] = PLAYER.computer
    print(iterr)
    
    if check_winner(gameData, PLAYER.computer):
        return print('WIN')#gameOver(variabile_turno)
    if check_tie(gameData):
        return print('TIE')#gameOver('Pareggio')

def check_winner(gameData, variabile_turno):
    x = 0

    while x < len(win_combos):
        vittoria = True

        i = 0
        while i < len(win_combos[x]):
            id = win_combos[x][i]
            vittoria = gameData[id] == variabile_turno and vittoria
            i += 1

        if vittoria:
            return True

        x += 1
    return False


def check_tie(gameData):
    pareggio = True
    x= 0

    while x < len(gameData):
        pareggio = gameData[x] and pareggio
        x += 1

    if pareggio:
        return True

    return False

def gameOver():
    return 'gameOver'

def check_spaces(gameData):
    EMPTY = []
    x = 0

    while x < len(gameData):
        if not gameData[x]: EMPTY.append(x)
        x += 1
    
    return EMPTY

iterr = 0
def minimax(gameData, turno):
    if check_winner(gameData, PLAYER.computer): return {'eval': 10 }
    if check_winner(gameData, PLAYER.man):      return {'eval': -10}
    if check_tie(gameData):                     return {'eval': 0  }
    global iterr
    iterr += 1

    empty = check_spaces(gameData)
    moves = []

    x = 0
    while x < len(empty):
        id = empty[x]

        backup = gameData[id]
        gameData[id] = turno

        move = {}
        move['id'] = id

        if turno == PLAYER.computer:
            move['eval'] = minimax(gameData, PLAYER.man)['eval']
        else:
            move['eval'] = minimax(gameData, PLAYER.computer)['eval']
        
        gameData[id] = backup
        moves.append(move)
        x += 1
    
    bestMove = ''

    if turno == PLAYER.computer:
        # max
        bestEval = -999999
        i = 0
        while i < len(moves):
            if moves[i]['eval'] > bestEval:
                bestEval = moves[i]['eval']
                bestMove = moves[i]
            i += 1
    else:
        # mini
        bestEval = 999999
        i = 0
        while i < len(moves):
            if moves[i]['eval'] < bestEval:
                bestEval = moves[i]['eval']
                bestMove = moves[i]
            i += 1
    
    return bestMove



root.mainloop()