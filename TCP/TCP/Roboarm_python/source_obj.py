import selftcpclient as tcpclient
import mqtt_function as mqttclient
import logger as logger

localhost="127.0.0.1"
port= 8083
armfixed_command=tcpclient.tcp_client(localhost,29999)
armfixed_realtime=tcpclient.tcp_client(localhost,30004)
#armmoving_command=tcpclient.tcp_client(localhost,29999)
#armfixed_realtime=tcpclient.tcp_client(localhost,30004)
armmoving_prev_index=-1
armfixed_prev_index=-1
page_index_armmoving=1
page_index_armfixed=1
armfixed_warning=False
armmoving_warning=False
connected=False
mqtt=None
password="iuseonly"
manual_connection=False
sended_warning_armfixed=False
sended_warning_armmoving=False
disconnect_from_connect=False
collision_warning_armmoving=False
collision_warning_armfixed=False
nonseq=False
mqttstartup_timer=0

def log(msg):
    logger.Logger.log(msg)

