from phue import Bridge
import logging
logging.basicConfig()

b = Bridge('192.168.1.218')

b.connect()

