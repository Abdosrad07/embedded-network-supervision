# Mini Embedded Network Supervision System

## Overview

This project implements a miniature network supervision architecture based on an embedded node and a monitoring
server.

An embedded device built with an Arduino Uno generates structured data frames and transmits them with UART.
A Python-based supervision server receives, parses, analyses, and visualizes the data in real time.

The objective is to demonstrate core concepts of network supervision applied to embedded systems.

---

## System Architecture

The system is composed of two main components:

### 1. Embedded Node
-   Generates periodic data
-   Encapsulates data in a structured frame
-   Sends frames over UART (USB)
Frame format:
<START>|ID:01|DATA:27|TIME:54321|<END>

### 2. Supervision Server
-   Reads serial port
-   Detects frame boundaries
-   Extracts DATA field
-   Stores values in a circular buffer
-   Computes a moving average
-   Detcts threshold anomalies
-   Displays real-time graph

---

## Technical Concepts
-   UART communication
-   Custom application-layer protocol
-   Serial frame parsing(regex)
-   Circular buffer (deque)
-   Moving average computation 
-   Threshold-based anomaly detection
-   Real-time data visualization

## Hardware Requirements
-   Arduino Uno
-   USB cable
-   LED
-   220 ohms resistor
-   Computer (Windows/Linux/macOS)

---

## Software Requirements
-   Arduino IDE
-   Python 3
-   Required Python libraries: pyserial and matplotlib
-   Or install automatically: pip install -r requirements.txt

---

## How to Run

### Step 1 - Flash the Arduino
Upload the `arduino_node.ino` file located in the `/embedded` directory.

### Step 2 - Configure Serial Port
Edit the supervision script:
Examples:
    - Windows : COM5
    - Linux : /dev/ttyUSB0
    - macOS : /dev/tty.usbserial

### Step 3 - Launch Supervision
python supervision/supervision_graphique.py

The supervision console will start and a real-time graph will appear

---

## Output

The system provides:

- Live DATA plotting
- Moving average visualization
- Console alerts when threshold exceeded
- Real-time monitoring behaviour

---

## Demonstration
A demonstration video showing:

- Hardware setup
- Frame transmission
- Real-time parsing
- Live graphical monitoring

(Video link here)

---

## Results

The project demonstrates:

- Stable data acquisition over UART
- Structured frame parsing
- Real-time monitoring capability
- Basic anomaly detection logic

This architecture reflects simplified principles used in industrial network supervision systems.

---

## Future Improvements 
- Timestamping on PC side
- CSV export
- Multi-node supervision
- Packet loss simulation
- Advanced statistical anomaly detection

## License
This project is licensed under the MIT License.

---

## Author
Embedded Systems & Telecommunications Enginnering Student
