import numpy as np
from pynput import keyboard
import random
from time import sleep
import t048inter
import t048sim

sleep(1)

t048inter.find_bbox()
realboard = t048inter.start_board()

while not t048inter.END:
    best_move = 0
    zeros = 0
    for move in ('left', 'right', 'up', 'down'):
        simboard = t048sim.make_move(realboard, move)
        if not np.array_equal(simboard, realboard):
            zros = 0
            for i in simboard:
                for j in i:
                    if j == 0:
                        zros += 1
            if zros > zeros:
                best_move = move
                zeros = zros
    t048inter.make_move(best_move)
    sleep(0.25)
    realboard = t048inter.update_board()
    print(realboard)