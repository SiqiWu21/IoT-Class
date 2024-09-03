#This code is designed to connect to the MQTT server and subscribe to the topic "ifn649".
# Through AWS ec2 instance IP, the client connects to the server. 
#When a message is received, it is sent to the serial port.

import paho.mqtt.client as mqtt
import serial

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print(f"Connected with MQTT")
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("ifn649")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    ser = serial.Serial("/dev/rfcomm0",9600)
    ser.write(msg.payload)

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

client.connect("13.239.113.88", 1883, 60)    # Connect to the server - AWS EC2 instance IP

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()