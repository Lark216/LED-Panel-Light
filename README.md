3D Printed Panel Light

A compact, single NeoPixel GRBW panel light powered by an **Adafruit KB2040** microcontroller and written in **CircuitPython**.  
This project creates a soft, diffused white light—perfect for desktop accent lighting or art illumination.

---
Features
- Uses a **single GRBW NeoPixel** for a bright, pure white light.
- Runs on **CircuitPython**, easy to modify or expand.
- Designed to fit a **3D printed panel housing** (see image below).
- Fully customizable color and brightness.

---

 Hardware Used
- **Adafruit KB2040** (RP2040 microcontroller)  
- **NeoPixel GRBW** LED (1 pixel)  
- **3D printed panel enclosure**  
- Optional: Diffuser panel or frosted acrylic cover  

---

 Wiring Diagram
| KB2040 Pin | Component        | Description              |
|-------------|------------------|--------------------------|
| D5          | NeoPixel Data In | Control signal to LED    |
| 3V          | NeoPixel VCC     | Power                    |
| GND         | NeoPixel GND     | Ground                   |

> ⚠️ Ensure you power the NeoPixel from **3V or 5V** depending on your LED specifications.  

---

 CircuitPython Code

Save this file to your KB2040 as **`code.py`**:

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
