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
    b = random.randint(0, 4)
    move = 0
    if b == 0:
        move = 'left'
    elif b == 1 or b == 2:
        move = 'right'
    elif b == 3:
        move = 'down'
    else:
        move = 'up'
    t048inter.make_move(move)
    simboard = t048sim.make_move(realboard, move)
    sleep(0.23)
    realboard = t048inter.update_board()
    diff = 16 - sum(sum(realboard == simboard))
    if diff > 1:
        print(realboard)
        print(simboard)
        print(move)
        print(diff)
        break