import os


class NautilusScriptVariables:
    # newline-delimited paths for selected files (only if local)
    NAUTILUS_SCRIPT_SELECTED_FILE_PATHS = 'NAUTILUS_SCRIPT_SELECTED_FILE_PATHS'

    # newline-delimited URIs for selected files
    NAUTILUS_SCRIPT_SELECTED_URIS = 'NAUTILUS_SCRIPT_SELECTED_URIS'

    # current location
    NAUTILUS_SCRIPT_CURRENT_URI = 'NAUTILUS_SCRIPT_CURRENT_URI'

    # position and size of current window
    NAUTILUS_SCRIPT_WINDOW_GEOMETRY = 'NAUTILUS_SCRIPT_WINDOW_GEOMETRY'

    @classmethod
    def getSelectedFiles(cls):
        yield from os.environ.get(cls.NAUTILUS_SCRIPT_SELECTED_FILE_PATHS, '').splitlines()
