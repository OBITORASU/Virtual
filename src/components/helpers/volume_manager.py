import logging

import numpy as np

from src.components.helpers.os_detection import LINUX, MAC, WINDOWS


def manageVol(length: float) -> None:
    """Detects the host os and calls upon respective volume control modules to manipulate system volume.

    Args:
        length (float): Value corresponding to the length between two hand landmarks. This length is used to control system volume and this length is generated dynamically using mediapipe hand landmark recognition.
    """
    logging.basicConfig(format="%(levelname)s: %(message)s")
    try:
        if LINUX:
            from src.components.volume_controls import linux_vol

            controllerLinux = linux_vol.linuxVol()
            minVol, maxVol = (
                controllerLinux.getVolRangeLinux()[0],
                controllerLinux.getVolRangeLinux()[1],
            )
            volume = int(np.interp(length, [20, 160], [minVol, maxVol]))
            controllerLinux.changeVolLinux(volume)
        elif WINDOWS:
            from src.components.volume_controls import windows_vol

            controllerWin = windows_vol.winVol()
            minVol, maxVol = (
                controllerWin.getVolRangeWindows()[0],
                controllerWin.getVolRangeWindows()[1],
            )
            volume = np.interp(length, [20, 160], [minVol, maxVol])
            controllerWin.changeVolWindows(volume)
        elif MAC:
            from src.components.volume_controls import mac_vol

            controllerMac = mac_vol.macVol()
            minVol, maxVol = (
                controllerMac.getVolRangeMac()[0],
                controllerMac.getVolRangeMac()[1],
            )
            volume = int(np.interp(length, [20, 160], [minVol, maxVol]))
            controllerMac.changeVolMac(volume)
    except Exception as e:
        logging.error(e)
        exit(1)
