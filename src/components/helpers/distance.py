import math


def findDistance(coordinate1: int, coordinate2: int, landmarks: list) -> tuple:
    """Finds the distance between two coordinates from the list of landmarks
    supplied and returns the length between the coordiantes along with the
    center point between the two.

    Args:
        coordinate1 (int): First coordiante.
        coordinate2 (int): Second coordinate.
        landmarks (list): List containing all the landmarks and their
        respective coordiantes.

    Returns:
        tuple: Returns three values namely the length bwtween the coordiantes
        and the x and y coordiantes of the center point between the two
        coordinates  supplied.
    """
    x1, y1 = landmarks[coordinate1][1], landmarks[coordinate1][2]
    x2, y2 = landmarks[coordinate2][1], landmarks[coordinate2][2]

    cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
    length = math.hypot(x2 - x1, y2 - y1)
    return length, cx, cy
