import logging
import time

import cv2

from src.components.helpers.hand_state import openOrClosed
from src.components.tracking import hand_tracker
from src.core.volume import volController


def modeSelection():
    """A selector functions which sets up and starts the camera and waits for
    certain hand gestures to call for specific modes like the Volume Mode,
    Keyboard Mode and Mouse Mode."""
    logging.basicConfig(format="%(levelname)s: %(message)s")
    capture = cv2.VideoCapture(0)
    if capture is None or not capture.isOpened():
        logging.error("Webcam could not be initialized.")
        exit(1)
    previousTime = 0.0
    currentTime = 0.0

    detect = hand_tracker.detector()
    detect.trackHands()
    mode = "Selector Mode"
    while True:
        success, image = capture.read()
        image = cv2.flip(image, 1)
        image = detect.drawHands(image)
        landmarks = detect.findLandmarks(image)
        handedness = detect.checkHandedness(image)
        if len(landmarks) != 0:
            fingerState = openOrClosed(handedness[0], landmarks)
            if fingerState == [0, 1, 0, 0, 0]:
                print("call vol function")
                volController(handedness, landmarks, capture)

            elif fingerState == [0, 1, 1, 0, 0]:
                print("call mouse function")

            elif fingerState == [0, 1, 1, 1, 0]:
                print("call keyboard function")
            else:
                print("None")

        currentTime = time.time()
        fps = 1 / (currentTime - previousTime)
        previousTime = currentTime

        cv2.putText(
            image,
            "{} {}".format(mode, str(int(fps))),
            (5, 15),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 255, 0),
            1,
        )

        cv2.imshow("Image", image)
        k = cv2.waitKey(1)
        if k == 27:
            print("ESC")
            capture.release()
            cv2.destroyAllWindows()
            exit(0)


modeSelection()
