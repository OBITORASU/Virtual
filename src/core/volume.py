import time

import cv2

from src.components.tracking import hand_tracker, volume_tracker


def volController() -> None:
    """Controller function which starts reading a stream of images from the camera. It then computes all the landmarks of the hands present in the image stream.Finally it uses the offset distance between the tip of the index finger and the thumb to control the volume of the system."""
    previousTime = 0.0
    currentTime = 0.0
    capture = cv2.VideoCapture(0)
    detect = hand_tracker.detector()
    detect.trackHands()
    while True:
        success, image = capture.read()
        image = cv2.flip(image, 1)
        image = detect.drawHands(image)
        landmarks = detect.findLandmarks(image)
        if len(landmarks) != 0:
            image = volume_tracker.controlVolume(landmarks, image)
        currentTime = time.time()
        fps = 1 / (currentTime - previousTime)
        previousTime = currentTime

        cv2.putText(
            image,
            str(int(fps)),
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
            break


volController()
