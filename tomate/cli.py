import os
import sched
import sys


_BASE_DIR = os.path.dirname(os.path.realpath(__file__))
_BELL_SOUND_PATH = os.path.join(_BASE_DIR, 'assets/bell.wav')
_LONG_DELAY_SECONDS = 1500
_RING_PRIORITY = 1


def _ring():
    os.system(f'aplay -q {_BELL_SOUND_PATH}')


def _run():
    scheduler = sched.scheduler()
    scheduler.enter(_LONG_DELAY_SECONDS, _RING_PRIORITY, _ring)
    scheduler.run()


def main():
    try:
        _run()
    except KeyboardInterrupt:
        sys.exit(1)
