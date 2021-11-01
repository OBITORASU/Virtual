import alsaaudio


class linuxVol:
    def __init__(self) -> None:
        self.m = alsaaudio.Mixer(device="pulse")
        self.volume = self.m.getvolume()[0]

    def changeVolLinux(self, vol: int) -> None:
        """Change the volume of the system.

        Args:
            vol (int): Value to which the volume will be set in terms of percentage.
        """
        self.m.setvolume(vol)
        self.volume = vol

    def getVolRangeLinux(self) -> tuple:
        """Get the supported volume range of the system.

        Returns:
            tuple: A tuple of two  integer values corresponding to the volume range of the system in percentage.
        """
        return (0, 100)

    def getCurrentVolLinux(self) -> int:
        """Get the current volume of the system in terms of percentages.
        Returns:
            int: Value corresponding to the current output volume of the system in terms of percentage.
        """
        return self.volume
