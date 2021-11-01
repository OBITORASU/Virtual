import math
import time

import cv2

from src.components.helpers.volume_manager import manageVol
from src.components.tracking import tracker


class volume:
    def __init__(self):
        pass

    def volController(self):
        pTime = 0.0
        cTime = 0.0
        capture = cv2.VideoCapture(0)
        detect = tracker.detector()
        detect.trackHands()
        while True:
            success, image = capture.read()
            image = cv2.flip(image, 1)
            image = detect.drawHands(image)
            landmarks = detect.findLandmarks(image)
            if len(landmarks) != 0:
                x1, y1 = landmarks[4][1], landmarks[4][2]
                x2, y2 = landmarks[8][1], landmarks[8][2]

                cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
                cv2.line(image, (x1, y1), (x2, y2), (0, 128, 0), 2)
                cv2.circle(image, (cx, cy), 5, (0, 128, 0), cv2.FILLED)

                length = math.hypot(x2 - x1, y2 - y1)
                if length < 25:
                    cv2.circle(image, (cx, cy), 5, (0, 0, 255), cv2.FILLED)
                manageVol(length)

            cTime = time.time()
            fps = 1 / (cTime - pTime)
            pTime = cTime

            cv2.putText(
                image,
                str(int(fps)),
                (5, 15),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 128, 0),
                1,
            )
            cv2.imshow("Image", image)
            k = cv2.waitKey(1)
            if k == 27:
                print("ESC")
                capture.release()
                cv2.destroyAllWindows()
                break


controller = volume()
controller.volController()
