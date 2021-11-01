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
        detectionConf: float = 0.8,
        trackingConf: float = 0.8,
    ) -> None:
        """Creates a mediapipe.solutions.hands.Hands object with the passed arguments.

        Args:
            imageMode (bool, optional): Decides if the image is static or a dynamic video stream. Defaults to False (Video Stream).
            maxHands (int, optional): Value corresponding to the maximum hands to be detected. Defaults to 2.
            complexity (int, optional): Value to set the complexity the hand landmarking model can be 0 or 1. Defaults to 1.
            detectionConf (float, optional): Value to set the maximum confidence value for the model to consider when determining successfull detection. Range [0.0, 1.0]Defaults to 0.8.
            trackingConf (float, optional): Value to set the maximum confidence value for the model to consider when determining successfull tracking. Range [0.0, 0.1] Defaults to 0.8.
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
            NDArray: An NDarray of the image stream. Optionally supports landmarks drawn for the detected hands if draw is set to True.
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

    def findLandmarks(self, image: nt.NDArray) -> list:
        """Finds landmarks of the hands in the supplied image and returns a list of the landmarks found.

        Args:
            image (nt.NDArray): An NDArray of an image in which the hand landmarks are to be found.

        Returns:
            list: A list of integers contaning the landmarks of the hands detected in the image.
        """
        landmarkList = []
        if self.result.multi_hand_landmarks:
            for handLandmarks in self.result.multi_hand_landmarks:
                for id, landmark in enumerate(handLandmarks.landmark):
                    h, w, c = image.shape
                    cx, cy = int(landmark.x * w), int(landmark.y * h)
                    landmarkList.append([id, cx, cy])
        return landmarkList