import tkinter as tk
import tcp_client as client
import threading
import tkinter_form as form
from mqtt_client import mqtt_client


#ip="127.0.0.1"
ip_fixed="192.168.1.100"
ip_moving="192.168.1.102"
RED="#FF0000"
LIMEGREEN="#32CD32"
SILVER="#C0C0C0"


def connect():
    global fixarm_command
    global fixarm_realtime
    global movingarm_command
    global movingarm_realtime
    fixarm_command=client.tcp_client(ip_fixed,29999)
    fixarm_realtime=client.tcp_client(ip_fixed,30004)
    movingarm_command=client.tcp_client(ip_moving,29999)
    movingarm_realtime=client.tcp_client(ip_moving,30004)
    mqtt=mqtt_client()
    form.connect_button.config(state=tk.DISABLED)
    fixed_feedbacking=threading.Thread(target=fixed_feedback_data)
    moving_feedbacking=threading.Thread(target=moving_feedback_data)
    get_status=threading.Thread(target=get_robot_status)
    get_status.start()
    fixed_feedbacking.start()
    moving_feedbacking.start()
    mqtt.loop_start()


def fixed_feedback_data():
    while True:
        indata=False
        if fixarm_command.s.recv(1024)!=None:
            client=fixarm_command
            fromarm="from fixedarm: "
            feedback_text=form.fixedarm_feedback_text
            indata=True

        if indata==True:
            errorcode, feedback,getting = client.GetFeedback()
            if errorcode is not None:
                feedback_text.delete('1.0','end')
                check_error(int(errorcode),feedback_text)
                feedback_text.insert('2.end',fromarm+str(feedback))
                if getting==1:
                    coordinates=client.GetCoordinates(feedback)
                    get_coordinates(coordinates)

def moving_feedback_data():
    while True:
        indata=False
            
        if movingarm_command.s.recv(1024)!=None:
            client=movingarm_command
            fromarm="from movingarm: "
            feedback_text=form.movingarm_feedback_text
            indata=True

        if indata==True:
            errorcode, feedback,getting = client.GetFeedback()
            if errorcode is not None:
                feedback_text.delete('1.0','end')
                check_error(int(errorcode),feedback_text)
                feedback_text.insert('2.end',fromarm+str(feedback))
                if getting==1:
                    coordinates=client.GetCoordinates(feedback)
                    get_coordinates(coordinates)

def enable():
    fixarm_command.s.send(b'EnableRobot()')
    movingarm_command.s.send(b'EnableRobot()')
    form.enable_button.config(bg=LIMEGREEN)
    form.disable_button.config(bg=SILVER)

def disable():
    fixarm_command.s.send(b'DisableRobot()')
    movingarm_command.s.send(b'DisableRobot()')
    form.disable_button.config(bg=RED)
    form.enable_button.config(bg=SILVER)

def stop():
    fixarm_command.s.send(b'Stop()')
    movingarm_command.s.send(b'Stop()')

def movj():
    if form.fixedarm_button.config('bg')[-1]==LIMEGREEN:
        x=form.x_entry.get()
        y=form.y_entry.get()
        z=form.z_entry.get()
        rx=form.rx_entry.get()
        ry=form.ry_entry.get()
        rz=form.rz_entry.get()
        user=form.user_entry.get()
        vel=form.vel_entry.get()
        acc=form.acc_entry.get()
        fixarm_command.MoveJ(x,y,z,rx,ry,rz,user,vel,acc)
    elif form.movingarm_button.config('bg')[-1]==LIMEGREEN:
        x=form.x_moving_entry.get()
        y=form.y_moving_entry.get()
        z=form.z_moving_entry.get()
        rx=form.rx_moving_entry.get()
        ry=form.ry_moving_entry.get()
        rz=form.rz_moving_entry.get()
        user=form.user_entry.get()
        vel=form.vel_entry.get()
        acc=form.acc_entry.get()
        movingarm_command.MoveJ(x,y,z,rx,ry,rz,user,vel,acc)

def movl():
    if form.fixedarm_button.config('bg')[-1]==LIMEGREEN:
        x=form.x_entry.get()
        y=form.y_entry.get()
        z=form.z_entry.get()
        rx=form.rx_entry.get()
        ry=form.ry_entry.get()
        rz=form.rz_entry.get()
        user=form.user_entry.get()
        vel=form.vel_entry.get()
        acc=form.acc_entry.get()
        fixarm_command.MoveL(x,y,z,rx,ry,rz,user,vel,acc)
    elif form.movingarm_button.config('bg')[-1]==LIMEGREEN:
        x=form.x_moving_entry.get()
        y=form.y_moving_entry.get()
        z=form.z_moving_entry.get()
        rx=form.rx_moving_entry.get()
        ry=form.ry_moving_entry.get()
        rz=form.rz_moving_entry.get()
        user=form.user_entry.get()
        vel=form.vel_entry.get()
        acc=form.acc_entry.get()
        movingarm_command.MoveL(x,y,z,rx,ry,rz,user,vel,acc)

