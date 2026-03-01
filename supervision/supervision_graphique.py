import serial
import re
import matplotlib.pyplot as plt
from collections import deque
import statistics

PORT = "COM5"
BAUDRATE = 9600

ser = serial.Serial(PORT, BAUDRATE, timeout=1)

print("Centre de supervision démarré...\n")

plt.ion()
fig, ax = plt.subplots()

data_buffer = deque(maxlen=50)
moyenne_buffer = deque(maxlen=50)

while True:
    line = ser.readline().decode(errors='ignore').strip()

    if "<START>" in line and "<END>" in line:
        match = re.search(r'DATA:(\d+)', line)

        if match:
            data_value = int(match.group(1))
            data_buffer.append(data_value)

            if len(data_buffer) > 1:
                moyenne = statistics.mean(data_buffer)
                moyenne_buffer.append(moyenne)
            
            # Affichage console
            print(f"DATA reçue : {data_value}")

            # Alerte simple
            if data_value > 35:
                print("ALERTE : Valeur élevée détectée")

            # Graphique
            ax.clear()
            ax.plot(data_buffer)
            ax.plot(moyenne_buffer)
            ax.set_title("Supervision du noeud embarqué")
            ax.set_xlabel("Echantillons")
            ax.set_ylabel("Valeur DATA")
            ax.legend(["Signal", "Moyenne glissante"])
            plt.pause(0.01)