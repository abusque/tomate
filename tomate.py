import os
import sched


_LONG_DELAY_SECONDS = 1500
_RING_PRIORITY = 1


def _ring():
    os.system('aplay -q ./bell.wav')


def main():
    scheduler = sched.scheduler()

    scheduler.enter(_LONG_DELAY_SECONDS, _RING_PRIORITY, _ring)

    scheduler.run()


if __name__ == '__main__':
    main()
