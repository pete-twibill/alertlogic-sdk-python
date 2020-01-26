__version__ = '1.0.1'
__author__ = 'Alert Logic, Inc.'

import logging
from enum import Enum

class NoValue(Enum):
     def __repr__(self):
         return '<%s.%s>' % (self.__class__.__name__, self.name)

from almdrlib.client import Client

def set_logger(name='almdrlib', level=logging.DEBUG, format_string=None):
    """
    Add a stream handler for the given name and level to the logging module.
    By default, this logs all almdrlib messages to ``stdout``.
        >>> import almdrlib
        >>> almdrlib.set_logger('almdrlib.client', logging.INFO)
    For debugging purposes a good choice is to set the stream logger to ``''``
    which is equivalent to saying "log everything".

    :type name: string
    :param name: Log name
    :type level: int
    :param level: Logging level, e.g. ``logging.INFO``
    :type format_string: str
    :param format_string: Log message format
    """

    if format_string is None:
        format_string = "%(asctime)s %(name)s [%(levelname)s] %(message)s"

    logger = logging.getLogger(name)
    logger.setLevel(level)
    handler = logging.StreamHandler()
    handler.setLevel(level)
    formatter = logging.Formatter(format_string)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

def create_client(service_name, version = None, session = None, *args, **kwargs):
    return Client(service_name, version, session, *args, **kwargs)


# Logging to dev/null
# http://docs.python.org/3.3/howto/logging.html#configuring-logging-for-a-library
class NullHandler(logging.Handler):
    def emit(self, record):
        pass


logging.getLogger('almdrlib').addHandler(NullHandler())