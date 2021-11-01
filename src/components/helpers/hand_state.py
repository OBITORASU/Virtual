import logging


def openOrClosed(handedness: str, landmarks: list) -> list:
    """Calculates which fingers are open and closed based on landmarks and handedness.

    Args:
        handedness (str): A single value "Left" or "Right" to denote the handedness of the hand.
        landmarks (list): Values corresponding to the hand landmarks detected in the image stream.

    Returns:
        list: A list of integers namely 0s and 1s denoting which fingers are open and which ones are closed based on index.
    """
    logging.basicConfig(format="%(levelname)s: %(message)s")
    tipLandmark = [4, 8, 12, 16, 20]
    fingers = []
    if handedness == "Left":
        if landmarks[tipLandmark[0]][1] > landmarks[tipLandmark[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
    elif handedness == "Right":
        if landmarks[tipLandmark[0]][1] < landmarks[tipLandmark[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
    else:
        logging.error(
            "Invalid value for handedness, it can only be Left or Right."
        )
        exit(1)

    for index in range(1, 5):
        if (
            landmarks[tipLandmark[index]][2]
            < landmarks[tipLandmark[index] - 2][2]
        ):
            fingers.append(1)
        else:
            fingers.append(0)

    return fingers
