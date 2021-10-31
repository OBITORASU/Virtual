import alsaaudio

# Setup the Mixer object
m = alsaaudio.Mixer(device="pulse")


def changeVolLinux(volume: int) -> None:
    """Change the volume of the system.

    Args:
        volume (int): Value to which the volume will be set in terms of percentage.
    """
    m.setvolume(volume)


def getVolRangeLinux() -> list:
    """Get the supported volume range of the system.

    Returns:
        list: A list of two  integer values corresponding to the volume range of the system.
    """
    return m.getrange()


def getCurrentVolLinux() -> list:
    """Get the current volume of the system in terms of percentages.
    Returns:
        list: A list of integers contaning the volume in percentage of the available channels.
    """
    return m.getvolume()
