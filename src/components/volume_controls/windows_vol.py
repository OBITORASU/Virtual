from ctypes import POINTER, cast

from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


class winVol:
    def __init__(self):
        self.devices = AudioUtilities.GetSpeakers()
        self.interface = self.devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None
        )
        self.winVolume = cast(self.interface, POINTER(IAudioEndpointVolume))
        self.volume = self.winVolume.GetMasterVolumeLevel()

    def changeVolWindows(self, vol: float) -> None:
        """Change the volume of the system.

        Args:
            volume (float): Value to which the volume will be set in terms of
            supported range.
        """
        self.winVolume.SetMasterVolumeLevel(vol, None)
        self.volume = vol

    def getVolRangeWindows(self) -> tuple:
        """Get the supported volume range of the system.

        Returns:
            tuple: A tuple of three float values corresponding to the volume
            range of the system.
        """
        return self.winVolume.GetVolumeRange()

    def getCurrentVolWindows(self) -> float:
        """Get the current volume of the system.

        Returns:
            float: Value corresponding to the current volume of the system.
        """
        return self.volume
