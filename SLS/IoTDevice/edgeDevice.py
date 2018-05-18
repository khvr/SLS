import paho.mqtt.client as mqtt
import json

#Group Integration Common Variable

ProximityData = 0
illuminanceData = 1

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("CLOUD")
    client.subscribe("Trigger")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    #print(msg.topic+" "+str(msg.payload))
    #global ProximityData 
    #global illuminanceData 
    if(msg.topic != "ACT"):
        jsonToDic = json.loads(msg.payload)
        grpChck = jsonToDic['Name']
        #Actuation part 
        if(grpChck == "SLS"):
            print("The Data is "+ str(jsonToDic['SensorData']))
            illumianceData = jsonToDic['SensorData']    
        elif grpChck == 'SHOLS' :
            print("The Data is from team " + str(jsonToDic['SensorData']))
    else :
        print(msg.topic+" "+str(msg.payload))
        ProximityData = 1 
    groupIntegration()
    
def groupIntegration():
    #global ProximityData 
    #global illuminanceData
    if(illuminanceData == 3):
        if(ProximityData == 0):
            print("Turn off the light")
        else:
            print("Turn on the light with medium intensity")
    elif(illuminanceData > 3):
        if(ProximityData == 0):
            print("Turn off the light")
        else:
            print("Turn on the light with low intensity")
    elif(illuminanceData < 3):
        if(ProximityData == 0):
            print("Turn on the light with low intensity")
        else:
            print("Turn on the light with High intensity")
    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("iot.eclipse.org", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()

client.disconnect()
