import tkinter as tk
import tkinter_tcp as main


RED="#FF0000"
LIMEGREEN="#32CD32"
SILVER="#C0C0C0"
WHITE="#FFFFFF"


#window init
window=tk.Tk()
window.title('Dobot Control')
window.geometry('1000x650')
point_selected=tk.IntVar(value=1)



#button init
connect_button=tk.Button(window,
                        text='Connect',
                        width=15,
                        height=2,
                        command=main.connect,
                        bg=WHITE
                        )
enable_button=tk.Button(window,
                        text='Enable',
                        width=10,
                        height=2,
                        command=main.enable,
                        bg=SILVER
                        )
disable_button=tk.Button(window,
                        text='Disable',
                        width=10,
                        height=2,
                        command=main.disable,
                        bg=RED
                        )
stop_action_button=tk.Button(window,
                            text='Stop Action',
                            width=10,
                            height=2,
                            command=main.stop,
                            bg=WHITE
                            )
movj_button=tk.Button(window,
                    text='MovJ',
                    width=10,
                    height=2,
                    command=main.movj,
                    bg=WHITE
                    )
movl_button=tk.Button(window,
                    text='MovL',
                    width=10,
                    height=2,
                    command=main.movl,
                    bg=WHITE
                    )
clear_warning_button=tk.Button(window,
                            text='Clear Warning',
                            width=10,
                            height=2,
                            command=main.clear_warning,
                            bg=WHITE
                            )
get_pose_button=tk.Button(window,
                        text='Get Pose',
                        width=10,
                        height=2,
                        command=main.get_pose,
                        bg=WHITE)
command_button=tk.Button(window,
                        text='Send',
                        command=main.send_command,
                        width=10,
                        height=2,
                        bg=WHITE)
e_stop_button=tk.Button(window,
                        text='Emergency\nStop',
                        font=('Arial',18,'bold'),
                        justify='center',
                        width=10,
                        height=3,
                        command=main.e_stop,
                        bg=RED)
running_status_button=tk.Button(window,
                                text='Stop',
                                font=('Arial',14),
                                width=8,
                                height=2,
                                bg=RED,
                                state='disabled')
fixedarm_button=tk.Button(window,
                          text='Fixed Arm',
                          width=10,
                          height=2,
                          command=main.fixedarm_change,
                          bg=LIMEGREEN)
movingarm_button=tk.Button(window,
                          text='Moving Arm',
                          width=10,
                          height=2,
                          command=main.movingarm_change,
                          bg=SILVER)
custom_action_1_button=tk.Button(window,
                                text='Custom Action 1',
                                width=15,
                                height=2,
                                #command=main.custom_action_1,
                                bg=WHITE)
custom_action_2_button=tk.Button(window,
                                text='Custom Action 2',
                                width=15,
                                height=2,
                                #command=main.custom_action_2,
                                bg=WHITE)
custom_action_3_button=tk.Button(window,
                                text='Custom Action 3',
                                width=15,
                                height=2,
                                #command=main.custom_action_3,
                                bg=WHITE)
custom_action_4_button=tk.Button(window,
                                text='Custom Action 4',
                                width=15,
                                height=2,
                                #command=main.custom_action_4,
                                bg=WHITE)
copy_button=tk.Button(window,
                    text='Copy',
                    width=10,
                    height=2,
                    command=main.copy,
                    bg=WHITE)

set_coordinate_button=tk.Button(window,
                                text='Set User',
                                width=10,
                                height=2,
                                command=main.set_coordinate,
                                bg=WHITE)

radiobutton_1=tk.Radiobutton(window,
                            text='Origin Point',
                            variable=point_selected,
                            value=0,
                            bg=WHITE)
radiobutton_2=tk.Radiobutton(window,
                            text='Point 1',
                            variable=point_selected,
                            value=1,
                            bg=WHITE)
radiobutton_3=tk.Radiobutton(window,
                            text='Point 2',
                            variable=point_selected,
                            value=2,
                            bg=WHITE)

