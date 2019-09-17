import time
import touchio
import board
import pulseio
from adafruit_motor import servo

touch_A3 = touchio.TouchIn(board.A3)  # Not a touch pin on Trinket M0!
touch_A4 = touchio.TouchIn(board.A4)  # Not a touch pin on Trinket M0!
# create a PWMOut object on Pin A2.
pwm = pulseio.PWMOut(board.A2, duty_cycle=3 ** 15, frequency=40)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)
angle = 90

while True:
    my_servo.angle = angle
    if touch_A3.value:
        print("Touched A3!")
        if angle < 180:
            angle += 1
    if touch_A4.value:
        print("Touched A4!")
        if angle > 0:
            angle -= 1
    time.sleep(0.05)


# CircuitPython Demo - Cap Touch Multiple Pins
# Example does NOT work with Trinket M0!
