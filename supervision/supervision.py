import serial
import re

PORT = "COM5"
BAUDRATE = 9600

ser = serial.Serial(PORT, BAUDRATE, timeout=1)

print("Supervision réseau démarrée...\n")

while True:
    line = ser.readline().decode(errors='ignore').strip()

    if "<START>" in line and "<END>" in line :
        print("Trame reçue :", line)

        # Extraction de DATA
        match = re.search(r'DATA:(\d+)', line)
        if match:
            data_value = int(match.group(1))
            print("Valeur extraite :", data_value)
            print("-"*40)

            if data_value > 35:
                print("ALERTE : Valeur élevée détectée")