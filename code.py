```python
import board
import neopixel
import time

# Configuration
NUM_PIXELS = 1
PIXEL_PIN = board.D5
BRIGHTNESS = 1.0

pixels = neopixel.NeoPixel(
    PIXEL_PIN,
    NUM_PIXELS,
    brightness=BRIGHTNESS,
    auto_write=False,
    pixel_order=neopixel.GRBW
)

# Turn off any previous color
pixels.fill((0, 0, 0, 0))

# Set light to pure white using the W channel
pixels[0] = (0, 0, 0, 255)

pixels.show()
