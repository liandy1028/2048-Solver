import numpy as np
from pynput import keyboard
import random
from time import sleep
import t048sim as sim
import seleniumdriver
import time


driver = seleniumdriver.start_window()
realboard = np.zeros((4,4), dtype=int)

sleep(2)
seleniumdriver.update_board(realboard, driver)
# print(realboard)


t = time.time()
for _ in range(100):
    best_move = 0
    zeros = 0
    for move in ('left', 'right', 'up', 'down'):
        simboard = sim.make_move(realboard, move)
        if not np.array_equal(simboard, realboard):
            zros = 0
            for i in simboard:
                for j in i:
                    if j == 0:
                        zros += 1
            if zros > zeros:
                best_move = move
                zeros = zros
    seleniumdriver.make_move(best_move)
    realboard = sim.make_move(realboard, best_move)
    # sleep(0.03)
    seleniumdriver.update_board(realboard, driver)
    # print(realboard)
    
print(time.time() - t)

seleniumdriver.close(driver)