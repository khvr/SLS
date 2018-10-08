# SLS
Smart-Lighting- System

 Approach: To enable energy saving & help consumer to reduce E-bill by employing IoT based system to automate effort for controlling lights on and off. We will use sensor to measure illuminance in an area and feed it to gateway device which pushes data to cloud for analytics and data to edge device which control power supply to lights.

Design Overview
 Topology: -Hub & Spoke is used since our design is for Home environment.
 Hub & Spoke is used because we are doing most of the processing locally and just having remote cloud for analytics(* Future Scope)
 Overhead is placed on Server (CoAP Protocol) which handles the data and forward to edge device & cloud service using MQTT protocol
 Cloud Service : - IBM Bluemix is used to capture the data and store in its DB.
Smart Lighting System (SLS) Yogesh Suresh
 Message : To have fluid flow of data the payload is constructed in such way that transfer between CoAP & MQTT is hassle-free process.Detailed format given in sub sequent topic.
 Edge Tier :- Actuation(MQTT Subscriber) & Sensing(CoAP Client) comes in this tier
 Gateway Tier :- CoAP server & MQTT publisher (cloud ,Actuator) for sits here
