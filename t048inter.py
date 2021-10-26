from pynput import keyboard
from time import sleep
import pyautogui
from cv2 import cv2
import numpy as np

BBOX = 0
COLOR2NUM = dict()
END = False

def make_move(move):
    pyautogui.press(move)

def update_board():
    board = np.zeros((4,4), int)
    ss = cv2.cvtColor(np.array(pyautogui.screenshot(region=BBOX)), cv2.COLOR_RGB2BGR)
    colors = dict()
    for i in range(4):
        for j in range(4):
            color = tuple(ss[int(BBOX[3] / 4 * (i + 0.2))][int(BBOX[2] / 4 * (j + 0.2))])
            if color in COLOR2NUM:
                board[i][j] = COLOR2NUM[color]
            else:
                add_to_dict(color)
                board[i][j] = COLOR2NUM[color]

    return board

def find_bbox():
    img = pyautogui.screenshot()
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

    lowerb = np.array([155,168,182])
    upperb = np.array([165,178,192])
    img = cv2.inRange(img, lowerb, upperb)

    contours, _ = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    max_area = 0
    final_cnt = 0
    for cnt in contours:
        pos = cv2.boundingRect(cnt)
        if (area := pos[2] * pos[3]) > max_area:
            max_area = area
            final_cnt = cnt

    bbox = cv2.boundingRect(final_cnt)
    global BBOX
    BBOX = bbox
    return bbox

def add_to_dict(color):
    global COLOR2NUM
    COLOR2NUM[color] = 0
    COLOR2NUM[color] = len(COLOR2NUM) - 1
    if len(COLOR2NUM) > 10:
        global END 
        END = True

def start_board():
    board = np.zeros((4,4), int)
    ss = cv2.cvtColor(np.array(pyautogui.screenshot(region=BBOX)), cv2.COLOR_RGB2BGR)
    colors = dict()
    for i in range(4):
        for j in range(4):
            color = tuple(ss[int(BBOX[3] / 4 * (i + 0.2))][int(BBOX[2] / 4 * (j + 0.2))])
            if color in colors:
                colors[color] += 1
            else:
                colors[color] = 0
    
    for color, amt in colors.items():
        if amt == 13:
            add_to_dict(color)
    if len(colors) == 2:
        for color, amt in colors.items():
            if amt == 1:
                add_to_dict(color)
    else:
        color_brightness = dict()
        for color, amt in colors.items():
            if amt == 0:
                color_brightness[sum(color)] = color
        add_to_dict(color_brightness[max(color_brightness)])
        add_to_dict(color_brightness[min(color_brightness)])

    for i in range(4):
        for j in range(4):
            color = tuple(ss[int(BBOX[3] / 4 * (i + 0.2))][int(BBOX[2] / 4 * (j + 0.2))])
            board[i][j] = COLOR2NUM[color]

    return board


# def on_press(key):
#     if key == keyboard.Key.esc:
#         return False
#     else:
#         print(update_board())


# find_bbox()
# # img = pyautogui.screenshot(region=BBOX)
# # img.show()
# print(start_board())
# with keyboard.Listener(on_press=on_press) as k:
#     k.join()
