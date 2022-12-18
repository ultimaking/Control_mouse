from pynput.mouse import Button, Controller as c_mouse
import random
mouse = c_mouse()
x,y = mouse.position
while True:
    mouse.position=(x,y)
