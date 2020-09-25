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
    #a note of which GPIO pin the button is in
    buttonPin = 5	

    GPIO.setup(LEDPin, GPIO.OUT)
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    buttonPressed = True
    ledState = False
    try:	    
        while currentNum < endPoint:
            print("Press the button")
            buttonPressed = GPIO.input(buttonPin)
            if buttonPressed == False and ledState == False:
                GPIO.output(LEDPin, True)
                ledState = True
                sleep(3)
            elif buttonPressed == False and ledState == True:
                GPIO.output(LEDPin, False)
                ledState = False
                currentNum += 1
                sleep(0.5)
            sleep(0.1)
	        	
    finally:
        GPIO.cleanup()


if __name__ == '__main__':
    main()
