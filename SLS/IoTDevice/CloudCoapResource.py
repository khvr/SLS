'''
Created on Apr 16, 2018

@author: yogesh

'''
from coapthon.resources.resource import Resource
from IoTDevice.MqttConnecter import *
import logging

'''
Definition for a CoAP resource handler.
'''
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("CloudResource")
fh = logging.FileHandler('CloudResource.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

class CloudCoapResource(Resource):
    '''
    Initialization of class.
    '''
    
    def __init__(self, name="CloudCoapResource", coap_server=None):
        super(CloudCoapResource, self).__init__(
            name, coap_server, visible=True, observable=True, allow_children=True)
        self.payload = "Cloud CoAP Resource"
        self.resource_type = "rt1"
        self.content_type = "text/plain"
        self.interface_type = "if1"
        logger.info("CloudCoapResource initiation successful")
       
    def render_GET(self, request):
        logger.info("CloudCoapResource handling GET req")
        print("Successfully retrieved this message from CloudCoapResource. Payload: " + str(self.payload))
        return self

    def render_PUT(self, request):
        logger.info("CloudCoapResource handling POST req")
        print("Editing stored payload(test): " + str(request.payload))
        self.edit_resource(request)
        return self
    
    def render_POST(self, request):
        logger.info("CloudCoapResource handling POST req")
        
        print("Adding payload(test): " + str(request.payload))
        #Parsing the Topic from path for MQTT Publish
        topic = self.path.replace('/', '')
        
        print("Topic Received : " + topic)
        
        try:
            MqttConnect(topic, request.payload)
        except Exception:
            print("MQTT publish failure Topic-" + topic)
            logger.warning("CloudCoapResource MQTT publish failed")
        
        res = self.init_resource(request, CloudCoapResource())
        return res

    def render_DELETE(self, request):
        logger.info("CloudCoapResource handling DELETE req")
        print("Delete request successful")
        self.render_DELETE(request)
        return True
