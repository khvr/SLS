'''
Created on Apr 17, 2018

@author: yoges
'''
import paho.mqtt.client as mqtt
import time
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    #client.publish("house/bulb1","Hinew",2)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
print("1")

client = mqtt.Client()

#print("Connected with result code "+str(rc))
client.connect("iot.eclipse.org", 1883, 60)
#client.publish("house/bulb1","Hi1",2)
client.on_connect = on_connect
print("2")
client.on_message = on_message
print("3")
client.publish("house/bulb1","Hinew",2)
print("4")
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
#client.loop_forever()
client.loop_start()
time.sleep(1)
client.loop_stop()

