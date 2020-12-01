#!/usr/bin/env python

import logging

from nautilius_scripts.import_checker import importGtk
from nautilius_scripts.log_config import configLogger
from nautilius_scripts.trust_changer import TrustChanger

logger = logging.getLogger()


def main():
    logging.basicConfig(level=logging.DEBUG)
    configLogger()
    if not importGtk():
        exit()
    TrustChanger.changeFiles()


if __name__ == '__main__':
    main()
