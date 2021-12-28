import cv2
from pynput.mouse import Button, Controller

from src.components.helpers.distance import findDistance

mouse = Controller()


def leftClick(landmarks, image):
    length, cx, cy = findDistance(4, 8, landmarks)
    cv2.circle(image, (cx, cy), 5, (0, 255, 0), cv2.FILLED)
    if length < 25:
        cv2.circle(image, (cx, cy), 10, (0, 0, 255), cv2.FILLED)
        mouse.click(Button.left)


def rightClick(landmarks, image):
    length, cx, cy = findDistance(4, 12, landmarks)
    cv2.circle(image, (cx, cy), 5, (0, 255, 0), cv2.FILLED)
    if length < 25:
        cv2.circle(image, (cx, cy), 10, (0, 0, 255), cv2.FILLED)
        mouse.click(Button.right)
