from paho.mqtt import client as mqttclient
from ast import literal_eval
import time
import json
import threading
import source_obj as obj



class Mqtt_Client():
    

    def __init__(self, ip, port,username):
        
        try:
            self.client=mqttclient.Client(username,clean_session=True,userdata=None,protocol=mqttclient.MQTTv311,transport="websockets")
            self.client.connect(ip,port)
            self.client.ws_set_options(path="/mqtt")
            self.client.on_message=self.on_message
            self.client.subscribe("inno/to/arms")

        except Exception as e:
            print(e)
            obj.log(e)
            print("Error in mqtt_client __init__")

    def loop_forever(self):
        self.client.loop_forever()

    def on_message(self,client,userdata,message):
        try:
            #Log received message
            obj.log("Received message:"+message.payload.decode())
            #run action thread
            threading.Thread(target=self.receieved_message,args=(message.payload.decode(),)).start()
        except Exception as e:
            #Log error
            print(e)
            obj.log(e)
            print("Error in mqtt_client on_message")

    def receieved_message(self, message):
        print("Received message:"+ message)
        payload=literal_eval(message)
        command=payload["command"]
        armid=payload["targetarm"]
        if armid=="armfixed":
            client_command=obj.armfixed_command
            client_realtime=obj.armfixed_realtime
        elif armid=="armmoving":
            #client_command=obj.armmoving_command
            #client_realtime=obj.armmoving_realtime
            pass
        match command:
            case "factoryhome":
                if self.check_error() and self.check_status():
                    pass
                self.response(armid,"immediate","accepted")
                client_command.MoveJ("0","0","0","0","0","0","0","100","100")
                print("Factory home")

            case "estop":
                print("Estop")

            case "clearerror":
                print("Clear error")

            case "enable":
                print("Enable")

            case "action":
                if self.check_error() and self.check_status():
                    pass
                if self.determine_sequence(armid,payload["sequenceindex"]):
                    self.response(armid,"immediate","accepted")
                else:
                    self.response(armid,"immediate","rejected","seq not in order")
                match payload["sequenceindex"]:
                    case 0:
                        print("Action 0")
                    case 1:
                        print("Action 1")
                    case 2:
                        print("Action 2")
                    case 99:
                        print("Action 99")

            case "getstatus":
                self.check_status("getstatus",client_realtime)
                print("Get status")

            case "getnextseqindex":
                print("Get next sequence index")

            case "setpage":
                print("Set page")

            case "collapsed":
                print("Collapsed")

            case _:
                print("Invalid command")
        
        
    def check_status(self,command,client_realtime):
        if command == ("factoryhome" or "action" or"collapsed"):
            if client_realtime.robot_state==7:
                self.response("armfixed","immediate","rejected","arm is running prevoius command")
                return True
            else: 
                return False
        elif command == "getstatus":
            if not client_realtime.connected:
                self.response("armfixed","armstatus","disconnected")
            else:
                match client_realtime.robot_state:
                    case 4:
                        self.response("armfixed","armstatus","disabled")
                    case 5:
                        self.response("armfixed","armstatus","ready")
                    case 7:
                        self.response("armfixed","armstatus","busy")
                    case 9:
                        #load error
                        self.response("armfixed","armstatus","error")
                    case 11: 
                        self.response("armfixed","armstatus","arm collided")
            return True        
    
    def check_error(self,client_command,client_realtime):
        if client_realtime.robot_state == 9 or 11:
            self.response("armfixed","immediate","rejected",self.load_error(client_command.get_error()))
            return True
        else:
            return False

    def load_error(errorid):
        with open('C:\\arm\\program\\Roboarm\\Roboarm\\en_alarmController.json',"r", encoding="utf-8") as file:
            data = json.load(file)
            for items in data:
                if items['id'] == errorid:
                    if items['en']['description'] != "":
                        msg = "Description: " + items['en']['description'] + " "
                        break
        return msg

    def determine_sequence(self,armid,seq_index):
        if armid=="armfixed":
            prev_index=obj.armfixed_prev_index
        elif armid=="armmoving":
            prev_index=obj.armmoving_prev_index

        if seq_index==prev_index+1:
            return True
        else:
            return False

    """
    def set_page(self):
        pass

    def action_response(self):
        pass
"""
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
        self.publish(str(json.dumps(response)))
    
    def publish(self,message):
        obj.log("Publishing message:"+message)
        print("Publishing message:"+message)
        self.client.publish("inno/from/arms",message) 

    """
    def to_initial(self):
        pass

    def to_point(self):
        pass

    def parallel_move(self):
        pass

    def arc_move(self):
        pass

    def click_point(self):
        pass

    def weld_action(self):
        pass

    def welding(self):
        pass

    def idle(self):
        pass

    def check_success(self):
        pass

    def perform_action_p0(self):
        pass
    """
if __name__=="__main__":
    mqtt=Mqtt_Client("127.0.0.1",8083,"Client100")
    mqtt.client.loop_forever()
