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
move = 'Null'
checkbit = 0
while move != 'Done':
    move = sim.next_move(board)
    # print(board)
    # print(sim.TRYHARD_MODE)
    if move == 'None':
        # print(board)
        # print(sim.next_move(board))
        if checkbit == 3:
            print(move)
            move = 'Done'
        checkbit += 1
    else:
        print(move)
        seleniumdriver.make_move(move, driver)
        checkbit = 0
    # sleep(0.05)
    board = seleniumdriver.update_board(driver)

# print(time.time() - t)

# print(board)
sleep(10)
seleniumdriver.close(driver)