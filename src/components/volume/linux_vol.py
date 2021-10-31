import alsaaudio

# Setup the Mixer object
m = alsaaudio.Mixer(device="pulse")


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

    def getVolRangeLinux(self) -> list:
        """Get the supported volume range of the system.

        Returns:
            list: A list of two  integer values corresponding to the volume range of the system.
        """
        return self.m.getrange()

    def getCurrentVolLinux(self) -> int:
        """Get the current volume of the system in terms of percentages.
        Returns:
            int: Value corresponding to the current output volume of the system in terms of percentage.
        """
        return self.volume
