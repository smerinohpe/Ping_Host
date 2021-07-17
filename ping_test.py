import subprocess as sub
import tkinter as tk
from tkinter import *

class test (tk.Tk):
    def ping(self):
      try:
        self.withdraw()
        result=sub.Popen(["ping", "-n", "1", "-w", "1000", conf_ip.get()],shell=True).wait()
        if result == 0:
          # print ('Active')
          B = btn_ping
          B ['bg'] = 'green'
        else:
          # print ('Inactive')
          B = btn_ping
          B ['bg'] = 'red'
        self.after(1000, self.ping)
      except:
        quit()

    def __init__(self):
      tk.Tk.__init__(self)
      global conf_ip, ping_ip, btn_ping, btn_stop, window
      window = tk.Tk()
      window.title("Ping to host IP")
      window.attributes('-topmost',True)
      window.geometry('175x70+1350+730')

      lbl = Label(window, text='Pinging')
      lbl.grid(row=0, columnspan=3)

      ping_ip= StringVar()
      
      btn_ping= Button(window, text='LIVE')
      btn_ping.config(width=25, height=1)
      btn_ping.grid(row=4, column=1)
	  
      conf_ip = Entry(window, state='normal', textvariable=ping_ip)
      conf_ip.grid(row=1, column=1)
      ping_ip.set('Enter IP')

      #window.mainloop()

app = test()
app.ping()
app.mainloop()