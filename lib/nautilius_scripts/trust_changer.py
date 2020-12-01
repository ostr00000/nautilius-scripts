from nautilius_scripts.nautilus_script_variables import NautilusScriptVariables


class TrustChanger(NautilusScriptVariables):

    def __init__(self, path: str):
        from gi.repository import Gio

        # noinspection PyArgumentList,PyCallByClass
        self.file: Gio.File = Gio.File.new_for_path(path)

        # noinspection PyArgumentList,PyCallByClass
        self.desktopAppInfo: Gio.DesktopAppInfo = Gio.DesktopAppInfo.new_from_filename(path)
        if self.desktopAppInfo is None or self.file is None:
            raise ValueError(f"Invalid path {path}")

    @classmethod
    def changeFiles(cls, trust: bool = True):
        for file in cls.getSelectedFiles():
            trustChanger = cls(file)
            trustChanger.setTrustedState(trust)

    def setTrustedState(self, isTrusted: bool = False):
        val = 'true' if isTrusted else 'false'
        from gi.repository import Gio
        ok = self.file.set_attribute_string('metadata::trusted', val, Gio.FileQueryInfoFlags.NONE)
        return ok
