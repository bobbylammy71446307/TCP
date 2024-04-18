from paho.mqtt import client as mqttclient
from ast import literal_eval
import time
import json

localhost= "127.0.0.1"
#"test.mosquitto.org"
port=8083

class mqtt_client():
    def __init__(self,localhost=localhost,port=port):
        #self.client=mqttclient.Client("BOOOOB",clean_session=False,userdata=None,protocol=mqttclient.MQTTv311,transport="tcp")
        self.client=mqttclient.Client("tester",clean_session=True,userdata=None,protocol=mqttclient.MQTTv311,transport="websockets")
        self.client.connect(localhost,port)
        self.client.ws_set_options(path="/mqtt")
        self.client.on_message=self.on_message
        self.armfixedout=False
        self.armmovingout=False

    def publish(self,topic,message):
        self.client.publish(topic,str(json.dumps(message)))
        if message["targetarm"]=="armfixed":
            self.armfixedout=True
        elif message["targetarm"]=="armmoving":
            self.armmovingout=True

    def on_disconnect(self,client,userdata,rc):
        print("Disconnected from broker with code:"+str(rc))

    def subscribe(self,topic):
        self.client.subscribe(topic)

    def on_message(self,client,userdata,message):
        try:
            print("Received message:"+message.payload.decode())
            self.check_completed(literal_eval(message.payload.decode()))

        except Exception as Na:
            print(Na)

    def loop(self):
        self.client.loop()
    
    def loop_start(self):   
        self.client.loop_start()

    def loop_forever(self):
        self.client.loop_forever()
     
    def loop_stop(self):
        self.client.loop_stop()
    
    def check_completed(self,message):       
        if message["targetarm"]=="armfixed" and message["commandstatus"]=="completed":
            self.armfixedout=False
        if message["targetarm"]=="armmoving"and message["commandstatus"]=="completed":
            self.armmovingout=False
    
    
    def idle(self):
        while self.armfixedout or self.armmovingout:
            time.sleep(0.1)


if __name__=="__main__":
    mqtt=mqtt_client()
    mqtt.subscribe("inno/from/arms")
    mqtt.loop_start()
    while True:
        publish_msg=json.loads(input("msg to be publish: "))
        mqtt.publish("inno/to/arms",publish_msg)
        print("Send message:"+str(publish_msg))
        time.sleep(1)
        #mqtt.idle()



