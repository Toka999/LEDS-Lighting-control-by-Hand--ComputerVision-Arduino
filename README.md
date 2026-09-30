Hand-Controlled LED System with Python, MediaPipe, and ArduinoA real-time computer vision project that tracks hand gestures via webcam, counts the number of raised fingers using Python, OpenCV, and MediaPipe, and sends commands to an Arduino microcontroller using PyFirmata to control an array of LEDs dynamically.🌟 FeaturesReal-Time Hand Tracking: Utilizes Google's MediaPipe framework for accurate and fast hand landmark detection.Dynamic Finger Counting: Detects how many fingers are actively raised (0 to 5).Firmata Protocol Integration: Communicates seamlessly between Python and Arduino without needing custom C++ serial parsing code on the Arduino side.Interactive LED Control: Maps the finger count directly to hardware LEDs (e.g., 1 raised finger turns on 1 LED, 2 fingers turn on 2 LEDs, and a rock hand or zero fingers turns all LEDs off).🛠️ Tech Stack & HardwareSoftware & LibrariesPython 3.xOpenCV (cv2): For video capture and frame rendering.MediaPipe: For hand detection and landmark extraction.PyFirmata: For controlling Arduino digital pins directly from Python.Arduino IDE: To flash the StandardFirmata firmware onto the Arduino.Hardware ComponentsArduino Board (Uno, Nano, Mega, etc.)USB Cable (for connection and serial communication)5 x LEDs5 x 220Ω ResistorsBreadboard and Jumper Wires📋 Wiring DiagramConnect your LEDs to the digital output pins on your Arduino. For a standard 5-LED setup:LEDArduino Digital PinLED 1Pin 2LED 2Pin 3LED 3Pin 4LED 4Pin 5LED 5Pin 6Make sure each LED's anode (long leg) connects to the digital pin through a 220Ω resistor, and the cathode (short leg) connects to the Arduino's Ground (GND).⚙️ Setup and InstallationStep 1: Prepare the ArduinoOpen the Arduino IDE.Connect your Arduino board to your computer via USB.Navigate to File > Examples > Firmata > StandardFirmata.Select your correct Board and Port under Tools, then click Upload to flash the firmware.Step 2: Clone or Download the ProjectBashgit clone https://github.com/your-username/hand-controlled-led-arduino.git
cd hand-controlled-led-arduino
Step 3: Install Python DependenciesInstall the required Python packages using pip:Bashpip install opencv-python mediapipe pyfirmata
🚀 How to Run the ProjectConnect your Arduino to your computer.Open the main Python script and update the Arduino port variable to match your system port (e.g., 'COM3' on Windows or '/dev/cu.usbmodemXXXX' on macOS/Linux):Pythonboard = Arduino('COM3')  # Change to your actual port
Run the Python script:Bashpython main.py
Position your hand in front of your webcam:0 Fingers / Rock Hand: All LEDs are turned OFF.1 to 5 Fingers: Corresponding number of LEDs light up sequentially.Press q on your keyboard to quit the application.
📂 Project Structure
Your project contains the following files and directories:

Plaintext
├── hand_tracker.py          # Main script for camera capture, MediaPipe tracking, and logic
├── controller.py            # Handles communication logic with the Arduino board
├── arduinocontrol.py        # Supplementary script for hardware control commands
├── finger tracker.py        # Alternative or modular script for finger detection
├── finger tracker.html      # HTML documentation or web visualization file
├── hand.code-profile        # VS Code profile settings for the project
├── *.png / *.jpg            # Circuit diagrams, hand landmarks, and project screenshots
├── LED hand controller project.docx # Project report / documentation
└── __pycache__/             # Python compiled bytecode cache