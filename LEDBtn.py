#import GPIO lib to configure LED
import RPi.GPIO as GPIO
#import sleep to enable LED to blink
from time import sleep

#configure mode for chosen pin values
GPIO.setmode(GPIO.BCM)

#a var to keep track of current number
currentNum = 0
#a var to monitor the endpoint
endPoint = 4
#a note of which GPIO pin belongs to the LED
LEDPin = 22

def main():
	GPIO.setup(LEDPin, GPIO.OUT)
	while currentNum < endPoint:

	sleep()


if __name__ == '__main__':
    main()
