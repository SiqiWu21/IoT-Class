import paho.mqtt.publish as publish

publish.single("ifn649","hello world",hostname="13.239.113.88") 
# Publish a message to the topic "ifn649" on the server - AWS EC2 instance IP

print("done")