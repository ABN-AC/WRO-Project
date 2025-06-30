# hardware_interfaces.py

import time
import Adafruit_PCA9685
import RPi.GPIO as GPIO
import cv2

# --- Setup PCA9685 ---
pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)

# --- Servo Control (Channel 0 for MG996R) ---
def set_steering(angle):
    # Map angle (0–180) to PWM pulse (e.g., 150–600)
    pulse = int((angle / 180.0) * 450) + 150
    pwm.set_pwm(0, 0, pulse)

# --- Motor Control (Cytron MD10C via GPIO) ---
motor_pwm_pin = 18  # PWM pin
motor_dir_pin = 23  # Direction pin

GPIO.setmode(GPIO.BCM)
GPIO.setup(motor_pwm_pin, GPIO.OUT)
GPIO.setup(motor_dir_pin, GPIO.OUT)

motor_pwm = GPIO.PWM(motor_pwm_pin, 1000)
motor_pwm.start(0)

def set_motor(speed):
    direction = GPIO.HIGH if speed >= 0 else GPIO.LOW
    GPIO.output(motor_dir_pin, direction)
    motor_pwm.ChangeDutyCycle(min(abs(speed), 100))

# --- Ultrasonic Sensor Setup (HC-SR04) ---
TRIG = 5
ECHO = 6

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def get_distance():
    GPIO.output(TRIG, False)
    time.sleep(0.01)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150  # cm
    return round(distance, 2)

# --- Camera Init (CSI) ---
def init_camera():
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)  # Width
    cap.set(4, 480)  # Height
    return cap
