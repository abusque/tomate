======
Tomate
======

A minimalist pomodoro timer.

Requirements
------------

To run Tomate, you will need the following software:

- Python ≥ 3.6
- aplay

`aplay` is the native ALSA wav player, used to play a bell tone at the
end of a pomodoro period.

To install Tomate, we also recommend using the `pip` package manager.

Once all the requirements are fulfilled, you may proceed with the
installation.

Installing
----------

To install Tomate system-wide, simply run:

.. code-block:: sh

   sudo pip3 install tomate

To install Tomate manually from source, the steps are as follows:

.. code-block:: sh

   git clone git@github.com:abusque/tomate.git
   cd tomate
   sudo ./setup.py install

Using
-----

Once installed, you can use Tomate by simply running the following:

.. code-block:: sh

   tomate

This will start a 25 minute timer, after which a soft bell will
ring. To start another pomodoro, simply re-run the command.
