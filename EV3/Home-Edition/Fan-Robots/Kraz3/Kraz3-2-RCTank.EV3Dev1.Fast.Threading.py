#!/usr/bin/env python3

"""
Add the Kung-Fu manoeuvre
via the Touch Sensor and Remote Control of head and arms
"""

from kraz3_rctank_ev3dev1 import Kraz3

from threading import Thread


KRAZ3 = Kraz3(fast=True)


Thread(
    target=KRAZ3.kungfu_manoeuvre_whenever_touched_or_remote_controlled,
    daemon=True).start()

KRAZ3.main()