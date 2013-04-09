python-event
============

Lightweight Python Event Module

Sample code
----------
```python
#!/usr/bin/python

import socket
sock = None

# Import event class in event module
from event import event

# Initialise event instances.
connecting = event()
connected = event()
failed = event()

# Handle with decorator.
@connecting.handler
def on_connecting():
  print "connecting..."

# These will be handled in __name__ == "__main__".
def on_connected():
  print "connected!"

def on_failed(ex):
  print "%s" % repr(ex)


if __name__ == "__main__":
  # Handle with __iadd__.
  connected += on_connected
  # Handle with __ior__.
  failed |= on_failed
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  # Raise connecting event.
  connecting()
  try:
    sock.connect(("127.0.0.1", 80))
    # Raise connected event.
    connected()
  except Exception as ex:
    # Unhandle with __isub__
    connecting -= on_connecting
    # Unhandle with __ixor__
    connected ^= on_connected
    # Raise failed event.
    failed(ex)
  sock.close()
```
