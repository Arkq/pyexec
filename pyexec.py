import sys
from os import execl
from signal import signal


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
