#Run this program once to connect phue to your bridge

from phue import Bridge
import logging
logging.basicConfig()

b = Bridge('ip of your bridge')

b.connect()

