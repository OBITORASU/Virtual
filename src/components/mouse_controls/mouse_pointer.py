from tkinter import Tk

import numpy as np
from pynput.mouse import Controller


def movePointer(
    camWidth: float,
    camHeight: float,
    x1: int,
    y1: int,
    curLocX: int,
    curLocY: int,
    prevLocX: int,
    prevLocY: int,
) -> tuple:
    """Takes the camera's width, height along with the coordinates of the x
    and y axes for the tip of the index finger. The other arguments include
    the current and previous x and y axes location coordinates of the tip of
    the index finger. The function itself calculates the position of the tip
    of the index finger and moves the mouse around the screen relative to it.
    It also does some frame reduction so that the capturable area is enough
    to cover the entire distance of the screen. On top of that smoothing is
    applied to prevent the pointer movement from being choppy.

    Args:
        camWidth (float): [description]
        camHeight (float): [description]
        x1 (int): [description]
        y1 (int): [description]
        curLocX (int): [description]
        curLocY (int): [description]
        prevLocX (int): [description]
        prevLocY (int): [description]

    Returns:
        tuple: Returns two values containing the coordinates corresponding
        to the previous location of the pointer on the x and y axes
        respectively.
    """
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
