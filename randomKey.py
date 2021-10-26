from pynput import keyboard
import random
from time import sleep

k = keyboard.Controller()
sleep(1)

for i in range(200):
    b = random.randint(0, 4)
    if b == 0:
        k.press(keyboard.Key.left)
        k.release(keyboard.Key.left)
    elif b == 1 or b == 2:
        k.press(keyboard.Key.right)
        k.release(keyboard.Key.right)
    elif b == 3:
        k.press(keyboard.Key.down)
        k.release(keyboard.Key.down)
    else:
        k.press(keyboard.Key.down)
        k.release(keyboard.Key.down)
    sleep(0.15)