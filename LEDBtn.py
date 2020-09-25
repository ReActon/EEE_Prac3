#import GPIO lib to configure LED
import RPi.GPIO as GPIO
#import sleep to enable LED to blink
from time import sleep

#configure mode for chosen pin values
GPIO.setmode(GPIO.BCM)

