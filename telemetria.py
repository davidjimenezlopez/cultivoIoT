import Adafruit_DHT
from cliente import Cliente
from sensor import Sensor

class Telemetria:

    def __init__(self):
        self.cliente = Cliente()
        self.sensor = Sensor()

    def iothub_client_telemetry_sample_run(self):  
        try:  
            
            print ( "Sending data to IoT Hub, press Ctrl-C to exit" )  
            while True: 
                msg_txt_formatted = self.sensor.obtenerDatos() 
                message = self.cliente.setMensaje(msg_txt_formatted) 
                self.cliente.send_message(message)
                print( "Sending message: {}".format(message) )  
                self.client.send_message(message)  
                print ( "Message successfully sent" )  
                time.sleep(3)  
                param='1024'
                self.crear_llave(param)
                
        except KeyboardInterrupt:  
            print ( "IoTHubClient stopped" )  

    def crear_llave(self, param):        
        param=1
        key = RSA.generate(1024)        
        f = open('mykey.pem','wb')
        f.write(key.export_key('PEM'))        
        f.close()
        f = open('mykey.pem','r')
        key = RSA.import_key(f.read())
        narg=len(sys.argv)

    
    if __name__ == '__main__':
        medida = Telemetria()
        print('Se ha agregado el usuario Abbas con id id ', person.set_name('Abbas'))
        print('User associated with id 0 is ', person.get_name(0))
     