#label init
x_label=tk.Label(window,text='x')
y_label=tk.Label(window,text='y')
z_label=tk.Label(window,text='z')
rx_label=tk.Label(window,text='rx')
ry_label=tk.Label(window,text='ry')
rz_label=tk.Label(window,text='rz')
vel_label=tk.Label(window,text='vel')
acc_label=tk.Label(window,text='acc')
x_moving_label=tk.Label(window,text='x')
y_moving_label=tk.Label(window,text='y')
z_moving_label=tk.Label(window,text='z')
rx_moving_label=tk.Label(window,text='rx')
ry_moving_label=tk.Label(window,text='ry')
rz_moving_label=tk.Label(window,text='rz')
vel_moving_label=tk.Label(window,text='vel')
acc_moving_label=tk.Label(window,text='acc')
user_label=tk.Label(window,text='User')
command_label=tk.Label(window,text='Command')
fixedarm_feedback_label=tk.Label(window,text='Fixedarm Feedback')
movingarm_feedback_label=tk.Label(window,text='Fixedarm Feedback')
fixedarm_status_label=tk.Label(window,text='Fixedarm Status')
movingarm_status_label=tk.Label(window,text='Movingarm Status')
warning_label=tk.Label(window,text='Warning')
custom_label=tk.Label(window,text='Custom Action')
set_user_label=tk.Label(window,text='Set User')
#entry init
x_entry=tk.Entry(window,width=10)
y_entry=tk.Entry(window,width=10)
z_entry=tk.Entry(window,width=10)
rx_entry=tk.Entry(window,width=10)
ry_entry=tk.Entry(window,width=10)
rz_entry=tk.Entry(window,width=10)
vel_entry=tk.Entry(window,width=10,textvariable=tk.StringVar(value="50"))
acc_entry=tk.Entry(window,width=10,textvariable=tk.StringVar(value="20"))
x_moving_entry=tk.Entry(window,width=10)
y_moving_entry=tk.Entry(window,width=10)
z_moving_entry=tk.Entry(window,width=10)
rx_moving_entry=tk.Entry(window,width=10)
ry_moving_entry=tk.Entry(window,width=10)
rz_moving_entry=tk.Entry(window,width=10)
vel_moving_entry=tk.Entry(window,width=10,textvariable=tk.StringVar(value="50"))
acc_moving_entry=tk.Entry(window,width=10,textvariable=tk.StringVar(value="20"))
user_entry=tk.Entry(window,width=8,textvariable=tk.StringVar(value="0"))
command_entry=tk.Entry(window,width=30)
set_user_entry=tk.Entry(window,width=8)

x_origin_entry=tk.Entry(window,width=8)
y_origin_entry=tk.Entry(window,width=8)
z_origin_entry=tk.Entry(window,width=8)
rx_origin_entry=tk.Entry(window,width=8)
ry_origin_entry=tk.Entry(window,width=8)
rz_origin_entry=tk.Entry(window,width=8)
x_point_1_entry=tk.Entry(window,width=8)
y_point_1_entry=tk.Entry(window,width=8)
z_point_1_entry=tk.Entry(window,width=8)
rx_point_1_entry=tk.Entry(window,width=8)
ry_point_1_entry=tk.Entry(window,width=8)
rz_point_1_entry=tk.Entry(window,width=8)
x_point_2_entry=tk.Entry(window,width=8)
y_point_2_entry=tk.Entry(window,width=8)
z_point_2_entry=tk.Entry(window,width=8)
rx_point_2_entry=tk.Entry(window,width=8)
ry_point_2_entry=tk.Entry(window,width=8)
rz_point_2_entry=tk.Entry(window,width=8)



#textbox init
fixedarm_feedback_text=tk.Text(window,width=30,height=3)
movingarm_feedback_text=tk.Text(window,width=30,height=3)
fixedarm_status_text=tk.Text(window,width=30,height=1)
movingarm_status_text=tk.Text(window,width=30,height=1)
warning_text=tk.Text(window,width=30,height=5)










#placing init
command_label.place(x=50,y=130)
command_entry.place(x=50,y=160)
command_button.place(x=50,y=190)

