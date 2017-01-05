# pyexec.py
# Copyright (c) 2015-2017 Arkadiusz Bokowy
#
# This file is a part of pyexec.
#
# This project is licensed under the terms of the MIT license.

import sys
from os import execl
from signal import signal


# NOTE: Changing this number will alter package version as well.
__version__ = '1.0.0'


def _handler(signum, stack):
    _handler.callback()
    execl(sys.executable, sys.executable, *sys.argv)


def install(signum, callback=lambda: None):
    """Install pyexec functionality for the given signal number.

    Optionally one can specify callback function, which will be called before
    process restart. In this function one can perform proper process shutdown
    operations, e.g. handler closing, data save, etc.

    Note:
        This function is not thread-safe. It should be called in the main
        thread - only the main thread is allowed to set signal handler.

    Arguments:
        signum: The signal number for which the exec handler is installed.
        callback: Function called just before the exec action.

    Returns:
        Previously installed handler (if any) for the given signal number.

    """
    _handler.callback = callback
    return signal(signum, _handler)
