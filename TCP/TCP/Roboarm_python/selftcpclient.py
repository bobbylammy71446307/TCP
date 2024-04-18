import socket
import copy

class tcp_client:
    def __init__(self,ip,port):
        self.s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.s.connect((ip,port))
        self.robotstate=0

    def MoveJ(self,x,y,z,rx,ry,rz,user,vel,acc):
        msg='MovJ(pose={'+x+','+y+','+z+','+rx+','+ry+','+rz+'},user='+user+',tool=0,a='+acc+',v='+vel+',cp=100)'
        self.s.send(bytes(msg.encode()))

    def MoveL(self,x,y,z,rx,ry,rz,user,vel,acc):
        msg='MovL(pose={'+x+','+y+','+z+','+rx+','+ry+','+rz+'},user='+user+',tool=0,a='+acc+',v='+vel+',cp=100)'
        self.s.send(bytes(msg.encode()))

    def MoveL_speed(self,x,y,z,rx,ry,rz,user,speed):
        msg='MovL(pose={'+x+','+y+','+z+','+rx+','+ry+','+rz+'},user='+user+',tool=0,speed='+speed+',cp=100)'
        self.s.send(bytes(msg.encode()))

    def SetUser(self,user,x,y,z,rx,ry,rz):
        msg='SetUser('+user+',{'+x+','+y+','+z+','+rx+','+ry+','+rz+'})'
        self.s.send(bytes(msg.encode()))
        
    def GetFeedback(self):
        indata=self.s.recv(1024)
        getdata=indata.decode()
        feedback=[]
        count=0
        getting=0
        in_bracket=False
        print(getdata)
        for i in range(len(getdata)):
            if (getdata[i]==',' or getdata[i]== ';') and in_bracket==False:
                feedback.append(getdata[count:i])
                count=i+1
            if getdata[i]=='(':
                in_bracket=True
            elif getdata[i]==')':
                in_bracket=False
        for j in range(len(feedback[-1])):
            if feedback[-1][j]=='(':
                command=feedback[-1][0:j]
                break
        if command=='GetPose':
            getting=1
        return feedback[0],feedback[1:-1],getting
            
    def GetCoordinates(self,getdata):
        getdata[0]=getdata[0][1:]
        getdata[-1]=getdata[-1][:-1]
        return getdata
        

    
    def Getdata(self,init,count):
        buffer=[]
        indata=self.s.recv(1440)
        if not indata:
            print("No data")
            pass
        else:
            buffer=copy.deepcopy(indata[init:init+count])
        return buffer

            

