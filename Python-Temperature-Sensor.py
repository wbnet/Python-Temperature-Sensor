import time
import board
import adafruit_dht

newTime = oldTime = time.time()
newTemp = oldTemp = 0.0
x = 0

# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT22(board.D4)

while True:
    try:
        # Print the values to the serial port
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        print(
            "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                temperature_f, temperature_c, humidity
            )
        )

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])

    oldTime = newTime
    oldTemp = newTemp

    newTime = time.time()
    newTemp = temperature_c

    timeDelta = newTime - oldTime
    tempDelta = newTemp - oldTemp

    timeDelta = round(timeDelta, 2)
    tempDelta = round(tempDelta, 2)

    print()

    if x > 0:
        print("Time since last reading (s)")
        print(timeDelta)
        print()

        print("Temperature change since last reading (degree C)")
        print(tempDelta)
        print()

    x += 1
    # print()

    for y in range(2):
        print()

    time.sleep(4.0)
