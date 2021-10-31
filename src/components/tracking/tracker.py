# Hand Tracking
import time

import cv2
import mediapipe


class detector:
    def __init__(self):
        pass

    def trackHands(
        self,
        imageMode=False,
        maxHands=2,
        complexity=1,
        detectionConf=0.7,
        trackingConf=0.7,
    ):
        self.mpHands = mediapipe.solutions.hands
        self.hands = self.mpHands.Hands(
            imageMode, maxHands, complexity, detectionConf, trackingConf
        )
        self.mpDraw = mediapipe.solutions.drawing_utils

    def drawHands(self, image, draw=True):
        imgRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        self.result = self.hands.process(imgRGB)

        if self.result.multi_hand_landmarks:
            for handLandmarks in self.result.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(
                        image, handLandmarks, self.mpHands.HAND_CONNECTIONS
                    )

        return image

    def findLandmark(self, img, handNo=0, draw=True):
        landMarkList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                landMarkList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
        return landMarkList


pTime = 0.0
cTime = 0.0
cap = cv2.VideoCapture(0)
detect = detector()
detect.trackHands()

while True:
    success, image = cap.read()
    image = cv2.flip(image, 1)
    image = detect.drawHands(image)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(
        image,
        str(int(fps)),
        (10, 50),
        cv2.FONT_HERSHEY_COMPLEX_SMALL,
        3,
        (255, 0, 255),
        3,
    )
    cv2.imshow("Image", image)
    k = cv2.waitKey(1)
    if k == 27:
        print("ESC")
        cap.release()
        cv2.destroyAllWindows()
        break
