



# ✋💡 Hand Gesture LED Controller

Control LEDs with your bare hand. A webcam tracks your hand in real time using **Python, OpenCV and MediaPipe**, counts how many fingers are raised, and sends that number to an **Arduino** through **PyFirmata**. The Arduino turns on exactly that many LEDs.

| Gesture | Result |
|---------|--------|
| ☝️ 1 finger raised | 1 LED on |
| ✌️ 2 fingers raised | 2 LEDs on |
| 🤟 3 fingers raised | 3 LEDs on |
| 🖖 4 fingers raised | 4 LEDs on |
| 🖐️ 5 fingers raised | 5 LEDs on |
| ✊ Fist (rock hand, 0 fingers) | All LEDs off |

---

## 🎬 Demo

<video src="[Real-demo.mp4](https://github.com/user-attachments/assets/1297c73d-de85-45e0-89a9-59d5062d7f1c)" controls muted width="100%"></video>

> If the player does not load in your viewer, [click here to watch the demo]([Real-demo.mp4](https://github.com/user-attachments/assets/1297c73d-de85-45e0-89a9-59d5062d7f1c])).

---

## 🧠 How It Works

```
Webcam ──► OpenCV (capture + flip + BGR→RGB)
              │
              ▼
        MediaPipe Hands (21 landmarks per hand)
              │
              ▼
   Compare fingertip vs. joint positions ──► count raised fingers
              │
              ▼
   PyFirmata (serial) ──► Arduino (StandardFirmata, C++) ──► LEDs
```

1. **OpenCV** (`cv2`) reads frames from the camera and mirrors them horizontally.
2. Each frame is converted from BGR to RGB and passed to **MediaPipe Hands**, which returns 21 landmarks per detected hand.
3. The pixel position of every landmark is computed and stored in a list (`lmList`).
4. A finger is considered **raised** when its tip landmark (IDs `4, 8, 12, 16, 20`) is above the joint below it (smaller `y` value).
5. The finger count is sent to the Arduino using **PyFirmata**, which sets the matching digital pins HIGH or LOW.
6. The Arduino runs the standard **Firmata firmware** (C++ sketch), so no custom Arduino code is needed.

---

## 🧰 Hardware Required

- Arduino Uno / Nano / Mega (any board that supports Firmata)
- 5 × LEDs
- 5 × 220 Ω resistors
- Breadboard and jumper wires
- USB cable
- Webcam (built-in or external)

### Wiring

Connect each LED (long leg/anode) through a 220 Ω resistor to a digital pin, and the short leg (cathode) to GND.

| LED | Arduino Pin |
|-----|-------------|
| LED 1 | D8 |
| LED 2 | D9 |
| LED 3 | D10 |
| LED 4 | D11 |
| LED 5 | D12 |

> 📝 Pin numbers are examples. Change them in the code to match your circuit.

---

## 💻 Software Requirements

- **Python 3.9 – 3.11** (recommended: 3.11)
- Arduino IDE
- Python packages:
  - `opencv-python`
  - `mediapipe`
  - `pyfirmata`
  - `pyserial`

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/hand-tracker.git
cd hand-tracker
```

### 2. Install Python dependencies

```bash
pip install opencv-python mediapipe pyfirmata pyserial
```

### 3. Upload Firmata to the Arduino (C++)

1. Open the **Arduino IDE**.
2. Go to **File → Examples → Firmata → StandardFirmata**.
3. Select your board and COM port, then click **Upload**.

### 4. Set your COM port

Find your port in the Arduino IDE (**Tools → Port**) or Windows Device Manager, then update it in the Python code:

```python
board = pyfirmata.Arduino('COM3')   # Windows
# board = pyfirmata.Arduino('/dev/ttyACM0')   # Linux
# board = pyfirmata.Arduino('/dev/cu.usbmodem14101')   # macOS
```

---

## ▶️ Usage

1. Connect the Arduino and make sure Firmata is uploaded.
2. Close the Arduino IDE Serial Monitor (it blocks the port).
3. Run the program:

   ```bash
   python hand_tracker.py
   ```

4. Show your hand to the camera and raise fingers.
5. Press **`q`** in the video window to quit.

---

## 📁 Project Structure

```
hand tracker/
├── hand_tracker.py      # Main program: camera, MediaPipe, finger counting
├── tracker/
│   ├── controller.py    # Arduino / LED control functions
│   ├── finger tracker.py
│   └── ...
├── arduinocontrol.py    # Arduino communication helpers
├── Real-demo.mp4        # Demo video
└── README.md
```

---

## 🛠️ Troubleshooting

| Problem | Fix |
|---------|-----|
| `mediapipe` or `pyfirmata` fails to install or import | Use Python 3.9–3.11. Newer versions (3.12+) are often unsupported. |
| `AttributeError: module 'collections' has no attribute 'Mapping'` | Use `pip install pyfirmata2` and `import pyfirmata2 as pyfirmata`, or patch `pyfirmata`. |
| `SerialException: could not open port` | Wrong COM port, or another program (Serial Monitor) is using it. |
| Camera does not open | Change the camera index: `cv2.VideoCapture(1)`. |
| Wrong finger count | Keep your palm facing the camera with good lighting. Thumb detection is the most sensitive. |
| LEDs don't light up | Check LED polarity, resistors, and pin numbers. |

---

## 🚀 Future Improvements

- Support for two hands (up to 10 LEDs)
- Control LED brightness with PWM using finger distance
- Gesture-based control of motors and relays
- Simple GUI for selecting the port and pins

---

## 🧾 Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?logo=opencv&logoColor=white)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0097A7?logo=google&logoColor=white)
![Arduino](https://img.shields.io/badge/Arduino-00979D?logo=arduino&logoColor=white)
![C++](https://img.shields.io/badge/C++-00599C?logo=cplusplus&logoColor=white)

---

## 📄 License

This project is licensed under the MIT License. Feel free to use, modify, and share it.

---

## 🙌 Acknowledgements

- [MediaPipe](https://developers.google.com/mediapipe) for hand landmark detection
- [OpenCV](https://opencv.org/) for computer vision
- [PyFirmata](https://github.com/tino/pyFirmata) and the Firmata protocol for Python–Arduino communication
