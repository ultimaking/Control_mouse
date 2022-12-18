from pynput.mouse import Button, Controller as c_mouse
import random
mouse = c_mouse()
while True:
    x,y = mouse.position
    mouse.position=(x+random.randint(-100,100),y+random.randint(-100,100))
