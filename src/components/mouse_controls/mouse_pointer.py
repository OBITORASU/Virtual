from tkinter import Tk

import numpy as np
from pynput.mouse import Controller


def movePointer(
    camWidth, camHeight, x1, y1, curLocX, curLocY, prevLocX, prevLocY
):
    root = Tk()

    mouse = Controller()
    smoothening = 3
    frameReduction = 125

    width, height = (root.winfo_screenwidth(), root.winfo_screenheight())
    x3 = np.interp(x1, (frameReduction, camWidth - frameReduction), (0, width))
    y3 = np.interp(
        y1,
        (frameReduction, camHeight - frameReduction),
        (0, height),
    )
    mouse.position = (0, 0)

    curLocX = prevLocX + (x3 - prevLocX) / smoothening
    curLocY = prevLocY + (y3 - prevLocY) / smoothening
    mouse.move(curLocX, curLocY)
    prevLocX, prevLocY = curLocX, curLocY
    return prevLocX, prevLocY
