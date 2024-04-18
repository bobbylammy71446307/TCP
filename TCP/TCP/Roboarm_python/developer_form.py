import mqtt_function as mqttclient
import source_obj as obj


if __name__=="__main__":
    obj.log("**//Roboarm Start//**")
    obj.mqtt=mqttclient.Mqtt_Client(obj.localhost,obj.port,"Client1")
    obj.mqtt.loop_forever()