'''
Created on Apr 16, 2018

@author: yoges
'''

import paho.mqtt.client as mqtt
import time

connflag = False    

    
def on_connect(client, userdata, flags, rc):
    global connflag
    connflag = True
    print("Connected with result code " + str(rc))


def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload) + " received payload")


def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Disconnection failure")


def on_subscribe(client, userdata, mid, granted_qos):
    print ("client" + client 
               + "user data" + userdata
               + "mid" + mid
               + "granted_qos" + granted_qos)

    
def on_publish(client, userdata, mid):
    print ("client" + client 
               + "user data" + userdata
               + "mid" + mid)
        
   
def MqttConnect(topic, payload):
            
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    
    host = 'iot.eclipse.org'
    port = 1883
    
    client.connect(host, port, keepalive=60)
 
    client.loop_start()
    time.sleep(1)    
    client.publish(topic, payload, 2)
    print (" Published : Payload " + payload)
   
    client.loop_stop()

    
def main():

    MqttConnect("house/bulb1", "testing")
 
    
if __name__ == '__main__':
    main()
