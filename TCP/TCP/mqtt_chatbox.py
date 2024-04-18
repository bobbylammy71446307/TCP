from paho.mqtt import client as mqttclient
from ast import literal_eval
import time
import json

localhost= "127.0.0.1"
#"test.mosquitto.org"
port=8083
move_forward=False

armfixed_message=[  {"command":"factoryhome","targetarm":"armfixed","direction":"out"},
                    {"command":"setpage","targetarm":"armfixed","pageindex":1},
                    {"command":"action","targetarm":"armfixed","sequenceindex":0},
                    {"command":"action","targetarm":"armfixed","sequenceindex":1},
                    {"command":"action","targetarm":"armfixed","sequenceindex":2},
                    {"command":"action","targetarm":"armfixed","sequenceindex":3},
                    {"command":"action","targetarm":"armfixed","sequenceindex":4},
                    {"command":"action","targetarm":"armfixed","sequenceindex":5},
                    {"command":"action","targetarm":"armfixed","sequenceindex":6},
                    {"command":"action","targetarm":"armfixed","sequenceindex":7},
                    {"command":"action","targetarm":"armfixed","sequenceindex":8},
                    {"command":"action","targetarm":"armfixed","sequenceindex":9},
                    {"command":"action","targetarm":"armfixed","sequenceindex":10},
                    {"command":"action","targetarm":"armfixed","sequenceindex":11},
                    {"command":"action","targetarm":"armfixed","sequenceindex":12},
                    {"command":"action","targetarm":"armfixed","sequenceindex":13},
                    {"command":"action","targetarm":"armfixed","sequenceindex":14}]

armmoving_message=[ {"command":"factoryhome","targetarm":"armmoving","direction":"out"},
                    {"command":"setpage","targetarm":"armmoving","pageindex":1},
                    {"command":"action","targetarm":"armmoving","sequenceindex":0},
                    {"command":"action","targetarm":"armmoving","sequenceindex":1},
                    {"command":"action","targetarm":"armmoving","sequenceindex":2},
                    {"command":"action","targetarm":"armmoving","sequenceindex":3},
                    {"command":"action","targetarm":"armmoving","sequenceindex":4},
                    {"command":"action","targetarm":"armmoving","sequenceindex":5},
                    {"command":"action","targetarm":"armmoving","sequenceindex":6},
                    {"command":"action","targetarm":"armmoving","sequenceindex":7},
                    {"command":"action","targetarm":"armmoving","sequenceindex":8},
                    {"command":"action","targetarm":"armmoving","sequenceindex":9},
                    {"command":"action","targetarm":"armmoving","sequenceindex":10},
                    {"command":"action","targetarm":"armmoving","sequenceindex":11},
                    {"command":"action","targetarm":"armmoving","sequenceindex":12},
                    {"command":"action","targetarm":"armmoving","sequenceindex":13},
                    {"command":"action","targetarm":"armmoving","sequenceindex":14}
                    ]

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

    def idle_armfixed(self):
        while self.armfixedout:
            time.sleep(0.1)

    def idle_armmoving(self):
        while self.armmovingout:
            time.sleep(0.1)


        


if __name__=="__main__":
    mqtt=mqtt_client()
    mqtt.subscribe("inno/from/arms")
    mqtt.loop_start()
    for i in range(11):
        mqtt.publish("inno/to/arms",armmoving_message[i])
        print("Send message:"+str(armmoving_message[i]))
        mqtt.publish("inno/to/arms",armfixed_message[i])
        print("Send message:"+str(armfixed_message[i]))
        mqtt.idle()
    mqtt.publish("inno/to/arms",armfixed_message[11])
    print("Send message:"+str(armfixed_message[11]))
    time.sleep(1.5)
    mqtt.publish("inno/to/arms",armmoving_message[11])
    print("Send message:"+str(armmoving_message[11]))
    mqtt.idle_armfixed()
    mqtt.publish("inno/to/arms",armfixed_message[12])
    print("Send message:"+str(armfixed_message[12]))
    mqtt.idle_armmoving()
    mqtt.publish("inno/to/arms",armmoving_message[12])
    print("Send message:"+str(armmoving_message[12]))
    mqtt.idle_armfixed()
    mqtt.publish("inno/to/arms",armfixed_message[13])
    print("Send message:"+str(armfixed_message[13]))
    mqtt.idle_armmoving()
    mqtt.publish("inno/to/arms",armmoving_message[13])
    print("Send message:"+str(armmoving_message[13]))
    mqtt.idle()
    mqtt.publish("inno/to/arms",armmoving_message[14])
    print("Send message:"+str(armmoving_message[14]))
    mqtt.idle()
    mqtt.publish("inno/to/arms",armfixed_message[14])
    print("Send message:"+str(armfixed_message[14]))
    mqtt.idle()
    for i in range (15,len(armfixed_message)):
        mqtt.publish("inno/to/arms",armmoving_message[i])
        print("Send message:"+str(armmoving_message[i]))
        mqtt.publish("inno/to/arms",armfixed_message[i])
        print("Send message:"+str(armfixed_message[i]))
        mqtt.idle()
    mqtt.loop_stop()




