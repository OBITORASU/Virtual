import math

import cv2
import numpy.typing as nt

from src.components.helpers.volume_manager import manageVol


def controlVolume(landmarks: list, image: nt.NDArray) -> nt.NDArray:
    x1, y1 = landmarks[4][1], landmarks[4][2]
    x2, y2 = landmarks[8][1], landmarks[8][2]

    cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
    cv2.line(image, (x1, y1), (x2, y2), (0, 128, 0), 2)
    cv2.circle(image, (cx, cy), 5, (0, 255, 0), cv2.FILLED)

    length = math.hypot(x2 - x1, y2 - y1)
    if length < 25:
        cv2.circle(image, (cx, cy), 5, (0, 0, 255), cv2.FILLED)
    manageVol(length)
    return image