def send_command():
    command=form.command_entry.get()
    fixarm_command.s.send(bytes(command.encode()))
    movingarm_command.s.send(bytes(command.encode()))

def check_error(errorcode,feedback_text):
    form.warning_text.delete('1.0','end')
    match errorcode:
        case 0:
            feedback_text.insert('1.0','Execute successfully \n')
        case -1:
            form.warning_text.insert('1.end',"Command Sent, Action Failed \r\n")
        case -2:
            form.warning_text.insert('1.end',"Dobot is at alert Warning, please clear the warning signal" + "\r\n");
        case -3:
            form.warning_text.insert('1.end',"Dobot is at force stop, please release the forece stop and clear the warning signal" + "\r\n");
        case -4:
            form.warning_text.insert('1.end',"Dobot is not in power, please connect to power supply" + "\r\n");
        case -5:
            form.warning_text.insert('1.end',"Dobot is at script mode/ pause mode, please terminate script or pause before command" + "\r\n");
        case -10000:
            form.warning_text.insert('1.end',"Command nonexist" + "\r\n");
        case -20000:
            form.warning_text.insert('1.end',"Command input variable number unmatch" + "\r\n");
        case _:
            pass

def clear_warning():
    fixarm_command.s.send(b'ClearError()')
    movingarm_command.s.send(b'ClearError()')
    form.warning_text.delete('1.0','end')

def get_pose():
    msg='GetPose(user='+form.user_entry.get()+',tool=0)'
    fixarm_command.s.send(bytes(msg.encode()))
    movingarm_command.s.send(bytes(msg.encode()))

def get_robot_status():
    while True:
        global fixedarm_robot_status
        global movingarm_robot_status
        fixedarm_robot_status=int.from_bytes(fixarm_realtime.Getdata(24,8),"little")
        movingarm_robot_status=int.from_bytes(movingarm_realtime.Getdata(24,8),"little")
        for i in range (2):
            if i==0:
                robot_status=fixedarm_robot_status
                status_text=form.fixedarm_status_text
            elif i==1:
                robot_status=movingarm_robot_status
                status_text=form.movingarm_status_text

            match robot_status:
                case 1:
                    status_text.delete('1.0','end')
                    status_text.insert('1.0',"Dobot is at initialize mode")
                
                case 2:
                    status_text.delete('1.0','end')
                    status_text.insert('1.0',"Dobot is at initialize mode")

                case 3:
                    status_text.delete('1.0','end')
                    status_text.insert('1.0',"Dobot power off")

                case 4:
                    status_text.delete('1.0','end')
                    status_text.insert('1.0',"Dobot disabled")

                case 5:
                    status_text.delete('1.0','end')
                    status_text.insert('1.0',"Dobot enabled and idle")

                case 6:
                    status_text.delete('1.0','end')
                    status_text.insert('1.0',"Dobot is at drag mode")
                
                case 7:
                    status_text.delete('1.0','end')
                    status_text.insert('1.0',"Dobot is running")


                case 8:
                    status_text.delete('1.0','end')
                    status_text.insert('1.0',"Dobot is running single move")


                case 9:
                    status_text.delete('1.0','end')
                    status_text.insert('1.0',"Dobot have uncleared warning")

                case 10:
                    status_text.delete('1.0','end')
                    status_text.insert('1.0',"Dobot is paused")

                case 11:
                    status_text.delete('1.0','end')
                    status_text.insert('1.0',"Dobot collision detected")
                
                case _:
                    pass
        
        
        if fixarm_realtime.Getdata(1028,1)==b'\x00' and movingarm_realtime.Getdata(1028,1)==b'\x00':
            form.running_status_button.config(text='Stop',bg=RED)
        else:
            form.running_status_button.config(text='Running',bg=LIMEGREEN)       
            
def get_coordinates(pose_coordinate):
    for i in range(2):
        if i==0:
            x_write=form.x_entry
            y_write=form.y_entry
            z_write=form.z_entry
            rx_write=form.rx_entry
            ry_write=form.ry_entry
            rz_write=form.rz_entry
        elif i==1:
            x_write=form.x_moving_entry
            y_write=form.y_moving_entry
            z_write=form.z_moving_entry
            rx_write=form.rx_moving_entry
            ry_write=form.ry_moving_entry
            rz_write=form.rz_moving_entry
        x_write.delete('0','end')
        y_write.delete('0','end')
        z_write.delete('0','end')
        rx_write.delete('0','end')
        ry_write.delete('0','end')
        rz_write.delete('0','end')
        try:
            x_write.insert('0',pose_coordinate[0])
            y_write.insert('0',pose_coordinate[1])
            z_write.insert('0',pose_coordinate[2])
            rx_write.insert('0',pose_coordinate[3])
            ry_write.insert('0',pose_coordinate[4])
            rz_write.insert('0',pose_coordinate[5])
        except Exception as e:
            pass

