import RPi.GPIO as GPIO
import time

def servoMotor(pin, degree, t):
    id(degree>=0 and degree<=180)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    pwm=GPIO.PWM(pin, 50)

    pwm.start((0.054*degree)+3.0)
    time.sleep(t)
    
    pwm.ChangeDutyCycle(3.0)
    time.sleep(t)
    
    pwm.ChangeDutyCycle(3.0)

    pwm.stop() 
    GPIO.cleanup(pin)

degree = 90
# how to use function
for i in range(3):
    servoMotor(12, degree, 2.5)
    servoMotor(16, degree, 2.5)
    degree+=30
