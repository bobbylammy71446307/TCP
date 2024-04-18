import tkinter as tk


RED="#FF0000"
LIMEGREEN="#32CD32"
SILVER="#C0C0C0"
WHITE="#FFFFFF"


#window init
window=tk.Tk()
window.title('Media Server')
window.geometry('1000x650')



#button init
connect_button=tk.Button(window,
                        text='Connect',
                        width=15,
                        height=2,
                        #command=main.connect,
                        bg=WHITE
                        )
send_1_button=tk.Button(window,
                        text='Send',
                        width=10,
                        height=2,
                        #command=main.enable,
                        bg=SILVER
                        )
send_2_button=tk.Button(window,
                        text='Send',
                        width=10,
                        height=2,
                        #command=main.disable,
                        bg=RED
                        )
send_tgt_button=tk.Button(window,
                            text='Simultaneous',
                            width=10,
                            height=2,
                            #command=main.stop,
                            bg=WHITE
                            )

#label init
send_1_label=tk.Label(window,text='Send 1')
send_2_label=tk.Label(window,text='Send 2')
command_1_label=tk.Label(window,text='command')
command_2_label=tk.Label(window,text='command')
targetarm_1_label=tk.Label(window,text='targetarm')
targetarm_2_label=tk.Label(window,text='targetarm')
index_1_label=tk.Label(window,text='index')
index_2_label=tk.Label(window,text='index')
sent_label=tk.Label(window,text='Sent')
received_label=tk.Label(window,text='Received')

#Entry init


#textbox init

command_1_Text=tk.Text(window,width=10,height=2)
command_2_Text=tk.Text(window,width=10,height=2)
targetarm_1_Text=tk.Text(window,width=10,height=2)
targetarm_2_Text=tk.Text(window,width=10,height=2)
index_1_Text=tk.Text(window,width=10,height=2)
index_2_Text=tk.Text(window,width=10,height=2)

sent_text=tk.Text(window,width=30,height=10)
received_text=tk.Text(window,width=30,height=10)
#placing init
connect_button.place(x=50,y=10)

send_1_label.place(x=50,y=100)
command_1_label.place(x=100,y=100)
command_1_Text.place(x=180,y=100)
targetarm_1_label.place(x=280,y=100)
targetarm_1_Text.place(x=360,y=100)
index_1_label.place(x=460,y=100)
index_1_Text.place(x=540,y=100)
send_1_button.place(x=650,y=100)

send_2_label.place(x=50,y=250)
command_2_label.place(x=100,y=250)
command_2_Text.place(x=180,y=250)
targetarm_2_label.place(x=280,y=250)
targetarm_2_Text.place(x=360,y=250)
index_2_label.place(x=460,y=250)
index_2_Text.place(x=540,y=250)
send_2_button.place(x=650,y=250)


send_tgt_button.place(x=800,y=175)



sent_label.place(x=50,y=400)
sent_text.place(x=100,y=400)



received_label.place(x=450,y=400)
received_text.place(x=550,y=400)




window.mainloop()