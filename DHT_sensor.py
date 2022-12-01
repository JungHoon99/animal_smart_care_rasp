import adafruit_dht
import board
import time

class degree:
    degree = 0
    humidity = 0
    def __init__(self):
        self.dht = adafruit_dht.DHT11(board.D22)
        
    def getDegree(self):
        try:
            self.degree = self.dht.temperature
        except:
            return self.degree
        if(self.degree == None):
            return 0
        else:
            return self.degree
        
    def getHumidity(self):
        try:
            self.humidity = self.dht.humidity
        except:
            return self.humidity
        if(self.humidity == None):
            return 0
        else:
            return self.humidity
        
    def close(self):
        self.dht.exit()