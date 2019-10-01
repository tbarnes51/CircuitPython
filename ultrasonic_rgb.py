import time
import board
import adafruit_hcsr04
import neopixel
led = neopixel.NeoPixel(board.NEOPIXEL, 1)
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)

while True:
    try:
        print((sonar.distance,))
    except RuntimeError:
        print("Retrying!")
    time.sleep(.4)
    dist = sonar.distance
    #led = led.fill

    time.sleep(0.05)
    if dist >= 35:
        led.fill((255, 0, 0))
    if dist >= 15 and dist <= 34:
        led.fill((0, 255, 0))
    if dist >= 3 and dist <= 14:
        led.fill((0, 0, 255))

# import neopixel
# led = neopixel.NeoPixel(board.NEOPIXEL, 1)
led.brightness = .5