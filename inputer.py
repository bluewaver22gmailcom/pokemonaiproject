import pynput
from pynput import mouse, keyboard
from pynput.keyboard import Key
from pynput.mouse import Button
import time

keyboard_controller = keyboard.Controller()

def up():
    keyboard_controller.press(Key.up)
    time.sleep(0.1)
    keyboard_controller.release(Key.up)

def down():
    keyboard_controller.press(Key.down)
    time.sleep(0.1)
    keyboard_controller.release(Key.down)

def left():
    keyboard_controller.press(Key.left)
    time.sleep(0.1)
    keyboard_controller.release(Key.left)

def right():
    keyboard_controller.press(Key.right)
    time.sleep(0.1)
    keyboard_controller.release(Key.right)

def start():
    keyboard_controller.press(Key.enter)

def select():
    keyboard_controller.press(Key.shift_r)

def a():
    keyboard_controller.press('a')
    time.sleep(0.1)
    keyboard_controller.release('a')

def y():
    keyboard_controller.press('y')

def x():
    keyboard_controller.press('x')

def b():
    keyboard_controller.press('b')

def screenshot():
    keyboard_controller.press(Key.f12)
    keyboard_controller.press(Key.ctrl)
    time.sleep(0.5)
    keyboard_controller.release(Key.f12)
    keyboard_controller.release(Key.ctrl)

def moveUp():
    keyboard_controller.press(Key.up)
    time.sleep(0.3)
    keyboard_controller.release(Key.up)

def moveDown():
    keyboard_controller.press(Key.down)
    time.sleep(0.3)
    keyboard_controller.release(Key.down)

def moveLeft():
    keyboard_controller.press(Key.left)
    time.sleep(0.3)
    keyboard_controller.release(Key.left)

def moveRight():
    keyboard_controller.press(Key.right)
    time.sleep(0.3)
    keyboard_controller.release(Key.right)

def lookUp():
    keyboard_controller.press(Key.up)
    time.sleep(0.06)
    keyboard_controller.release(Key.up)

def lookDown():
    keyboard_controller.press(Key.down)
    time.sleep(0.06)
    keyboard_controller.release(Key.down)

def lookLeft():
    keyboard_controller.press(Key.left)
    time.sleep(0.06)
    keyboard_controller.release(Key.left)

def lookRight():
    keyboard_controller.press(Key.right)
    time.sleep(0.06)
    keyboard_controller.release(Key.right)

time.sleep(3)
moveUp()
time.sleep(0.5)
moveRight()
time.sleep(0.5)
a()
lookUp()
time.sleep(0.5)
lookRight()
time.sleep(0.5)
lookDown()
time.sleep(0.5)
lookLeft()
time.sleep(0.5)
