'''
Created on Apr 16, 2018

@author: yogesh
'''
import socket
import random
import json

from datetime import datetime 
from coapthon.client.helperclient import HelperClient
from coapthon.utils import parse_uri
'''
Definition for a CoAP communications client, with embedded test functions.
'''


class CoapCommClient:
    '''
    Initialization of class.
    '''

    def __init__(self, host, port, path):
        
        if host and not host.isspace():
            self.host = host
        else:
            self.host = "localhost"

        if port >= 1024:
            self.port = port
        else:
            self.port = 5683
        
        self.serverAddr = (self.host, self.port)
        
        if path and not path.isspace():
            self.path = path
        else:
            self.path = "test"
            
        self.url = "coap://" + self.host + ":" + str(self.port) + "/" + self.path

        try:
            print("Parsing URL: " + self.url)
            
            self.host, self.port, self.path = parse_uri(self.url)
            
            tmpHost = socket.gethostbyname(self.host)

            if tmpHost:
                self.host = tmpHost
            else:
                print("Can't resolve host: " + self.host)
                pass
        except socket.gaierror:
            print("Failed to resolve host: " + self.host)
    
    '''
    Initializes the client. This is expected to be called prior to every
    client call
    '''

    def initClient(self):
        try:
            self.client = HelperClient(server=(self.host, self.port))

            print("Created CoAP client ref: " + str(self.client))
            print(" coap://" + self.host + ":" + str(self.port) + "/" + self.path)
        except Exception:
            print("Failed to create CoAP helper client reference using host: " + self.host)
            pass

    '''
    Test function definition for discover.
    '''

    def handleDiscoverTest(self):
        print("Testing discover...")
        
        self.initClient()
        
        response = self.client.discover(timeout=5)
        
        if response:
            print(response.pretty_print())
        
            # get the payload and convert to a list of paths
            self.pathList = response.payload.split(",")
            index = 0

            for path in self.pathList:
                startTemp = path.find('</', 0, len(path))
                endTemp = path.find('>', 0, len(path))

                self.pathList[index] = path[startTemp + 2:endTemp]

                print(" Path entry [" + str(index) + "]:" + self.pathList[index])
                index += 1
        else:
            print("No response received.")
        
        self.client.stop()

    '''
    Test function definition for GET.
    '''

    def handleGetTest(self, path):
        self.initClient()
        if not path and self.pathList:
            for pathEntry in self.pathList:
                print("Testing GET with path entry: " + pathEntry)
            
                response = self.client.get(pathEntry)
            
                if response:
                    print(response.pretty_print())
                else:
                    print("No response received for GET on path entry: " + pathEntry)
        elif path:
            print("Testing GET with path: " + path)

            response = self.client.get(path)

            if response:
                print(response.pretty_print())
            else:
                print("No response received for GET on path: " + path)
        else:
            print("Can't test GET - no path or path list provided.")

        self.client.stop()

    '''
    Test function definition for POST.
    '''

    def handlePostTest(self, path, payload):
        print("Testing POST with path: " + path + ", payload: " + payload)
        self.initClient()
        
        response = self.client.post(path, payload)
        if response:
            print(response.pretty_print())
        else:
            print("No response received.")
    
        self.client.stop()
    
    '''
    Test function definition for PUT.
    '''

    def handlePutTest(self, path, payload):
        print("Testing PUT with path: " + path + ", payload: " + payload)
    
        self.initClient()
    
        response = self.client.put(path, payload)

        if response:    
            print(response.pretty_print())
        else:
            print("No response received.")

        self.client.stop()

    '''
    Test function definition for DELETE.
    '''

    def handleDeleteTest(self, path):
        print("Testing DELETE with path: " + path)
    
        self.initClient()

        response = self.client.delete(path)
    
        if response:
            print(response.pretty_print())
        else:
            print("No response received.")
    
        self.client.stop()

    '''
    Runs all test functions.
    '''

    
    def runTests(self):
        # execute tests
        print("Executing all CoAP comm tests...")
        payloadtest = "Smart Lighting System"
        cloudApiPath = "Bluemix"
        actApiPath = "Trigger"
        '''
        NOTE: each call must be made with a new client!
        '''
        self.handleDiscoverTest()
        self.handleGetTest(None)
        for i in range(1, 6):
          
            payloadCloud = self.payloadJsonCreate()
            
            self.handlePostTest(actApiPath, payloadCloud)
            self.handlePostTest(cloudApiPath, payloadCloud)

        #Below methods to test put & delete 
        #These request type are not required for current usecase
        #Might be useful in future scope
            
        #self.handlePutTest(actApiPath, payloadtest)
        #self.handleDeleteTest(actApiPath)

    
    def sensorData(self):
        print("sensor data")
        val = random.randint(0, 1)
        return val

    def payloadJsonCreate(self):
        time = str(datetime.now())
        sensorVal = self.sensorData()
        newJson = {'Group Name':'Home Automation','Name':'SHoLS',
                    'Location':'Home','TimeStamp':time,'SensorData':sensorVal}
        
        payJson = json.dumps(newJson)
        
        return payJson

'''
Main function definition for running client as application.
'''


def main():
    coapClient = CoapCommClient("localhost", 5683, "test")
    coapClient.runTests()


'''
Attribute definition for when invoking as app via command line
'''
if __name__ == '__main__':
    main()
