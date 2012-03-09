import socket
import sys
import select
import android
import time
import sys

def read_accel(droid):
  pos = droid.sensorsReadAccelerometer().result
  # - is left & backwards, + is right & forwards
  x = pos[1]
  y = pos[0]
  if y < 2:
    return 'f'
  elif y > 8:
    return 'b'
  elif x < -3:
    return 'l'
  elif x > 3:
    return 'r'
  else:
    return 's'

# create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to server
host = raw_input("Host IP: ") # server address
port = int(raw_input("Port: ")) # server port
s.connect((host, port))
s.settimeout(0.0)
# android setup
droid = android.Android() 
droid.startSensingTimed(2, 100)
running = True
while running:
  sen_mes = read_accel(droid)
  if sen_mes != None:
    s.send(sen_mes) 
    if sen_mes == "quit":
      running = False
# close the connection
s.close()
