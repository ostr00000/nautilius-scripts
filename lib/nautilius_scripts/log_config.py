import logging
from os.path import expanduser


def configLogger():
    formatStr = "[{asctime}] [{levelname:<6}] {module}:{funcName}:{lineno}({name}): {message}"
    formatter = logging.Formatter(formatStr, style="{")

    fileHandler = logging.FileHandler(expanduser('~') + '/.local/share/nautilus/script.log')
    fileHandler.setFormatter(formatter)

    formatStr = "{name}:{funcName}:{lineno}: {message}"
    formatter = logging.Formatter(formatStr, style="{")
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)

    root = logging.getLogger()
    root.setLevel(level=logging.DEBUG)
    root.addHandler(fileHandler)
    root.addHandler(streamHandler)

    root.info("Loggers configured")
