import os
import platform

# Detect os and set values to true for respective os detected rest being false
WINDOWS = (platform.system() == "Windows") and (os.name == "nt")
MAC = (platform.system() == "Darwin") and (os.name == "posix")
LINUX = (platform.system() == "Linux") and (os.name == "posix")
