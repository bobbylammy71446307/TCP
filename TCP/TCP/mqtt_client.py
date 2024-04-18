from paho.mqtt import client as mqttclient
from ast import literal_eval
import time
import json
import threading
import tkinter_tcp as ui

localhost="127.0.0.1"
port=8083

class mqtt_client():
    def __init__(self,localhost=localhost,port=port):
        self.client=mqttclient.Client("tester",clean_session=True,userdata=None,protocol=mqttclient.MQTTv311,transport="websockets")
        self.client.connect(localhost,port)
        self.client.ws_set_options(path="/mqtt")
        self.client.on_message=self.on_message
        self.armfixedout=False
        self.armmovingout=False

    def publish(self,topic,message):
        self.client.publish(topic,str(json.dumps(message)))

    def subscribe(self,topic):
        self.client.subscribe(topic)

    def on_message(self,client,userdata,message):
        print("Received message:"+message.payload.decode())
        command,armid,index=self.receive_command(message.payload.decode())
        match command:
            case "factoryhome":
                commandstatus,msg=ui.check_status(armid,command)
                self.response(armid,"immediate",commandstatus,msg)
                if msg is None:
                    #to factory home
                    self.response(armid,"completed","factoryhome")

            case "estop":
                self.response(armid,"immediate","accepted")
                #estop
                self.response(armid,"completed","estop")

            case "enable":
                self.response(armid,"immediate","accepted")
                #estop release+ enable
                self.response(armid,"completed","enable")

            case "action":

            case "getstatus":
                self.response(armid,"immediate","accepted")
                #estop release+ enable
                self.response(armid,"completed","enable")
            case "getnextseqindex":
                self.response(armid,"immediate","accepted")
                #estop release+ enable
                self.response(armid,"completed","enable")
            case "setpage":
                self.response(armid,"immediate","accepted")
                #estop release+ enable
                self.response(armid,"completed","enable")

        
        
        """
        if command=="getstatus":
            response=self.response(armid,"immediate","getstatus")
        commandstatus,msg=ui.check_status(armid,command)
        """

        

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

    def receive_command(self,msg):
        payload=literal_eval(msg)
        command=payload["command"]
        armid=payload["targetarm"]
        if command=="action":
            index=payload["sequenceindex"]
        elif command=="setpage":
            index=payload["pageindex"]
        else :
            index=None
        
        return command,armid, index
        
    def response(self,armid, status, commandstatus,msg=None):
        response={}
        if status=="immediate":
            response["feedback"]="ack"
            response["targetarm"]=armid
            response["commandstatus"]=commandstatus
        elif status=="completed":
            response["feedback"]="commandstatus"
            response["command"]=commandstatus
            response["targetarm"]=armid
            response["commandstatus"]="completed"
        if msg!=None:
            response["message"]=msg
        self.publish("inno/to/arms",str(json.dumps(response)))

    


        


if __name__=="__main__":
    mqtt=mqtt_client()
    mqtt.subscribe("inno/from/arms")
    mqtt.loop_start()
    mqtt.loop_stop()




