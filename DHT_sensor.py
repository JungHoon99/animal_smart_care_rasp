import adafruit_dht
import board
import time

dht = adafruit_dht.DHT11(board.D22)

for i in range(10):
    try:
        print(i+1,"test")
        print("degree" , dht.temperature)
        print("humidity", dht.humidity)
    except:
        continue
    time.sleep(1)
dht.exit()