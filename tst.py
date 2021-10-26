# https://www.baeldung.com/cs/2048-algorithm

import t048sim as sim
import seleniumdriver
import numpy as np
from time import sleep
import time

driver = seleniumdriver.start_window()

sleep(2)
board = seleniumdriver.update_board(driver)

t = time.time()
t1 = 0
t2 = 0
move = 'Null'
checkbit = False
for i in range(100):
    move = sim.next_move(board)
    seleniumdriver.make_move(move, driver)
    print(move)

    t= time.time()
    for move in sim.MOVES:
        b1 = np.array(board)
        a1 = sim.make_move(b1, move)
    t1 += time.time()-t
    t=time.time()
    for move in sim.MOVES:
        b2 = np.array(board)
        a2 = sim.make_move_old(b2, move)
    t2+=time.time()-t

    # print(board)
    # print(sim.TRYHARD_MODE)
    if move == 'None':
        # print(board)
        # print(sim.next_move(board))
        if checkbit:
            move = 'Done'
        checkbit = True
    else:
        checkbit = False
    sleep(0.03)
    board = seleniumdriver.update_board(driver)

# print(time.time() - t)

print(f'{t1},{t2}')

# print(board)
sleep(10)
seleniumdriver.close(driver)