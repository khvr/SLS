import paho.mqtt.client as mqtt
import time


# The callback for when the client receives a CONNACK response from the server.
class MqttClient:
 
      
    def __init__(self):
        self.addr = "iot.eclipse.org"
        self.portno = 1883
        self.keepalive = 120
        print("MQtt mankatha")
    
    def client(self):
        client = mqtt.Client()
        return client
        
    def on_connect(self,client,topic, payload, flags, rc):
        
        print("Connected with result code "+str(rc))
        client.publish(topic,payload,2)
        
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
        #client.subscribe(topic)        

# The callback for when a PUBLISH message is received from the server.
    def on_message(self,client, userdata, msg):
        print(msg.topic+" "+str(msg.payload))


    def connect(self,client,addr,portno,keepalive):
        client.connect(addr, portno,keepalive )
        
    def disconnect(self,client):
        client.disconnect()
        
    def looping(self,client):
        client.loop_start()
        time.sleep(1)
        client.loop_stop()
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
def main():
    addr = "iot.eclipse.org"
    portno = 1883
    keepalive = 120
    client = mqtt.Client()
    client.connect(client, addr, portno,keepalive)
    client.on_connect = on_connect

if __name__ == '__main__':
    main()
    