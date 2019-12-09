import time
import RPi.GPIO as GPIO

class Servomotor:
    """
    Expected to use SG-90, SG-5010.
    """
    def __init__(self, port, mode=GPIO.BCM, duty_min=2.5, duty_max=12.0, degree_range=180, pwm_cycle=50):
        self.port = port
        self.mode = mode
        self.duty_min = duty_min
        self.duty_max = duty_max
        self.degree_range = degree_range
        self.pwm_cycle = pwm_cycle

        GPIO.setmode(self.mode) # default:役割ピン番号を指定
        GPIO.setup(self.port, GPIO.OUT)
        self.p = GPIO.PWM(self.port, pwm_cycle)
        self.p.start(0.0)
    
    def servooff(self):
        self.p.ChangeDutyCycle(0.0)
        time.sleep(0.2)

    def changedutycycle(self, dutycycle, lock=False):
        self.p.ChangeDutyCycle(dutycycle)
        time.sleep(1.0)
        if not lock:
            self.servooff()
    
    def changedegree(self, degree, lock=False):
        self.changedutycycle(self.duty_min + (self.duty_max - self.duty_min) / self.degree_range * (degree + 90), lock)

    def __del__(self):
        GPIO.cleanup()
