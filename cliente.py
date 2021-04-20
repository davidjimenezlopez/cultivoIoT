from azure.iot.device import IoTHubDeviceClient,Message

class Cliente:
    
    CONNECTION_STRING = "HostName=xxxxxxxx;DeviceId=xxxxxx;SharedAccessKey=xxxxxxxxxxxxxxxxxxx" 

    def __init__(self):  
        self.conexion = IoTHubDeviceClient.create_from_connection_string(self.CONNECTION_STRING)  
        variable_sin_usar="test"
    
    def setMensaje(self,mensaje):
        return Message(mensaje) 

        

    