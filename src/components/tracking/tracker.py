# Hand Tracking
import time

import cv2
import mediapipe
import numpy.typing as nt


class detector:
    def __init__(self):
        pass

    def trackHands(
        self,
        imageMode: bool = False,
        maxHands: int = 2,
        complexity: int = 1,
        detectionConf: float = 0.7,
        trackingConf: float = 0.7,
    ) -> None:
        """Creates a mediapipe.solutions.hands.Hands object with the passed arguments.

        Args:
            imageMode (bool, optional): Decides if the image is static or a dynamic video stream. Defaults to False (Video Stream).
            maxHands (int, optional): Value corresponding to the maximum hands to be detected. Defaults to 2.
            complexity (int, optional): Value to set the complexity the hand landmarking model can be 0 or 1. Defaults to 1.
            detectionConf (float, optional): Value to set the maximum confidence value for the model to consider when determining successfull detection. Range [0.0, 1.0]Defaults to 0.7.
            trackingConf (float, optional): Value to set the maximum confidence value for the model to consider when determining successfull tracking. Range [0.0, 0.1] Defaults to 0.7.
        """
        self.mpHands = mediapipe.solutions.hands
        self.hands = self.mpHands.Hands(
            imageMode, maxHands, complexity, detectionConf, trackingConf
        )

    def drawHands(self, image: nt.NDArray, draw: bool = True) -> nt.NDArray:
        """Accepts a valid NDArray for an image and draws landmarks for the hands detected in the image based on a boolean value passed to it as an argument.

        Args:
            image (NDArray): An NDArray of an image generated by the cv2.VideoCapture(0).read() function.
            draw (bool, optional): Decides whether to enable or disable drawing on the image. Defaults to True.

        Returns:
            NDArray: An NDarray of an image with landmarks drawn for the detected hands.
        """

        imgRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        self.result = self.hands.process(imgRGB)
        self.mpDraw = mediapipe.solutions.drawing_utils

        if self.result.multi_hand_landmarks:
            for handLandmarks in self.result.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(
                        image, handLandmarks, self.mpHands.HAND_CONNECTIONS
                    )

        return image

    def findLandmarks(self, image: nt.NDArray, draw: bool = True) -> list:
        """Finds landmarks of the first hand in the supplied image and returns a list of the landmarks found.

        Args:
            image (nt.NDArray): An NDArray of an image in which the hand landmarks are to be found.
            draw (bool, optional): Decides whether to enable or disable drawing landmarks on the image. Defaults to True.

        Returns:
            list: A list of integers contaning the landmarks of the first hand detected in the image.
        """
        landmarkList = []
        if self.result.multi_hand_landmarks:
            myHand = self.result.multi_hand_landmarks[0]
            for id, landmark in enumerate(myHand.landmark):
                h, w, c = image.shape
                cx, cy = int(landmark.x * w), int(landmark.y * h)
                landmarkList.append([id, cx, cy])
                if draw:
                    cv2.circle(image, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
        return landmarkList


pTime = 0.0
cTime = 0.0
cap = cv2.VideoCapture(0)
detect = detector()
detect.trackHands()
while True:
    success, image = cap.read()
    image = cv2.flip(image, 1)
    image = detect.drawHands(image)
    landmarks = detect.findLandmarks(image)
    if len(landmarks) != 0:
        print(landmarks)
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
