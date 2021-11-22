import logging
import time

import cv2

from src.components.helpers.hand_state import openOrClosed
from src.components.tracking import hand_tracker, volume_tracker


def volController(
    handedness: list, landmarks: list, capture: cv2.VideoCapture
) -> int:
    """Controller function which starts reading a stream of images from the
    camera. It then computes all the landmarks of the hands present in the
    image stream. Finally it uses the offset distance between the tip of the
    index finger and the thumb to control the volume of the system.

    Args:
        handedness (list): A list of strings contaning the handedness of the
        hands detected in the image based on index.
        landmarks (list): A list of integers contaning the landmarks of the
        hands detected in the image.
        capture (cv2.VideoCapture): Capture initiated by cv2.VideoCapture().

    Returns:
        int: Returns 0 in case of success to the calling function or exists
        with return code 0 if terminated with ESC.
    """
    logging.basicConfig(format="%(levelname)s: %(message)s")
    previousTime = 0.0
    currentTime = 0.0
    detect = hand_tracker.detector()
    detect.trackHands()
    mode = "Volume Mode"
    while True:
        success, image = capture.read()
        image = cv2.flip(image, 1)
        image = detect.drawHands(image)
        landmarks = detect.findLandmarks(image)
        handedness = detect.checkHandedness(image)
        if len(landmarks) != 0:
            image = volume_tracker.controlVolume(handedness, landmarks, image)
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
        if handedness:
            state = openOrClosed(handedness[0], landmarks)
            if state == [0, 0, 0, 0, 0]:
                return 0
        if k == 27:
            print("ESC")
            capture.release()
            cv2.destroyAllWindows()
            exit(0)
