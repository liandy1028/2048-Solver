from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import math
import numpy as np
from time import sleep

def start_window():
    options = EdgeOptions()
    options.use_chromium = True
    options.add_extension('C:/edgedriver_win64/extension_1_32_4_0.crx')
    driver = Edge(executable_path='C:/edgedriver_win64/msedgedriver.exe', options=options)
    driver.get('https://play2048.co/')
    driver.maximize_window()
    global ACTIONS 
    ACTIONS = ActionChains(driver)
    return driver

def close(driver):
    driver.close()

def update_board(driver):
    board = np.zeros((4, 4), dtype=int)
    errors = 0
    maxerr = 2
    while errors < maxerr:
        try:
            elements = driver.find_elements_by_class_name('tile')
            for element in elements:
                i, j = (0, 0)
                for cls in element.get_attribute('class').split(' '):
                    if 'position' in cls:
                        cls = cls.lstrip('tile-position-')
                        i, j = cls.split('-')
                board[int(j) - 1][int(i) - 1] = int(math.log2(int(element.text)))
                errors = maxerr
        except:
            errors += 1
            # print(f"ERROR MESSAGE: Error #{errors}")
    return board

def make_move(move, driver):
    actions = ActionChains(driver)
    if move in ('up', 'down', 'left', 'right'):
        if move == 'up':
            actions.send_keys(Keys.ARROW_UP)
        elif move == 'down':
            actions.send_keys(Keys.ARROW_DOWN)
        elif move == 'left':
            actions.send_keys(Keys.ARROW_LEFT)
        elif move == 'right':
            actions.send_keys(Keys.ARROW_RIGHT)
        actions.perform()
    sleep(0.11)