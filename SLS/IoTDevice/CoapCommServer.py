'''
Created on Apr 16, 2018

@author: yogesh
'''
from coapthon.server.coap import CoAP
from IoTDevice.CloudCoapResource import CloudCoapResource
from IoTDevice.ActCoapResource import ActCoapResource
import logging 


'''
Definition for a CoAP communications server, with embedded test functions.
''' 
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("CoapServer")
fh = logging.FileHandler('CoapServer.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

class CoapCommServer(CoAP):
 
    '''
    Initialization of class.
    '''
  
    def __init__(self, ipAddr="127.0.0.1", port=5683, multicast=False):
        CoAP.__init__(self, (ipAddr, port), multicast)
        
        if port >= 1024:
            self.port = port
        else:
            self.port = 5683
    
        self.ipAddr = ipAddr
        self.useMulticast = multicast
        logger.info("CoapServer Resource initiation")
        
        self.initResources() 
    
    '''
    Initializes the resources.
    '''

    def initResources(self):
        self.add_resource('CLOUD/', CloudCoapResource())
        self.add_resource('ACT/', ActCoapResource())
        print("CoAP server initialized. Binding: " + self.ipAddr + ":" + str(self.port))
        print(self.root.dump())


'''
Main function definition for running server as application.
'''


def main():
    ipAddr = "127.0.0.1"
    
    port = 5683
    useMulticast = False
    coapServer = None

    try:
        coapServer = CoapCommServer(ipAddr, port, useMulticast)
        try:
            print("Created CoAP server ref: " + str(coapServer))
            logger.info("CoapServer load successful")
            coapServer.listen(10)
            
        except Exception:
            print("Failed to create CoAP server reference bound to host: " + ipAddr)
            logger.warning("CoapServer load unsuccessful")
            pass
    except KeyboardInterrupt:
        print("CoAP server shutting down due to keyboard interrupt...")
        logger.info("CoapServer shutdown ")
        
        if coapServer:
            coapServer.close()
        print("CoAP server app exiting.")
        logger.info("CoapServer exiting ")

'''
Attribute definition for when invoking as app via command line
'''

if __name__ == '__main__':
    main()
