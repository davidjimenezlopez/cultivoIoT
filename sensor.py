import Adafruit_DHT

class Sensor:
    
    sensor = Adafruit_DHT.DHT11
    pin = 4
    temperatura = 0
    humedad = 0

    def obtenerDatos(self):
        humedad, temperatura = Adafruit_DHT.read_retry(self.sensor, self.pin)
        return '{{"temperature": {temperatura},"humidity": {humedad}}}'.format(temperatura=temperatura, humedad=humedad)  
    
     
    