import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
 
GPIO.setup(4, GPIO.OUT)
 
p = GPIO.PWM(4, 50)
 
p.start(7.5)
 
try:
    while True:
        print("true")
        p.ChangeDutyCycle(7.5) # turn towards 90 degree
#         time.sleep(1) # sleep 1 second
#         p.ChangeDutyCycle(2.5) # turn towards 0 degree
#         time.sleep(1) # sleep 1 second
#         p.ChangeDutyCycle(12.5) # turn towards 180 degree
#         time.sleep(1) # sleep 1 second
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
