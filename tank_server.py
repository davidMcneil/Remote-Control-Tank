import socket
import sys
import select
import serial

# create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# associate the socket with a port
host = '' # can leave this blank on the server side
port = int(raw_input("Port: "))
s.bind((host, port))
# accept "call" from client
s.listen(1)
conn, addr = s.accept()
print 'Client connected at: ', addr
conn.settimeout(0.0)
running = True
try:
  ser = serial.Serial('/dev/ttyACM0', 9600)
  print "Found serial port"
except:
  print "No serial port"
while running:
  try:
    rec_mes = conn.recv(100000) # read up to 1000000 bytes
    print 'Command: ', rec_mes
    try:
      ser.write(rec_mes)
    except:
      pass
    if rec_mes == "quit":
      running = False
  except:
    pass
# close the connection
ser.close()
conn.close()


  
