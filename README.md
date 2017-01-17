# Phillips Hue RFID
This program uses the phue library found here: https://github.com/studioimaginaire/phue the MFRC522 library found here: https://github.com/mxgxw/MFRC522-python and the SPI-Py library found here: https://github.com/lthiery/SPI-Py.git

This tutorial is based off of [Sunfounder's](https://www.sunfounder.com/wiki/index.php?title=How_to_Use_an_RFID_RC522_on_Raspberry_Pi#Enable_Device_Tree) tutorial.
##Hardware
To read the RFID tags we will be using a RFID-RC522 reader. You can find many of these cheap readers on [Ebay](http://www.ebay.co.uk/sch/i.html?_from=R40&_trksid=p2050601.m570.l1313.TR1.TRC0.A0.H0.Xrfid-rc522.TRS0&_nkw=rfid-rc522&_sacat=0)

Using Female to Female (or Male to female if you have your reader on a breadboard) jumper wires connect your reader using the following pins

|Name      |Pin #|Pin Name  |
|----------|-----|----------|
|VCC (3.3v)|1    |3V3       |
|RST       |22   |GPIO 25   |
|GND       |Any  |Any Ground|
|IRQ       |None |None      |
|MISO      |21   |GPIO 9    |
|MOSI      |19   |GPIO 10   |
|SCK       |23   |GPIO 11   |
|SDA       |24   |GPIO 8    |

##RFID Reader Setup
###SPI Setup
Run raspi-config by running `sudo raspi-config` in the terminal. 
Navigate through 5 Interfacing options -> P4 SPI -> Yes -> OK -> Finish

After that, reboot the pi by running `sudo reboot`
###Install python-dev and git
```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python-dev git
```
###Install SPI-Py
```
git clone https://github.com/lthiery/SPI-Py.git
cd SPI-Py/
sudo python setup.py install
```
###Install MFRC522-python library
```
cd 
git clone https://github.com/mxgxw/MFRC522-python.git
cd MFRC522-python/
```
