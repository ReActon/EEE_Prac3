#import GPIO lib to configure LED
import RPi.GPIO as GPIO
#import sleep to enable LED to blink
from time import sleep


def main():

	

	#configure mode for chosen pin values
	GPIO.setmode(GPIO.BCM)

	#a var to keep track of current number
	currentNum = 0
	#a var to monitor the endpoint
	endPoint = 4
	#a note of which GPIO pin belongs to the LED
	LEDPin = 22
	
	GPIO.setup(LEDPin, GPIO.OUT)


	while currentNum < endPoint:
		GPIO.output(LEDPin, True)
		sleep(2)
		GPIO.output(LEDPin, False)
		sleep(2)
		currentNum += 1


if __name__ == '__main__':
    main()
