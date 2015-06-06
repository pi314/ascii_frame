=====
frame
=====

Wrap your stdout in a frame ::

  $ ls -al
  total 16
  drwxr-xr-x   5 cychih  staff  170  6  6 14:55 .
  drwxr-xr-x  10 cychih  staff  340  6  6 14:26 ..
  drwxr-xr-x   9 cychih  staff  306  6  6 14:55 .git
  -rw-r--r--   1 cychih  staff  310  6  6 14:55 README.rst
  -rwxr-xr-x   1 cychih  staff  600  6  6 14:53 frame
  $ ls -al | frame
  .--------------------------------------------------------.
  |total 16                                                |
  |drwxr-xr-x   5 cychih  staff  170  6  6 14:55 .         |
  |drwxr-xr-x  10 cychih  staff  340  6  6 14:26 ..        |
  |drwxr-xr-x   9 cychih  staff  306  6  6 14:55 .git      |
  |-rw-r--r--   1 cychih  staff  361  6  6 14:55 README.rst|
  |-rwxr-xr-x   1 cychih  staff  600  6  6 14:53 frame     |
  '--------------------------------------------------------'
  $ ls -al | frame 1
  .----------------------------------------------------------.
  | total 16                                                 |
  | drwxr-xr-x   5 cychih  staff  170  6  6 14:55 .          |
  | drwxr-xr-x  10 cychih  staff  340  6  6 14:26 ..         |
  | drwxr-xr-x   9 cychih  staff  306  6  6 14:56 .git       |
  | -rw-r--r--   1 cychih  staff  869  6  6 14:55 README.rst |
  | -rwxr-xr-x   1 cychih  staff  600  6  6 14:53 frame      |
  '----------------------------------------------------------'

