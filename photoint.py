# CircuitPython IO demo #1 - General Purpose I/O
import time
import board
from digitalio import DigitalInOut, Direction, Pull

led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

# For Gemma M0, Trinket M0, Metro M0 Express, ItsyBitsy M0 Express,
switch = DigitalInOut(board.D2)
# switch = DigitalInOut(board.D5)  # For Feather M0 Express, Feather M4 Express
# switch = DigitalInOut(board.D7)  # For Circuit Playground Express
switch.direction = Direction.INPUT
switch.pull = Pull.UP
counter = 0
lastswitch = False
while True:
    # We could also do "led.value = not switch.value"!
    if switch.value:
        led.value = False
    else:
        led.value = True
    if switch.value and not lastswitch:
        counter += 1
        print("I have been interrupted " + str(counter) + " times")
    lastswitch = switch.value
    print(time.monotonic())
    time.sleep(1)