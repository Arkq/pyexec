# reload.py
# Copyright (c) 2015-2017 Arkadiusz Bokowy
#
# This file is a part of pyexec.
#
# This project is licensed under the terms of the MIT license.

import signal
import sys
import time

import pyexec


def callback():
    sys.stderr.write("Reloading...\n")
    return sys.argv[0], str(int(sys.argv[1]) - 1)

pyexec.install(signal.SIGALRM, callback)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.stderr.write("usage: {} <NB>\n".format(sys.argv[0]))
        sys.exit(1)
    if int(sys.argv[1]):
        signal.alarm(1)
        time.sleep(2)
