import RPi.GPIO as GPIO
import time

class servo:
    def __init__(self):
        self.waterPin = 18
        self.feedPin = 23
        self.waterDegree = 120
        self.feedDegree = 30
        
    def WaterOpen(self):
        self.servoMotor(self.waterPin, self.waterDegree-90, 2.5)
        self.servoMotor(self.waterPin, self.waterDegree, 2)
        
    def FeedOpen(self):
        self.servoMotor(self.feedPin, self.feedDegree+90, 2.5)
        self.servoMotor(self.feedPin, self.feedDegree, 2)
        
    def servoMotor(self, pin, degree, t):
        #GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
        pwm=GPIO.PWM(pin, 50)

        pwm.start((0.054*degree)+3.0)
        time.sleep(t)

        pwm.stop() 
        GPIO.cleanup(pin)