def e_stop():
    if form.e_stop_button.config('bg')[-1]==RED:
        fixarm_command.s.send(b'EmergencyStop(1)')
        movingarm_command.s.send(b'EmergencyStop(1)')
        form.e_stop_button.config(bg=SILVER)
    elif form.e_stop_button.config('bg')[-1]==SILVER:
        fixarm_command.s.send(b'EmergencyStop(0)')
        movingarm_command.s.send(b'EmergencyStop(0)')
        form.e_stop_button.config(bg=RED)

def fixedarm_change():
    if form.fixedarm_button.config('bg')[-1]==SILVER:
        form.fixedarm_button.config(bg=LIMEGREEN)
        form.movingarm_button.config(bg=SILVER)

def movingarm_change():
    if form.movingarm_button.config('bg')[-1]==SILVER:
        form.movingarm_button.config(bg=LIMEGREEN)
        form.fixedarm_button.config(bg=SILVER)

def custom_action_1():
    pass

def custom_action_2():
    pass

def custom_action_3():
    pass

def custom_action_4():
    pass

def copy():
    match form.point_selected.get():
        case 0:
            copy_x=form.x_origin_entry
            copy_y=form.y_origin_entry
            copy_z=form.z_origin_entry
            copy_rx=form.rx_origin_entry
            copy_ry=form.ry_origin_entry
            copy_rz=form.rz_origin_entry
        case 1:
            copy_x=form.x_point_1_entry
            copy_y=form.y_point_1_entry
            copy_z=form.z_point_1_entry
            copy_rx=form.rx_point_1_entry
            copy_ry=form.ry_point_1_entry
            copy_rz=form.rz_point_1_entry
        case 2:
            copy_x=form.x_point_2_entry
            copy_y=form.y_point_2_entry
            copy_z=form.z_point_2_entry
            copy_rx=form.rx_point_2_entry
            copy_ry=form.ry_point_2_entry
            copy_rz=form.rz_point_2_entry
    if form.fixedarm_button.config('bg')[-1]==LIMEGREEN:
        from_x=form.x_entry
        from_y=form.y_entry
        from_z=form.z_entry
        from_rx=form.rx_entry
        from_ry=form.ry_entry
        from_rz=form.rz_entry
    elif form.movingarm_button.config('bg')[-1]==LIMEGREEN:
        from_x=form.x_moving_entry
        from_y=form.y_moving_entry
        from_z=form.z_moving_entry
        from_rx=form.rx_moving_entry
        from_ry=form.ry_moving_entry
        from_rz=form.rz_moving_entry
    copy_x.delete('0','end')
    copy_y.delete('0','end')
    copy_z.delete('0','end')
    copy_rx.delete('0','end')
    copy_ry.delete('0','end')
    copy_rz.delete('0','end')
    copy_x.insert('0',from_x.get())
    copy_y.insert('0',from_y.get())
    copy_z.insert('0',from_z.get())
    copy_rx.insert('0',from_rx.get())
    copy_ry.insert('0',from_ry.get())
    copy_rz.insert('0',from_rz.get())

def set_coordinate():
    x=form.x_origin_entry.get()
    y=form.y_origin_entry.get()
    z=form.z_origin_entry.get()
    rx=form.rx_point_2_entry.get()
    ry=form.ry_origin_entry.get()
    rz=form.rz_point_1_entry.get()    
    if form.fixedarm_button.config('bg')[-1]==LIMEGREEN:
        client=fixarm_command
    elif form.movingarm_button.config('bg')[-1]==LIMEGREEN:
        client=movingarm_command
    client.SetUser(form.set_user_entry.get(),x,y,z,rx,ry,rz)

def check_status(armid,command):
    commandstatus="accepted"
    msg=None
    if armid=="fixedarm":
        robot_status=fixedarm_robot_status
    elif armid=="movingarm":
        robot_status=movingarm_robot_status
    if robot_status == 7:
        if command=="action":
            commandstatus="rejected"
            msg="arm is running previous action"
        elif command=="getstatus":
            commandstatus="busy"
    elif robot_status == 5 and command =="getstatus":
        commandstatus="ready"
    elif robot_status==4 and command=="getstatus":
        commandstatus="disabled"
    elif robot_status==9 and command=="getstatus":
        commandstatus="warning"
    return commandstatus,msg


    





if __name__ == '__main__':
     mqtt=mqtt_client()
     mqtt.subscribe("inno/from/arms")
     mqtt.loop_start()
     form.window.mainloop()