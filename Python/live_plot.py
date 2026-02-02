import serial
## import pandas as pd
import matplotlib.pyplot as plot
import matplotlib.animation as animation


#odprtje seriskega porta
serial_py = serial.Serial('COM3', 115200, timeout=1)

# seznami za shranjevanje meritev
time_data = []
temp_data = [] 
hum_data = []

def update(frame):
    # branje vrstice iz porta
    line = serial_py.readline().decode(errors="ignore").strip()

    # preskoči, razbija in preverja vrstice
    if not line:
        return

    parts = line.split(",")

    if len(parts) != 3:
        print("Skipped:", line)
        return

    # razpakiranje, unpack, vrednosti
    time, temp, hum = parts

    # spet preverjanje, if ValueError
    try:
        time = int(time)
        temp = float(temp)
        hum = float(hum)
    except ValueError:
        return

    # dodaj podatke v seznam
    time_data.append(time / 1000.0)
    temp_data.append(temp)
    hum_data.append(hum)


    if len(time_data) > 50:
        time_data.pop(0)
        temp_data.pop(0)
        hum_data(0)

    plot.cla() # očisti graf

    # risanje obe krivulji
    plot.plot(time_data, temp_data, label="Temperature (C)", color="red")
    plot.plot(time_data, hum_data, label="Humidity (%)", color="blue")

    plot.xlabel("Time (s)")
    plot.ylabel("Value")
    plot.title("Real-time Temperature & Humidity")
    plot.legend()
    plot.grid(True)

# Nastavitev grafa
fig= plot.figure()
ani = animation.FuncAnimation(fig, update, interval=200) # osvežitev vsakih 200 ms
plot.show()

serial_py.close()