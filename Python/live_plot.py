import serial
import pandas as pd

#odprtje seriskega porta
serial_py = serial.Serial('COM3', 115200, timeout=1)
data = [] # seznam za shranjevanje meritev

while True:
    # branje vrstice iz porta
    line = serial_py.readline().decode(errors="ignore").strip()

    # preskoči, razbija in preverja vrstice
    if not line:
        continue

    parts = line.split(",")

    if len(parts) != 3:
        print("Skipped:", line)
        continue

    # razpakiranje, unpack, vrednosti
    time, temp, hum = parts

    # spet preverjanje, if ValueError
    try:
        temp = float(temp)
        hum = float(hum)
    except ValueError:
        continue

# prikaz 50 meritev
    data.append([int(time), temp, hum])
    print("OK:", time, temp, hum)

    if len(data) >= 50:
        break

# ustvarjanje tabele, DataFrame iz data, za analizo ali grafe, shranjeno v CSV datoteko,za Excel, Jupyter
df = pd.DataFrame(data, columns=["time_ms", "temperature", "humidity"])
df.to_csv("measurements.csv", index=False)

serial_py.close()