"""Level Home Device Manager Library."""
import logging

from level.dwelling.dwelling import Dwelling
from level.hub.hub import Hub

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s.%(msecs)03d %(levelname)s [%(module)s]: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',)
