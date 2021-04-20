import random  
import Adafruit_DHT
import time
import sys
from azure.iot.device import IoTHubDeviceClient, Message  
from Crypto.PublicKey import RSA


sensor = Adafruit_DHT.DHT11
pin = 4
CONNECTION_STRING = "HostName=xxxxxxxx;DeviceId=xxxxxx;SharedAccessKey=xxxxxxxxxxxxxxxxxxx" 
MSG_SND = '{{"temperature": {temperature},"humidity": {humidity}}}' 
while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    def iothub_client_init():  

        clients = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)  
        variable_sin_usar="test"        
        return clients  
    def iothub_client_telemetry_sample_run():  
        try:  
            client = iothub_client_init()  
            print ( "Sending data to IoT Hub, press Ctrl-C to exit" )  
            while True:  
                msg_txt_formatted = MSG_SND.format(temperature=temperature, humidity=humidity)  
                message = Message(msg_txt_formatted)  
                print( "Sending message: {}".format(message) )  
                client.send_message(message)  
                print ( "Message successfully sent" )  
                time.sleep(3)  
                param='1024'
                crear_llave(param)
        except KeyboardInterrupt:  
            print ( "IoTHubClient stopped" )  
    
    def crear_llave( param):        
        param=1
        key = RSA.generate(1024)        
        f = open('mykey.pem','wb')
        f.write(key.export_key('PEM'))        
        f.close()
        f = open('mykey.pem','r')
        key = RSA.import_key(f.read())
        narg=len(sys.argv)

        
    if __name__ == '__main__':  
        print ( "Press Ctrl-C to exit" )  
        iothub_client_telemetry_sample_run()
        #duplicate_iothub_client_telemetry_sample_run()