fixedarm_feedback_label.place(x=50,y=240)
fixedarm_feedback_text.place(x=50,y=260)

movingarm_feedback_label.place(x=50,y=310)
movingarm_feedback_text.place(x=50,y=330)

fixedarm_status_label.place(x=50,y=380)
fixedarm_status_text.place(x=50,y=400)

movingarm_status_label.place(x=50,y=420)
movingarm_status_text.place(x=50,y=440)


warning_label.place(x=50,y=460)
warning_text.place(x=50,y=480)


x_label.place(x=300,y=110)
x_entry.place(x=320,y=110)
y_label.place(x=300,y=140)
y_entry.place(x=320,y=140)
z_label.place(x=300,y=170)
z_entry.place(x=320,y=170)
rx_label.place(x=400,y=110)
rx_entry.place(x=420,y=110)
ry_label.place(x=400,y=140)
ry_entry.place(x=420,y=140)
rz_label.place(x=400,y=170)
rz_entry.place(x=420,y=170)
vel_label.place(x=300,y=200)
vel_entry.place(x=320,y=200)
acc_label.place(x=400,y=200)
acc_entry.place(x=420,y=200)

x_moving_label.place(x=520,y=110)
x_moving_entry.place(x=540,y=110)
y_moving_label.place(x=520,y=140)
y_moving_entry.place(x=540,y=140)
z_moving_label.place(x=520,y=170)
z_moving_entry.place(x=540,y=170)
rx_moving_label.place(x=620,y=110)
rx_moving_entry.place(x=640,y=110)
ry_moving_label.place(x=620,y=140)
ry_moving_entry.place(x=640,y=140)
rz_moving_label.place(x=620,y=170)
rz_moving_entry.place(x=640,y=170)
vel_moving_label.place(x=520,y=200)
vel_moving_entry.place(x=540,y=200)
acc_moving_label.place(x=620,y=200)
acc_moving_entry.place(x=640,y=200)


user_label.place(x=420,y=30)
user_entry.place(x=450,y=30)

x_origin_entry.place(x=410,y=460)
y_origin_entry.place(x=470,y=460)
z_origin_entry.place(x=530,y=460)
rx_origin_entry.place(x=590,y=460)
ry_origin_entry.place(x=650,y=460)
rz_origin_entry.place(x=710,y=460)

x_point_1_entry.place(x=410,y=490)
y_point_1_entry.place(x=470,y=490)
z_point_1_entry.place(x=530,y=490)
rx_point_1_entry.place(x=590,y=490)
ry_point_1_entry.place(x=650,y=490)
rz_point_1_entry.place(x=710,y=490)

x_point_2_entry.place(x=410,y=520)
y_point_2_entry.place(x=470,y=520)
z_point_2_entry.place(x=530,y=520)
rx_point_2_entry.place(x=590,y=520)
ry_point_2_entry.place(x=650,y=520)
rz_point_2_entry.place(x=710,y=520)

set_user_label.place(x=310,y=570)
set_user_entry.place(x=380,y=570)





movj_button.place(x=420,y=230)
movl_button.place(x=520,y=230)

fixedarm_button.place(x=370,y=60)
movingarm_button.place(x=590,y=60)

custom_label.place(x=310,y=300)
custom_action_1_button.place(x=310,y=330)
custom_action_2_button.place(x=460,y=330)
custom_action_3_button.place(x=310,y=380)
custom_action_4_button.place(x=460,y=380)

radiobutton_1.place(x=310,y=460)
radiobutton_2.place(x=310,y=490)
radiobutton_3.place(x=310,y=520)




connect_button.place(x=85,y=10)
enable_button.place(x=50,y=70)
disable_button.place(x=150,y=70)
stop_action_button.place(x=760,y=130)
get_pose_button.place(x=540,y=10)
clear_warning_button.place(x=50,y=570)
e_stop_button.place(x=800,y=500)
running_status_button.place(x=750,y=60)
copy_button.place(x=450,y=550)
set_coordinate_button.place(x=550,y=550)


