
import RPi.GPIO as GPIO
import MFRC522
import signal
from phue import Bridge
import time
import logging
logging.basicConfig()

#IP of Phillips Hue Bridge
b = Bridge('ip of your bridge')
continue_reading = True

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading = False
    GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

#Sets value of variable on to either True or False depending on whether the light is on or off
on = b.get_light(1, 'on')


# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:
    
    # Scan for cards    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
    
    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:
        # Print UID
        print "Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3])
        #If light is off turn light on
        if on == False:
            b.set_light(1,'on', True)
            on = True
        #If light is on turn light off
        elif on == True:
            b.set_light(1,'on', False)
            on = False
        time.sleep(2)

        


