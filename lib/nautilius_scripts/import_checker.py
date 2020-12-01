import logging

logger = logging.getLogger(__name__)


def importGtk():
    try:
        import gi
        gi.require_version('Gtk', '3.0')
        return True

    except ImportError:
        logger.error("Cannot import package gi (ubuntu package: python3-gi)")
        return False

    except ValueError:
        logger.error("Cannot ensure Gtk version3.0")
        return False
