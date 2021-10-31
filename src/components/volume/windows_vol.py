from ctypes import POINTER, cast

from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))


def changeVolWindows(vol: float) -> None:
    """Change the volume of the system.

    Args:
        volume (float): Value to which the volume will be set.
    """
    volume.SetMasterVolumeLevel(vol, None)


def getVolRangeWindows() -> tuple:
    """Get the supported volume range of the system.

    Returns:
        tuple: A tuple of three float values corresponding to the volume range of the system.
    """
    return volume.GetVolumeRange()


def getCurrentVolWindows() -> float:
    """Get the current volume of the system.

    Returns:
        float: A float value corresponding to the current volume of the system.
    """
    return volume.GetMasterVolumeLevel()
