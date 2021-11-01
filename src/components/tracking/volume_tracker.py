import math

import cv2
import numpy.typing as nt

from src.components.helpers.volume_manager import manageVol


def controlVolume(
    landmarks: list, image: nt.NDArray, draw: bool = True
) -> nt.NDArray:
    """Takes an image stream in the form of an NDArray. It detects hand landmarks present in the image stream and calculates the offset length between the tip of the thumb and the index finger. Then, it calls src.components.helpers.volume_manager.manageVol with the offset length as an argument to manipulate the system volume. Optionally returns the image stream with drawings if draw is set to True, else it returns the image as is.

    Args:
        landmarks (list): Values corresponding to the hand landmarks detected in the image stream.
        image (NDArray): An NDArray of an image generated by the cv2.VideoCapture(0).read() function.
        draw (bool, optional): Decides whether to enable or disable drawing on the image. Defaults to True.

    Returns:
        NDArray: An NDarray of the image stream. Optionally supports drawing on the image if draw is set to True.
    """
    x1, y1 = landmarks[4][1], landmarks[4][2]
    x2, y2 = landmarks[8][1], landmarks[8][2]

    cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
    if draw:
        cv2.line(image, (x1, y1), (x2, y2), (0, 128, 0), 2)
        cv2.circle(image, (cx, cy), 5, (0, 255, 0), cv2.FILLED)

    length = math.hypot(x2 - x1, y2 - y1)
    if length < 25 and draw:
        cv2.circle(image, (cx, cy), 5, (0, 0, 255), cv2.FILLED)
    manageVol(length)
    return image