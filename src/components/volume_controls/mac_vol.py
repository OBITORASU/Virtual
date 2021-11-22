from subprocess import call, check_output


class macVol:
    def __init__(self) -> None:
        self.volume = int(
            check_output(
                ["osascript -e 'output volume of (get volume settings)'"],
                shell=True,
            ).decode("utf-8")
        )

    def changeVolMac(self, vol: int) -> None:
        """Change the volume of the system.

        Args:
            vol (int): Value to which the volume will be set in terms of
            percentage.
        """
        call(
            ["osascript -e 'set volume output volume {}'".format(vol)],
            shell=True,
        )
        self.volume = vol

    def getVolRangeMac(self) -> tuple:
        """Get the supported volume range of the system in terms of percentage.

        Returns:
            tuple: A hardcoded value representing the system volume range in
            terms of percentage.
        """
        return (0, 100)

    def getCurrentVolMac(self) -> int:
        """[summary]

        Returns:
            int: Value corresponding to the current output volume of the
            system in terms of percentage.
        """
        return self.volume
