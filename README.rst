===========
ASCII Frame
===========
Wrap your stdout in an ASCII frame. ::

  $ ls -l
  total 24
  -rw-r--r--  1 cychih  staff  1454  1 21 21:44 README.rst
  drwxr-xr-x  9 cychih  staff   306  1 21 21:43 ascii_frame
  drwxr-xr-x  6 cychih  staff   204  1 21 17:52 ascii_frame.egg-info
  drwxr-xr-x  3 cychih  staff   102  1 21 15:47 scripts
  -rw-r--r--  1 cychih  staff    22  1 21 19:01 setup.cfg
  -rw-r--r--  1 cychih  staff  1632  1 21 17:53 setup.py
  $ ls -l | ascii_frame
  .------------------------------------------------------------------.
  |total 24                                                          |
  |-rw-r--r--  1 cychih  staff  1454  1 21 21:44 README.rst          |
  |drwxr-xr-x  9 cychih  staff   306  1 21 21:43 ascii_frame         |
  |drwxr-xr-x  6 cychih  staff   204  1 21 17:52 ascii_frame.egg-info|
  |drwxr-xr-x  3 cychih  staff   102  1 21 15:47 scripts             |
  |-rw-r--r--  1 cychih  staff    22  1 21 19:01 setup.cfg           |
  |-rw-r--r--  1 cychih  staff  1632  1 21 17:53 setup.py            |
  '------------------------------------------------------------------'

You can also specify width and padding with ``-w`` and ``-p`` arguments ::

  $ ls -l | ascii_frame -w 50 -p 3
  .--------------------------------------------------.
  |   total 24                                       |
  |   -rw-r--r--  1 cychih  staff  1454  1 21 21:4   |
  |   4 README.rst                                   |
  |   drwxr-xr-x  9 cychih  staff   306  1 21 21:4   |
  |   3 ascii_frame                                  |
  |   drwxr-xr-x  6 cychih  staff   204  1 21 17:5   |
  |   2 ascii_frame.egg-info                         |
  |   drwxr-xr-x  3 cychih  staff   102  1 21 15:4   |
  |   7 scripts                                      |
  |   -rw-r--r--  1 cychih  staff    22  1 21 19:0   |
  |   1 setup.cfg                                    |
  |   -rw-r--r--  1 cychih  staff  1632  1 21 17:5   |
  |   3 setup.py                                     |
  '--------------------------------------------------'

Note: the frame itself does not calculated into width, so if you specify ``-w 50``, the output will actually be 52 character wide.

As a Python Module
-------------------
This Python module provides programming API to wrap text programmatically.

* ``wrap(data, width=0, padding=0)`` ::

    >>> import ascii_frame
    >>> ascii_frame.wrap(['ascii frame'])
    ['.-----.', '|ascii|', '|frame|', "'-----'"]
    >>> ascii_frame.wrap(['ascii frame'], width=3)
    ['.---.', '|asc|', '|ii |', '|fra|', '|me |', "'---'"]
    >>> ascii_frame.wrap(['ascii', 'frame'], width=7, padding=3)
    ['.-------.',
     '|   a   |',
     '|   s   |',
     '|   c   |',
     '|   i   |',
     '|   i   |',
     '|   f   |',
     '|   r   |',
     '|   a   |',
     '|   m   |',
     '|   e   |',
     "'-------'"]

* ``print(data, width=0, padding=0, **kwargs)``

  - Just a wrapping of ``wrap()`` and builtin ``print()``
